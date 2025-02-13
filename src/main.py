import io
import sys
from google.cloud import speech
from llm import stream_chat_completion
from gtts import gTTS
import os
from audio import record_audio
from audio import list_audio_devices


def main():
    print("Welcome!")

    # Part 1: speech-to-text
    # - "push to talk" : Aufnahme während Leertaste gedrückt ist
    # - aufgenommenes Audio mittels whisper verarbeiten und Text erkennen
    # - Text in Variable input speichern

    # print('Die folgenden Audio-Devices stehen zur Verfügung')
    # list_audio_devices()

    print('Drücke und halte die Space-Taste, um mit mir zu reden!')
    audio_output_file = 'audio/input.wav'
    record_audio(audio_output_file)

    # os.environ['GOOGLE_APPLICATION_CREDENTIALS']= 'google_secret_key.json'
    # client = speech.SpeechClient()
    #
    # audiofile = os.path.join('..', 'audio', 'wie geht es dir.wav')
    #
    # with io.open(audiofile, "rb") as audio_file:
    #     content = audio_file.read()
    #     audio = speech.RecognitionAudio(content=content)
    #
    # config = speech.RecognitionConfig(
    #     encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    #     enable_automatic_punctuation=True,
    #     audio_channel_count=2,
    #     language_code="de-DE",
    # )
    #
    # # Sends the request to google to transcribe the audio
    # response = client.recognize(request={"config": config, "audio": audio})
    # # Reads the response
    # for result in response.results:
    #     print("Transcript: {}".format(result.alternatives[0].transcript))

    input = 'Hallo Maschine, wie geht es dir?'

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

    print("Assistant's Response:")
    print(output)

    # ----------------------------------------------------------

    # Part 3: text-to-speech
    # - Text aus Output an Mimic3 oder gTTS übergeben
    # - Audiosignal erzeugen
    # - Audiosignal abspielen

    tts = gTTS(output, lang="de")
    tts.save('audio/output.mp3')

    os.system('sox audio/output.mp3 -d')

if __name__ == "__main__":
    main()
