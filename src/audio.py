import wave
import pyaudio
from pynput import keyboard

space_pressed = False

def on_press(key):
    global space_pressed
    if key == keyboard.Key.space:
        space_pressed = True

def on_release(key):
    global space_pressed
    if key == keyboard.Key.space:
        space_pressed = False
        return False # stop listener

def record_audio(output_file):
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    print('Aufnahme läuft...')
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)
    frames = []

    while space_pressed:
        data = stream.read(chunk)
        frames.append(data)

    print('Recording stopped')
    stream.stop_stream()
    stream.close()

    wf = wave.open(output_file, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

    p.terminate()
