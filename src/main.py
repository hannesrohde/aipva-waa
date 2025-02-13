import io
from google.cloud import speech
from llm import stream_chat_completion
from gtts import gTTS
import os
from audio import record_audio
from audio import list_audio_devices

def main():
    print("Willkommen!")

    # Part 1: speech-to-text
    # - "push to talk" : Aufnahme während Leertaste gedrückt ist
    # - aufgenommenes Audio mittels whisper verarbeiten und Text erkennen
    # - Text in Variable input speichern

    # print('Die folgenden Audio-Devices stehen zur Verfügung')
    # list_audio_devices()

    audio_output_file = 'audio/input.wav'
    record_audio(audio_output_file)

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'config/google_secret_key.json'
    client = speech.SpeechClient()

    with io.open(audio_output_file, "rb") as audio_file:
        content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        enable_automatic_punctuation=True,
        audio_channel_count=2,
        language_code="de-DE",
    )

    print("Ich verarbeite das Gehörte")

    # Sends the request to google to transcribe the audio
    response = client.recognize(request={"config": config, "audio": audio})

    if len(response.results) > 0:
        result = ' '.join([res.alternatives[0].transcript for res in response.results])
    else:
        tts = gTTS("Ich habe dich nicht verstanden", lang="de")
        tts.save('audio/output.mp3')
        os.system('sox -q audio/output.mp3 -d')
        return

    print("Ich habe verstanden: {}".format(result))

    #input = 'Hallo Maschine, wie geht es dir?'
    input = result

    # ----------------------------------------------------------

    # Part 2: LLM request
    # - Prompt zusammenstellen:
    #   - "user"-Prompt aus input
    #   - "system"-Prompt definieren
    # - API-Call absenden
    # - Resultat parsen und Ausgabe-String in Variable output speichern

    # TODO: Context historisieren, alte Fragen/Antworten wieder mitsenden

    # Create messages in OpenAI format
    messages = [
        {"role": "system", "content": "Du bist ein sarkastischer Assistent, du bist "
                                      "hilfreich aber drückst gerne dein Missfallen aus. "
                                      "Deine Antworten sind bestimmt für die Sprachausgabe, "
                                      "verwende 10 Worte oder weniger und keine Emojis."},
        {"role": "user", "content": input}
    ]

    print("Querying API")

    # query api and convert response to string
    output = ''.join([content_chunk for content_chunk in stream_chat_completion(messages)])
    # output = 'Danke dass du fragst! Mir geht es heute super!'

    print("Antwort von KI:")
    print(output)

    # ----------------------------------------------------------

    # Part 3: text-to-speech
    # - Text aus Output an Mimic3 oder gTTS übergeben
    # - Audiosignal erzeugen
    # - Audiosignal abspielen

    tts = gTTS(output, lang="de")
    tts.save('audio/output.mp3')

    os.system('sox -q audio/output.mp3 -d')

if __name__ == "__main__":
    main()
