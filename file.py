# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    file.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ommohame < ommohame@student.42abudhabi.ae> +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/08/08 22:26:18 by ommohame          #+#    #+#              #
#    Updated: 2022/08/08 22:41:53 by ommohame         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from database import *

def get_file(connection):
	with open("seats.txt", "w") as file:
		seats = call_query(connection, "SELECT * FROM seats WHERE student IS NOT NULL").fetchall()
		for seat in seats:
			student = call_query(connection, f"SELECT * FROM exam WHERE login = '{seat[1]}'").fetchone()
			login = student[0]
			first_name = student[1]
			last_name = student[2]
			email = student[3]
			seat = student[4]
			file.write(f"{seat}, {login}, {first_name} {last_name}, {email}\n")
