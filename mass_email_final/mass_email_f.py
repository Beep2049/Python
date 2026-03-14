import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass
import time

def get_recipients():
    recipients = []
    print("Email Recipients Information")
    
    while True:
        name = input("Enter Recipient Name: ").strip()
        if len(name) < 2 or not name:
            print("Invalid name, try again")
            continue

        email = input("Enter Recipient Email: ").strip()
        if '@' not in email or '.' not in email:
            print("Invalid email, try again")
            continue

        if name and email:
            print(f"Is this information correct ?")
            print(f"Name: {name}, email: {email}")
            answer = input("Yes or No: ").strip().lower()
            if answer != "yes":
                print("Retype the information please")
                continue
            else:
                recipients.append({"name": name, "email": email})
                print(f"Added {name} <{email}>")

        more_email = input("Add more recipients?: ").strip().lower()
        if more_email == 'no':
            break

    return recipients


def mass_email(recipients ,my_email, password, smtp_server="smtp.gmail.com", port=587):
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(my_email, password)

    results = {'success' : 0, 'failure' : 0, 'emails': []}
    for i, person in enumerate(recipients, 1):
        try:
            print(f"Sending {i}/{len(recipients)} emails to {person['email']}")

            msg = MIMEMultipart('alternative')
            msg['From'] = my_email
            msg['To'] = person['email']
            msg['Subject'] = f"For {person['name']} regarding..." #Edit
            msg['Bcc'] = ','.join([r['email'] for r in recipients])
            
            html_text =  MIMEText("")
            plain_text = MIMEText( "<html><body><p></p></body></html>")

            msg.attach(html_text)
            msg.attach(plain_text)

            server.send_message(msg)
            print(f"Email sent to {person['email']}")
            results['success'] += 1

            if i < len(recipients):
                time.sleep(2)

        except Exception as e:
            print(f"Error sending email to {person['email']}: {e}")
            results['failure'] += 1
            results['emails'].append(person['email'])
        
    server.quit()
    print(f"Emails Successfully sent: {results['success']}/{len(recipients)}")
    
    if results['emails']:
        print(f"Emails Unsuccessfully sent: {results['failure']}")
        print(f"Failed Emails: {','.join(results['emails'])}")
    
    return results

#Password: 
#gmail - tqhm fobp cjrh pqxs(no spaces)
#zoho - 
#other - 
app_password = getpass.getpass("Enter Password: ")

if __name__ == "__main__":
    mass_email(
        recipients=get_recipients(),
        my_email="ericb725@gmail.com",
        password=app_password
    )

    