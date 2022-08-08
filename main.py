# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ommohame < ommohame@student.42abudhabi.ae> +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/07/29 04:35:26 by ommohame          #+#    #+#              #
#    Updated: 2022/08/08 23:41:48 by ommohame         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

### connects to the SQLite database ###
### creates student table if it doesn't exist ###
### deletes previous exam table and creates the new one ###
import email
from database import *
from config import sql_data
connection = create_connection(sql_data)
call_query(connection, create_students_table)
call_query(connection, "DROP TABLE IF EXISTS seats")
call_query(connection, create_seats_table)
call_query(connection, "DROP TABLE IF EXISTS exam")
call_query(connection, create_exam_table)

### gets the data from the api and saves them into a variable ###
### it uses 42api-lib by hibehelsinki on github :)) ###
from get_data import get_api
response = get_api()

### inits the script when it starts ###
### if there's new students it's gonna add them to the student table in the daatabase ###
### add exam students to exam table ###
### add avaliable seats to seats table ###
from init_script import init_script
init_script(connection, response)


### BIGGG BRAIN ALGO?? ###
### 1 day later: nope ####
from algorithim import algoritim
algoritim(connection)

### creates a file with all seatings details ####
from file import get_file
get_file(connection)

### send emails ###
from emails import send_emails
emails = input("Do you want to send email? (y/n): ")
while True:
	if emails == 'y':
		send_emails(connection)
		break
	elif emails == 'n':
		break
	else:
		emails = input("you have to enter y or n: ")

connection.close()