from flask import Flask, render_template, Response
from rpicamera import RPiCamera
from time import sleep
from motionsensor import Motion
from gpiozero import MotionSensor, LED, Button
# from doorbell import Doorbell
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
# use gpio library to get button value to make if statment for button press
from datetime import datetime
from email.message import EmailMessage
import smtplib, pygame



app = Flask(__name__)

motion = Motion()
# email = Send_Email()
# bell = Doorbell()
#use smptlib to send using gmail server, on port 465. 
pygame.init()
pygame.mixer.init()
#load the sound file

button = Button(27)


counter = 0
is_waiting = True

def get_time():
    now = datetime.now()
    format = "%d/%m/%Y %H:%M:%S"
    time_formated = now.strftime(format)
    return str(time_formated)


def sendEmail():
    print("Initializing email...")
    msg = EmailMessage()
    msg['Subject'] = "Hello!"
    msg['From'] = "RobotShaylee@gmail.com"
    msg['To'] = "shaylee.coulter@csedge.org"

    msg.set_content("There has been motion detected at your door at " + get_time() + ". Please go to http://0.0.0.0:5000/ to acess livestream video of your door")
    
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("RobotShaylee@gmail.com", "IAmNotARobot")
    server.send_message(msg)
    
    print("sending email...")
    server.quit()  


def button_callback(channel):
    print("Button was pushed!")
    bellring.play()
    sleep(0.75)

@app.route('/')
def index():
    return render_template('index.html') 

def gen(camera):
    while True:
        print("button: " + str(button.is_pressed))

        frame = camera.get_frame()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')   
       
        if motion.is_motion_detected():
            # sendEmail()
            # is_waiting = False
            pass
           
        
            
           

@app.route('/stream')
def stream():
    feed = Response(gen(RPiCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')
    return feed

if __name__ =='__main__':
    app.run(host = '0.0.0.0', debug = True)