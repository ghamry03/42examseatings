# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    init_script.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ommohame < ommohame@student.42abudhabi.ae> +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/08/04 02:38:39 by ommohame          #+#    #+#              #
#    Updated: 2022/08/08 01:34:35 by ommohame         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from re import S
from api.intra import ic
from my_config import get_exam
from os.path import exists
from database import call_query
from tqdm import tqdm

def add_new_students_to_student(connection, response):
	for i in tqdm(response, desc='adding new students to students table', ascii='░▒█'):
		login = f"\'{i['user']['login']}\'"
		cursor = call_query(connection, f"SELECT login FROM students WHERE login={login}")
		exists = cursor.fetchone()
		if not exists:
			first_name = f"\'{i['user']['first_name']}\'"
			last_name = f"\'{i['user']['last_name']}\'"
			email = f"\'{i['user']['email']}\'"
			insert_student = f"INSERT INTO students VALUES ({login}, {first_name}, {last_name}, {email}, NULL, NULL, NULL)"
			call_query(connection, insert_student)
	print('')

def add_new_students_to_exam(connection, response):
	for i in tqdm(response, desc='adding new students to students table', ascii='░▒█'):
		login = f"\'{i['user']['login']}\'"
		cursor = call_query(connection, f"SELECT login FROM exam WHERE login={login}")
		exists = cursor.fetchone()
		if not exists:
			first_name = f"\'{i['user']['first_name']}\'"
			last_name = f"\'{i['user']['last_name']}\'"
			email = f"\'{i['user']['email']}\'"
			insert_student = f"INSERT INTO exam VALUES ({login}, {first_name}, {last_name}, {email}, NULL)"
			call_query(connection, insert_student)
	print('')

def init_script(connection, response):
	add_new_students_to_student(connection, response)
	add_new_students_to_exam(connection, response)