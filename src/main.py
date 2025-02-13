import io
import os
import sys
from google.cloud import speech
from llm import stream_chat_completion

def main():
    print("Welcome!")

    # Part 1: speech-to-text
    # - "push to talk" : Aufnahme während Leertaste gedrückt ist
    # - aufgenommenes Audio mittels whisper verarbeiten und Text erkennen
    # - Text in Variable input speichern

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

    # Create messages in OpenAI format
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": input}
    ]

    try:
        print("Assistant's Response:")
        # Stream the response
        for content_chunk in stream_chat_completion(messages):
            print(content_chunk, end='', flush=True)
        print("")

    except Exception as e:
        print(f"Error: {str(e)}")

    output = 'Danke dass du fragst! Mir geht es heute super!'

    # ----------------------------------------------------------

    # Part 3: text-to-speech
    # - Text aus Output an Mimic3 oder gTTS übergeben
    # - Audiosignal erzeugen
    # - Audiosignal abspielen

if __name__ == "__main__":
    main()
