import wave
import pyaudio
from pynput import keyboard

def list_audio_devices():
    """
    Lists all audio devices available on the system.
    """
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        print(f"Device {i}: {info['name']}")
    p.terminate()

def record_audio(output_file):
    """
    Records audio from the default input device until the space bar is released.

    Args:
        output_file
    """
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
                    input=True,
                    input_device_index=5)
    frames = []

    while True:
        if space_pressed:
            data = stream.read(chunk)
            frames.append(data)
        else:
            break

    print('Aufnahme beendet')
    stream.stop_stream()
    stream.close()

    wf = wave.open(output_file, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

    p.terminate()
