from gpiozero import MotionSensor, LED
from time import sleep

# pir = MotionSensor(4)


# while True: 
#     if pir.motion_detected:
#         motion_detected = True
#     else:
#         motion_detected = False

class Motion:
    def __init__(self):
        self.pir = MotionSensor(4)
        self.motion_detected = self.pir.motion_detected

    def motion_detection(self):
        self.motion_detected = self.pir.motion_detected
        print(self.motion_detected)

    def is_motion_detected(self):
        self.motion_detection()
        return self.motion_detected





    

        
        
 