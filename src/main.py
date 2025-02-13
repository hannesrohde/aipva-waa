import sys

def main():
    print("Welcome!")

    # Part 1: speech-to-text
    # - "push to talk" : Aufnahme während Leertaste gedrückt ist
    # - aufgenommenes Audio mittels whisper verarbeiten und Text erkennen
    # - Text in Variable input speichern

    audiofile = os.path.join('testfile.mp3')

    model = whisper.load_model("tiny")
    result = model.transcribe("../audio/wie geht es dir.wav")
    print(result["text"])

    input = 'Hallo Maschine, wie geht es dir?'

    # ----------------------------------------------------------

    # Part 2: LLM request
    # - Prompt zusammenstellen:
    #   - "user"-Prompt aus input
    #   - "system"-Prompt definieren
    # - API-Call absenden
    # - Resultat parsen und Ausgabe-String in Variable output speichern

    output = 'Danke dass du fragst! Mir geht es heute super!'

    # ----------------------------------------------------------

    # Part 3: text-to-speech
    # - Text aus Output an Mimic3 übergeben
    # - Audiosignal erzeugen
    # - Audiosignal abspielen

if __name__ == "__main__":
    main()
