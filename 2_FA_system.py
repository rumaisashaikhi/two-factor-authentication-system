import pyotp
import smtplib
from email.message import EmailMessage

# Step 1: User database (demo purpose)
USERNAME = "admin"
PASSWORD = "secure123"

# Step 2: Generate secret key for OTP
secret = pyotp.random_base32()
totp = pyotp.TOTP(secret)

def send_otp_email(otp):
    # ===== EMAIL SETTINGS (REPLACE WITH YOUR OWN) =====
    sender_email = "your_email@gmail.com"   # Add your email
    sender_password = "your_app_password"  # Use app password, not real Gmail password
    receiver_email = "receiver_email@gmail.com"   # Add your email

    msg = EmailMessage()
    msg.set_content(f"Your OTP code is: {otp}")
    msg['Subject'] = "Your Login OTP Code"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)

print("=== 2FA Login System ===")

user = input("Enter username: ")
pw = input("Enter password: ")

if user == USERNAME and pw == PASSWORD:
    print("Password correct. Sending OTP...")

    otp = totp.now()
    send_otp_email(otp)

    entered_otp = input("Enter OTP sent to your email: ")

    if totp.verify(entered_otp):
        print("✅ Login Successful with 2FA!")
    else:
        print("❌ Invalid OTP. Access Denied.")
else:
    print("❌ Wrong username or password.")
