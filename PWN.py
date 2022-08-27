import RPi.GPIO as GPIO

channel = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.OUT)
i = None
p = GPIO.PWM(channel,30)
p.start(30)

try:
	while i != "quit":
		try:
			f = input("Enter Frequency: \n")
			d = input("Enter Duty Cycle: \n")

			if(f == "q" or d == "q"):
				break

			p.ChangeFrequency(int(f))
			p.ChangeDutyCycle(int(d))

		except Exception as e:
			pass

except KeyboardInterrupt as e:
	print("Recieved Ctrl+C Quiting\n")
	pass

p.stop()
GPIO.cleanup()
print("Quiting\n")