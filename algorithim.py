# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    algorithim.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ommohame < ommohame@student.42abudhabi.ae> +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/08/08 01:45:42 by ommohame          #+#    #+#              #
#    Updated: 2022/08/08 23:41:55 by ommohame         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from database import *
from init_script import get_labs
from my_config import *
# from get_labs import get_labs
from tqdm import tqdm
import random

def count_users(connection):
	count = call_query(connection, count_users_for_exam).fetchone()
	return (count[0])

def count_seats():
	rows_count = 0
	for i in rows:
		rows_count += i[1] - i[0] + 1
	seats_per_row = seats[1] - seats[0] + 1
	seats_count = (seats_per_row * rows_count)
	return (seats_count)

def check_user(user, seat, connection):
	seat_1 = call_query(connection, f"SELECT first_seat FROM students WHERE login = '{user}'").fetchone()[0]
	seat_2 = call_query(connection, f"SELECT second_seat FROM students WHERE login = '{user}'").fetchone()[0]
	seat_3 = call_query(connection, f"SELECT third_seat FROM students WHERE login = '{user}'").fetchone()[0]
	if seat_1 != seat and seat_2 != seat and seat_3 != seat:
		call_query(connection, f"UPDATE exam SET seat = '{seat}' WHERE login = '{user}'")
		call_query(connection, f"UPDATE seats SET student = '{user}' WHERE seat = '{seat}'")
		return (1)
	else:
		return (-1)

def	switch_user(user, seat, connection):
	counter = 0
	exam_users = call_query(connection, "SELECT * FROM exam WHERE seat IS NOT NULL").fetchall()
	for old_user in exam_users:
		random.shuffle(exam_users)
		old_seat = old_user[4]
		old_user_seat_1 = call_query(connection, f"SELECT first_seat FROM students WHERE login = '{old_user[0]}'").fetchone()[0]
		old_user_seat_2 = call_query(connection, f"SELECT second_seat FROM students WHERE login = '{old_user[0]}'").fetchone()[0]
		old_user_seat_3 = call_query(connection, f"SELECT third_seat FROM students WHERE login = '{old_user[0]}'").fetchone()[0]
		if seat != old_user_seat_1 and seat != old_user_seat_2 and seat != old_user_seat_3:
			user_seat_1 = call_query(connection, f"SELECT first_seat FROM students WHERE login = '{user}'").fetchone()[0]
			user_seat_2 = call_query(connection, f"SELECT second_seat FROM students WHERE login = '{user}'").fetchone()[0]
			user_seat_3 = call_query(connection, f"SELECT third_seat FROM students WHERE login = '{user}'").fetchone()[0]
			if old_seat != user_seat_1 and old_seat != user_seat_2 and old_seat != user_seat_3:
				call_query(connection, f"UPDATE exam SET seat = '{old_seat}' WHERE login = '{user}'")
				call_query(connection, f"UPDATE exam SET seat = '{seat}' WHERE login = '{old_user[0]}'")
				call_query(connection, f"UPDATE seats SET student = '{user}' WHERE seat = '{old_seat}'")
				call_query(connection, f"UPDATE seats SET student = '{old_user[0]}' WHERE seat = '{seat}'")
				return (1)
		if (counter == 10):
			call_query(connection, f"UPDATE exam SET seat = '{seat}' WHERE login = '{user}'")
			call_query(connection, f"UPDATE seats SET student = '{user}' WHERE seat = '{seat}'")
			return (1)
		counter += 1
	call_query(connection, f"UPDATE exam SET seat = '{seat}' WHERE login = '{user}'")
	call_query(connection, f"UPDATE seats SET student = '{user}' WHERE seat = '{seat}'")
	return (1)

def assign_seats(connection, space):
	exam_users = call_query(connection, "SELECT * FROM exam").fetchall()
	random.shuffle(exam_users)
	for user in tqdm(exam_users, desc='assigning seats', ascii='░▒█'):
		seats = call_query(connection, "SELECT * FROM seats WHERE student IS NULL").fetchall()
		if not seats:
			return
		counter = 0
		seat = random.choice(seats)
		ret = check_user(user[0], seat[0], connection)
		while ret != 1:
			seat = random.choice(seats)
			ret = check_user(user[0], seat[0], connection)
			if counter == 3 and ret != 1:
				ret = switch_user(user[0], seat[0], connection)
				break
			counter += 1
	print('')


def update_students_table(connection, space):
	exam_users = call_query(connection, "SELECT login, seat FROM exam").fetchall()
	for user in tqdm(exam_users, desc='updating the students table', ascii='░▒█'):
		if user[1]:
			user_s = call_query(connection, f"SELECT * FROM students WHERE login = '{user[0]}'").fetchone()
			seat_1 = user_s[4]
			seat_2 = user_s[5]
			seat_3 = user_s[6]
			if not seat_1 and not seat_2 and not seat_3:
				call_query(connection, f"UPDATE students SET first_seat = '{user[1]}' WHERE login = '{user[0]}'")
			elif seat_1 and not seat_2 and not seat_3:
				call_query(connection, f"UPDATE students SET second_seat = '{user[1]}' WHERE login = '{user[0]}'")
			elif seat_1 and seat_2 and not seat_3:
				call_query(connection, f"UPDATE students SET third_seat = '{user[1]}' WHERE login = '{user[0]}'")
			elif seat_1 and seat_2 and seat_3:
				call_query(connection, f"UPDATE students SET first_seat = '{seat_2}' WHERE login = '{user[0]}'")
				call_query(connection, f"UPDATE students SET second_seat = '{seat_3}' WHERE login = '{user[0]}'")
				call_query(connection, f"UPDATE students SET third_seat = '{user[1]}' WHERE login = '{user[0]}'")
	print('')


def algoritim(connection):
	users_count = count_users(connection)
	if users_count == 0:
		print("Zero students subscribed for the exam\nexiting the script")
		exit(0)
	seats_count = count_seats()
	if users_count > seats_count:
		print("No enough seats")
		exit(0)
	space = seats_count // users_count
	if (space <= 0):
		space = 1
	get_labs(connection, space)
	assign_seats(connection, space)
	update_students_table(connection, space)
