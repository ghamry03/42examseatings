# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    get_data.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ommohame < ommohame@student.42abudhabi.ae> +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/08/02 01:46:31 by ommohame          #+#    #+#              #
#    Updated: 2022/08/08 01:28:15 by ommohame         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests
import json
from pstats import Stats
from urllib import response
from api.intra import ic
from my_config import get_exam
from database import call_query
from tqdm import tqdm

def get_api():
	ic.progress_bar=True
	response = ic.pages_threaded(get_exam)
	print();
	return (response)
