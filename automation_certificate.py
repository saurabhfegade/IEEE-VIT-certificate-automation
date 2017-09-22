import os
from os import listdir
import csv
from PIL import Image,ImageDraw,ImageFont
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def sending_email(from_address, to_address, names, password):
        msg = MIMEMultipart() 
        msg['From'] = from_address 
        msg['To'] = to_address 
        msg['Subject'] = "Certificate"
        body = ' '
        msg.attach(MIMEText(body, 'plain')) # attaching the body with the msg instance
          
        filename = "%s.jpg" %names # opening the file to be sent
        attachment = open(path, "rb") # Enter path of the certificates as raw string 
                                      # e.g. r"C:\Users\Saurabh\Desktop\Certificate Automation\certificates\%s.jpg" %names
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())

        encoders.encode_base64(p)
          
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                 
        msg.attach(p) # attach the instance 'p' to instance 'msg'        

        session = smtplib.SMTP('smtp.gmail.com', 587) # creates SMTP session         
        session.starttls()         
        session.login(from_address, password)# Authentication         
        text = msg.as_string()# Converts the Multipart message into a string        
        session.sendmail(from_address, to_address, text)         
        session.quit()

def generating_certificate(filename, certificate, textfont):
    with open(filename, newline='') as csvfile:
        read = csv.reader(csvfile,delimiter='`', quotechar='|')
        read = csv.DictReader(csvfile)
        for row in read:
            names = row['FULL NAME'] # Taking names
            print(names)
            image = Image.open(certificate) # opening the certificate
            x,y = image.size
            font_type = ImageFont.truetype(textfont,80) # specifying font type and size
            draw = ImageDraw.Draw(image)
            a,b = font_type.getsize(names) # storing size of the text to be applied i.e. names 
            draw.text(xy = (650-a/2,410),text = names, fill=(255,0,0),font = font_type)
            image.save(os.path.join('certificates' , names +'.jpg'))
            to_address = row['EMAIL ID'] # Taking email ids
            print(to_address)
            sending_email(from_address, to_address, names, password)

os.makedirs('certificates',exist_ok=True) # make new folder names certificates in working directory
generating_certificate('responses1.csv', 'Sample Certificate.jpg', 'DobkinScript.ttf')




    
        

