import RPi.GPIO as GPIO

channel = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.OUT)
i = None
p = GPIO.PWM(channel,50)
p.start(50)

try:
	while True:
		try:
			d = input("Enter Brightness Level(Duty Cycle): \n")

			if(d == "q"):
				break

			p.ChangeDutyCycle(int(d))

		except Exception as e:
			pass

except KeyboardInterrupt as e:
	print("Recieved Ctrl+C Quiting\n")
	pass

p.stop()
GPIO.cleanup()
print("Quiting\n")