import time
from pynput import keyboard

space_pressed = False

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

    global space_pressed
    if key == keyboard.Key.space:
        space_pressed = True

def on_release(key):
    print('{0} released'.format(key))
    global space_pressed
    if key == keyboard.Key.space:
        space_pressed = False
        return False # stop listener

def main():
    #with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    #    listener.join()

    #listener = keyboard.Listener(
    #    on_press=on_press,
    #    on_release=on_release)
    #listener.start()

    #while not space_pressed:
    #    print(space_pressed)
    #    time.sleep(0.1)

    #print('Aufnahme läuft...')

    #while space_pressed:
    #    print('space pressed')

    #print('Ende')

    print('start')
    while True:
        with keyboard.Events() as events:
            # Block at most one second
            event = events.get(1.0)
            if event is None:
                print('You did not press a key within one second')
            else:
                print('Received event {}'.format(event))

    print('ende')

    #listener.stop()


if __name__ == "__main__":
    main()
