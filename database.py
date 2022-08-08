# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    database.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ommohame < ommohame@student.42abudhabi.ae> +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/08/05 02:50:37 by ommohame          #+#    #+#              #
#    Updated: 2022/08/08 18:26:14 by ommohame         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sqlite3
from sqlite3 import Error
from os.path import exists
from os import makedirs
from config import data_directory

# connects to the database
def create_connection(path):
	if (exists(data_directory) == False):
		makedirs(data_directory)
	connection = None
	try:
		connection = sqlite3.connect(path)
		print("Connection to SQLite DB successful")
	except Error as e:
		print(f"database error: error: '{e}' occurred")
	return (connection)

# insert a query to the database
def call_query(connection, query):
	cursor = connection.cursor()
	try:
		cursor.execute(query)
	except Error as e:
		print(f"database: error: '{e}' occurred")
	connection.commit()
	return(cursor)

create_students_table = """
CREATE TABLE IF NOT EXISTS students (
	login INT PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL,
	first_seat TEXT,
	second_seat TEXT,
	third_seat TEXT
);
"""

create_exam_table = """
CREATE TABLE IF NOT EXISTS exam (
	login INT PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL,
	seat TEXT
);
"""

create_seats_table = """
CREATE TABLE IF NOT EXISTS seats (
	seat TEXT PRIMARY KEY,
	student TEXT
);
"""

count_users_for_exam = """
SELECT COUNT(*) FROM exam
"""
