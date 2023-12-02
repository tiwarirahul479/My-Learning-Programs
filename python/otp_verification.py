import os
import math
import random
import smtplib

digits = "0123456789"
otp = ""

for i in range(6):
    otp += digits[math.floor(random.random()*10)]

msg = f"{otp} is your OTP. Kindly donot share it with anyone."

try:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("tiwarirahul479@gmail.com","Rahul@123")

    user_email = input("Enter the your mail: ")
    s.sendmail('==================', user_email, msg)
except Exception as e:
    print("Something happened while sending the mail -------",e)

left_attempts = 3
while True:
    o = input("Enter your OTP: ")
    if o == otp:
        print("OTP Veirifed sucessfully!")
        break
    else:
        print("Incorrect OTP!!!")
        if left_attempts > 0:
            try_again = input(f"{left_attempts} attempts left. Want to try again? (y/n): ").lower()
            if try_again == 'n':
                print("Thanks for your response.")
                break
            else:
                left_attempts -= 1
                continue
        else:
            print("Sorry no attempts left. Kindly try again after some time.")
            break