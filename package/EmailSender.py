from config import Config

class Email():

    def __init__(self):
        self.emailid = Config.EMAIL_ID
        self.emailpassword=Config.EMAIL_PASSWORD


    def postiveprice_Email(self,email,username,stockname,buy,price):

        SUBJECT = f'Stock Updates(positive): {stockname}'

        TEXT = f"Hi {username},\n\nThe stock price is in positive flow. \n\nStock Name : {stockname}\n\nStock brought Price : {buy}\n\nRight now Stock Price : {price}\n \nThanks,\n Sherlock"

        # message to be sent
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

        print(email,message)

        self.trigger_email(email,message)



    def targetprice_email(self,email,username,stockname,buy,price):

        SUBJECT = f'Stock Updates:(target) {stockname}'

        TEXT = f"Hi {username},\n\nThe stock price is reach the target price. \n\nStock Name : {stockname}\n\nStock brought Price : {buy}\n\nRight now Stock Price : {price}\n \nThanks,\n Sherlock"

        # message to be sent
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

        print(email, message)

        self.trigger_email(email, message)


    def loss_email(self,email,username,stockname,buy,price):

        SUBJECT = f'Stock Updates:(loss) {stockname}'

        TEXT = f"Hi {username},\n\nThe stock price is going loss right now. \n\nStock Name : {stockname}\n\nStock brought Price : {buy}\n\nRight now Stock Price : {price}\n \nThanks,\n Sherlock"

        # message to be sent
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

        print(email, message)

        self.trigger_email(email, message)




    def trigger_email(self,senderemail,message):
        # Python code to illustrate Sending mail from
        # your Gmail account
        import smtplib

        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(self.emailid, self.emailpassword)

        # sending the mail
        s.sendmail(self.emailid, senderemail, message)

        # terminating the session
        s.quit()