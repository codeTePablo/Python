import smtplib # Simple Mail Transfer Protocol
from dotenv import load_dotenv
import os

load_dotenv() # load .env
my_email = os.environ["my_email"] # protect email 
my_password = os.environ["my_password"] # protect password
send_to = "jopsan63@gmail.com"

with smtplib.SMTP("smtp.gmail.com") as connection: # location  
    connection.starttls() # make secure email and avoid intercepted
    connection.login(user=my_email, password=my_password) 

    connection.sendmail(from_addr=my_email, to_addrs=send_to, msg="Hello")
    # connection.close()