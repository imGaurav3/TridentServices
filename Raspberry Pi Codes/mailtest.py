import smtplib

s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("ketkikokate199@gmail.com","7798398892")
msg = "Hello"
s.sendmail("ketkikokate199@gmail.com","rishabhgandhewar@gmail.com",msg)
s.quit()
