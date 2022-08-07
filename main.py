# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ommohame < ommohame@student.42abudhabi.ae> +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/07/29 04:35:26 by ommohame          #+#    #+#              #
#    Updated: 2022/08/08 01:33:55 by ommohame         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# connects to the SQLite database
# creates student table if it doesn't exist
# deletes previous exam table and creates the new one
from database import *
from my_config import exam
connection = create_connection(f"data/{exam}.db")
call_query(connection, create_students_table)
call_query(connection, "DROP TABLE IF EXISTS exam")
call_query(connection, create_exam_table)

# gets the data from the api and saves them into a variable
from get_data import get_api
response = get_api()

# inits the script when it starts
# if there's new students it's gonna add them to the student table in the daatabase
# add exam students to student table
from init_script import init_script
init_script(connection, response)

# gets a list of the labs for the exam
from get_labs import get_labs
get_labs()



connection.close()