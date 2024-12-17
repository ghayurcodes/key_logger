import smtplib

sender = "goku <hello@demomailtrap.com>"
receiver = " <superboiko124@gmail.com>"

message = f"""\
Subject: Hola man 
To: {receiver}
From: {sender}

This is a test e-mail message ok amnana."""

with smtplib.SMTP("live.smtp.mailtrap.io", 587) as server:
    server.starttls()
    server.login("api", "1c5bfd794a9aa716ef911a2c2013d77c")
    server.sendmail(sender, receiver, message)