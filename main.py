import random
import datetime as dt
import smtplib

user_email = input("Type your exact e-mail (Gmail) address: ")
app_password = input("After this step https://support.google.com/mail/answer/185833?hl=en\n"
                     "type your app password: ")
friend_email = input("Now, type your friend's e-mail: ")


def send_email(email_sender, password, receiver_email, message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email_sender, password=password)
        connection.sendmail(from_addr=email_sender,
                            to_addrs=receiver_email,
                            msg=message)


now = dt.datetime.now()
weekday_now = now.weekday()

if weekday_now == 6:  # If is Sunday
    with open("quotes.txt", mode="r") as quotes_txt:
        lines = quotes_txt.readlines()
        motivational_phrase = random.choice(lines)

    my_message = f"Subject: Here's your motivation!\n\n" \
                 f"Dear friend, " \
                 f"thank you for your friendship in my life. " \
                 f"You are special and this Sunday I want to send you a motivational message:\n\n" \
                 f"{motivational_phrase}\n" \
                 f"Have a great week!"

    send_email(email_sender=user_email, password=app_password, receiver_email=friend_email, message=my_message)

    input("Your email was sent successfully...")
