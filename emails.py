# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    emails.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ommohame < ommohame@student.42abudhabi.ae> +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/08/08 21:27:46 by ommohame          #+#    #+#              #
#    Updated: 2022/08/08 23:39:05 by ommohame         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from my_config import email_host
from my_config import email_port
from my_config import email_id
from my_config import email_pass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from database import *
from tqdm import tqdm
import smtplib

def send_emails(connection):
	seats = call_query(connection, "SELECT * FROM seats WHERE student IS NOT NULL").fetchall()
	for seat in tqdm(seats, desc='sending emails', ascii='░▒█'):
		student = call_query(connection, f"SELECT * FROM exam WHERE login = '{seat[1]}'").fetchone()
		login = student[0]
		first_name = student[1]
		last_name = student[2]
		email = student[3]
		seat = student[4]
		msg = MIMEMultipart()
		msg['From'] = email_id
		msg['To'] = email
		msg['Subject'] = 'Exam seat'
		message =  f"""
		Dear {first_name} {last_name},
			
		You have successfully subscribed to the exam session.

		You have been assigned to: {seat}.

		As a reminder, no phones or devices are allowed during your exam, and  you are required to carry your studentID during the session.

		Good luck and keep swimming !

		Kind Regards,

		42abudhabi"""
		msg.attach(MIMEText(message))
		mail = smtplib.SMTP(email_host, email_port)
		mail.ehlo()
		mail.starttls()
		mail.ehlo()
		mail.login(email_id, email_pass)
		mail.sendmail(email_id, email, msg.as_string())
		mail.quit()