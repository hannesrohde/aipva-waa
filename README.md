# aipva-waa
AI-powered voice assistant ... with an attitude!

![aipva](./mysterious-machine.png)
*Bild generiert mit Dall-E*

## Ein Spaß-Projekt für den Workshop der Github Copilot-Schulung

Realisiert wird ein Voice Chatbot, der Eingaben per Sprache annimmt, als Prompt
an ein LLM sendet und die Antwort wiederum als Sprache ausgibt.

## Installation

Das Projekt verwendet Poetry zur Python-Paketverwaltung, das auf dem System installiert sein muss.

```shell
poetry install
poetry run python src/main.py
```

## Umgebung

Das Programm benötigt API-Keys von [NanoGPT](https://nano-gpt.com/api) und Google Cloud:

Der API-Key für NanoGPT wird als Umgebungsvariable gesetzt:

```shell
export NANOGPT_API_KEY=abcd-efg-hij
```

Die Google API Secret Key Datei für Speech-To-Text muss unter `config/google_secret_key.json` abgespeichert sein.


## Details

- "Push-to-talk": die Benutzer:Innen halten eine Taste gedrückt, während sie in das Mikrophon des Rechners sprechen
- Prompt generieren
  - kurze und knackige Antworten für die Sprachausgabe
  - interessanter "Charakter" des Chatbots
- LLM-Request via nano-gpt.com, OpenAI-kompatibles API
  - https://nano-gpt.com/api
  - https://platform.openai.com/docs/guides/text-generation

## Technologien
- Python
- OpenAI API
- Google Cloud Speech-to-Text, Text-to-Speech
- TODO: lokal [Whisper](https://github.com/openai/whisper)
- TODO: lokal [Mimic3](https://community.openconversational.ai/t/introducing-mimic-3/12256) 
