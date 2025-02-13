# aipva-waa
AI-powered voice assistant ... with an attitude!

![aipva](./mysterious-machine.png)
*Bild generiert mit Dall-E*

## Ein Spaß-Projekt für den Workshop der Github Copilot-Schulung

Realisiert wird ein Voice Chatbot, der Eingaben per Sprache annimmt, als Prompt
an ein LLM sendet und die Antwort wiederum als Sprache ausgibt.

## Installation

Das Projekt verwendet Poetry zur Python-Paketverwaltung.

````
poetry init
poetry run python src/main.py
````




## Details

- "Push-to-talk": die Benutzer:Innen halten eine Taste gedrückt, während sie in das Mikrophon des Rechners sprechen
- Speech-to-text: "whisper"?
- Prompt generieren
  - kurze und knackige Antworten für die Sprachausgabe
  - interessanter "Charakter" des Chatbots
- LLM-Request via nano-gpt.com, OpenAI-kompatibles API
  - https://nano-gpt.com/api
  - https://platform.openai.com/docs/guides/text-generation
- text-to-speech: Mimic3
  - https://community.openconversational.ai/t/how-to-use-mimic3-directly-from-python-code/12778

## Technologien
- Python
- OpenAI API
- [Whisper](https://github.com/openai/whisper)
- [Mimic3](https://community.openconversational.ai/t/introducing-mimic-3/12256) 
