# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    get_labs.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ommohame < ommohame@student.42abudhabi.ae> +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/08/02 04:32:07 by ommohame          #+#    #+#              #
#    Updated: 2022/08/08 19:53:11 by ommohame         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from database import call_query
from my_config import labs
from my_config import rows
from my_config import seats

# def get_labs():
# 	with open ("data/labs.py", "w") as file:
# 		file.write("lab_seats = {\n")
# 		y = 0
# 		for i in labs:
# 			for j in range(rows[y][0], rows[y][1] + 1):
# 				for x in range(seats[0], seats[1] + 1):
# 					file.write(f"\'lab{i}r{j}s{x}\': {{\n\t\'student\': \'\'\n}},\n")
# 			y += 1
# 		file.write("}")