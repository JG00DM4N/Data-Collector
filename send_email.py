from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, count):
    from_email= "jonathon.goodman@gmail.com"
    from_password= "djmcselezahyjeph"
    to_email=email

    subject="Height Data"
    message="Hey there. Your Height is <strong>%s</strong> cm. <br>The average height for all submissions is <strong>%s</strong> cm. <br>There have been <strong>%s</strong> submissions so far." % (height, average_height, count)


    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)

