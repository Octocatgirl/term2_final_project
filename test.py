from motionsensor import Motion
from time import sleep
from gpiozero import MotionSensor, LED

motion = Motion()

while True:
    motion.is_motion_detected()