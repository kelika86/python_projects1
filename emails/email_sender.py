import smtplib 
from string import Template
from pathlib import Path 

html= Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'bill'
email['to'] = 'bill@aol.com'
email['subject'] = "It's Bill!"

email.set_content(html.substitute(name = 'Bill'), 'html') 

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls() 
    smtp.login('bill@gmail.com', 'bill')
    smtp.send_message(email)
    print('all good')