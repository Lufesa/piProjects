import tkinter as tk
import time
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

recorded = 0
GPIO.setup(11,GPIO.OUT)
pwm = GPIO.PWM(11,50)
pwm.start(0)

class Display:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Fuck me")

        self.slide1 = tk.Scale(self.root, from_=0, to=180, tickinterval=10, length = 300)
        self.button = tk.Button(self.root, text="colis",command=record).pack()
        self.radio1 = tk.Radiobutton(self.root, text = "record", value = 1, variable = 'var', command=record)
        self.radio2 = tk.Radiobutton(self.root, text = "don't record", value = 2,variable = 'var',command = doNotRecord )
        self.radio1.pack()
        self.radio2.pack()
        self.slide1.pack()

def SetAngle(angle):
    	duty = angle/18 + 2
	GPIO.output(11,True)
	pwm.ChangeDutyCycle(duty)
	sleep(3)
	#GPIO.output(11,False)
	pwm.ChangeDutyCycle(0)
def record():
    global recorded
    recorded = 1
    #print("FUCKs1")
def doNotRecord():
    global recorded
    recorded = 0
    #print("FUCKs2")

display = Display()

for i in range(1,200):
    display.root.update()
    SetAngle(display.slide1.get())

    #if (record==1):
    #        print("recording")

    #else:
       # print("FUCKs")
    #print(display.slide1.get())
    #print(recorded)
    time.sleep(0.1)

pwm.stop()
GPIO.cleanup()

