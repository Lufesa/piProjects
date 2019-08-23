import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
pwm = GPIO.PWM(11,50)
pwm.start(0)

angles = [20,120,150,100,10,100,120,180,0]

def SetAngle(angle):
	duty = angle/18 + 2
	GPIO.output(11,True)
	pwm.ChangeDutyCycle(duty)
	sleep(3)
	#GPIO.output(11,False)
	pwm.ChangeDutyCycle(0)
	
	
for i in angles:
	SetAngle(i)

pwm.stop()
GPIO.cleanup()
