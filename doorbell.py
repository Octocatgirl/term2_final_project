import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import pygame
from time import sleep

pygame.init()
pygame.mixer.init()
# load the sound file


bellring = pygame.mixer.Sound("Doorbell-Sound.wav")

def button_callback(channel):
    print("Button was pushed!")
    bellring.play()
    sleep(0.75)


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

GPIO.add_event_detect(27,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge

message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up

# class Doorbell():
#     def __init__(self):
#         self.bellring = pygame.mixer.Sound("Doorbell-Sound.wav")

#     def button_callback(self):
#         print("Button was pushed!")
#         self.bellring.play()
#         sleep(0.75)
        
#     def ringing(self):
#         GPIO.add_event_detect(27,GPIO.RISING,callback= self.button_callback) # Setup event on pin 10 rising edge

# doorbell = Doorbell()

# doorbell.ringing()