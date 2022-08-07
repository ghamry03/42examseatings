# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    my_config.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ommohame < ommohame@student.42abudhabi.ae> +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/08/04 00:44:05 by ommohame          #+#    #+#              #
#    Updated: 2022/08/08 01:33:41 by ommohame         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# the labs for the exam
labs = [1, 2]
# the rows in each lab
rows = [[3, 4], [1 , 2]]
# the seats in each row
seats = [1, 14]
# exam id on the api
exam_id = 10949
# exam get call
get_exam = f"https://api.intra.42.fr/v2/events/{exam_id}/events_users"
# exam type
exam = "cursus"
# exam = "piscine"