# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    init_script.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ommohame < ommohame@student.42abudhabi.ae> +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/08/04 02:38:39 by ommohame          #+#    #+#              #
#    Updated: 2022/08/08 20:31:49 by ommohame         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from re import S
from api.intra import ic
from my_config import get_exam
from os.path import exists
from database import call_query
from tqdm import tqdm
from my_config import *
import random

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
	for i in tqdm(response, desc='adding new students to exam table', ascii='░▒█'):
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

def get_labs(connection, space):
	y = 0
	for i in tqdm(labs, desc='adding seats to seats table', ascii='░▒█'):
		for j in range(rows[y][0], rows[y][1] + 1):
			starting_seat = random.randint(seats[0] - 1, seats[0] + 1)
			if starting_seat == 0:
				starting_seat = 1
			for x in range(starting_seat, seats[1] + 1, space):
				lab = f"'lab{i}r{j}s{x}'"
				call_query(connection, f"INSERT INTO seats VALUES ({lab}, NULL)")
		y += 1
	print('')

def init_script(connection, response):
	add_new_students_to_student(connection, response)
	add_new_students_to_exam(connection, response)
	