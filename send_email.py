from datetime import datetime
from email.message import EmailMessage
import smtplib

class Send_Email:
    def __init__(self):
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        self.msg = EmailMessage()

        #date and time format: dd/mm/YYYY H:M:S
        self.format = "%d/%m/%Y %H:%M:%S"
    
    def get_time(self):
        self.now = datetime.now()
        self.time_formatted = str(self.now.strftime(format))
        return self.time_formatted

    def notif(self):
        self.msg['Subject'] = "Motion at your Door!"
        self.msg['From'] = "shayleecoulter@outlook.com"
        self.msg['To'] = "shaylee.coulter@csedge.org"

        self.msg.set_content("There has been motion detected at your door at " + self.get_time() + ". Please go to http://0.0.0.0:5000/ to acess livestream video of your door")
        #replace with your own credentials
        self.server.login("RobotShaylee@gmail.com","IAmNotARobot" )

        #send email   
        self.server.send_message(self.msg)
        print("sending email...")
        self.server.quit() 