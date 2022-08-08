# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    my_config.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ommohame < ommohame@student.42abudhabi.ae> +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/08/04 00:44:05 by ommohame          #+#    #+#              #
#    Updated: 2022/08/08 23:46:25 by ommohame         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# the labs for the exam
labs = [1]

# the rows in each lab
rows = [[1, 4]]

# the seats in each row
seats = [1, 14]

# exam id on the api
exam_id = 10949

# exam get call
get_exam = f"https://api.intra.42.fr/v2/exams/{exam_id}/exams_users"

# exam type
exam = "cursus"
# exam = "piscine"

# email settings
email_host = ''
email_port = 587
email_id = ''
email_pass = ''
