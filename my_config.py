# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    my_config.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ommohame < ommohame@student.42abudhabi.ae> +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/08/04 00:44:05 by ommohame          #+#    #+#              #
#    Updated: 2022/08/08 23:39:40 by ommohame         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# the labs for the exam
labs = [1]

# the rows in each lab
rows = [[1, 3]]

# the seats in each row
seats = [1, 20]

# exam id on the api
exam_id = 10949

# exam get call
get_exam = f"https://api.intra.42.fr/v2/events/{exam_id}/events_users"

# exam type
exam = "cursus"
# exam = "piscine"

# email settings
email_host = 'smtp.mail.me.com'
email_port = 587
email_id = 'omarelghamry@icloud.com'
email_pass = 'bpye-ylwg-aqmq-fokt'
