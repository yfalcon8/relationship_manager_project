import smtplib

content = "your python email worked! mmm!"

# server and port (465 or 587 for gmail)
mail = smtplib.SMTP('smtp.gmail.com', 587)

# Identify yourself to server by helo (regular) or ehlo (esmtp server).
# mail.ehlo()

# Start TLS mode (transport layer security).
# Any smtp command that comes after this code will be encrypted.
mail.starttls()

mail.login("relationshipmanagerhb@gmail.com", "fulfillinspiremotivate")

mail.sendmail("relationshipmanagerhb@gmail.com", "yfalcon8@gmail.com", content)

mail.quit()
