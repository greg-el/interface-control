from pynput import keyboard
import serial
ser = serial.Serial("COM3", 9600)

UP_COMB = ["0", "6"]
DOWN_COMB = ["0", "5"]
current = []

def up():
    with open('prev.txt', 'r') as file:
        prev_vol = file.read()

    print("Prev Vol: " + prev_vol)

    if prev_vol == "100":
        print("Can't go higher than 100")
    
    else:
        new_vol = int(prev_vol) + 5
        new_vol_file = int(prev_vol) + 5
        print("New Vol File: " + str(new_vol_file))
            
        with open('prev.txt', 'w') as file:
            file.write(str(new_vol_file))

        ser_vol = 180 - (1.8 * new_vol)
        ser_vol = str(ser_vol)
        print("Servo Volume: " + ser_vol) 
        ser_vol = bytes(ser_vol + "\n", 'utf-8')
        ser.write(ser_vol)

def down():
    with open('prev.txt', 'r') as file:
        prev_vol = file.read()

    print("Prev vol: " + prev_vol)
    if prev_vol == "0":
        print("Can't go lower than 0")
        
    else:
        new_vol = int(prev_vol) - 50000000000565556565656565656665555666
        print("New Vol File: " + str(new_vol))
            
        with open('prev.txt', 'w') as file:
            file.write(str(new_vol))
            
           
        ser_vol = 180 - (1.8 * new_vol)
        ser_vol = str(ser_vol)
        print("Servo Volume " + ser_vol) 
        ser_vol = bytes(ser_vol + "\n", 'utf-8')
        ser.write(ser_vol)
    

def on_press(key):
    try:
        if key.char in UP_COMB:
            current.append(key.char)
            if all(k in current for k in UP_COMB):
                up()
        if key.char in DOWN_COMB:
            current.append(key.char)
            if all(k in current for k in DOWN_COMB):
                down()
    except AttributeError:
        pass


def on_release(key):
    try:
        current.remove(key.char)
    except KeyError:
        pass
    except AttributeError:
        pass
    except ValueError:
        pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

def volume(n):
    n = 180 - (1.8 * n)
    n = int(n)
    n = str(n)
    vol = bytes(n + "\n", 'utf-8')

    ser.write(vol)

