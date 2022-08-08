# <div align="center"> 42examseatings </div>
## <div align="center"> my submission for the first 42 Abu Dhabi coding challenge </div>

### First time installition:
To run the script you need to make sure that u have the used packages
you can run this command to install every package:

      pip3 install -r requirements.txt

Then you need to update your api credentials in config.yml in api directory:
- client: "UID"
- secret: "SECRET"

### To run the script you need to modify my_config.py file:
- labs = [lab1, lab2, ...] -> the labs for the exam
- rows = [[first seat in lab1, last seat in lab1], [first seat in lab2, last seat in lab2], ..]
- seats = [seats in each row for all the labs]
- exam_id = exam ID from the api
- get_exam = it uses the exam_id to call the data from the api
- exam = "cursus / piscine" -> it definies which data to use
- email_host = "email server host"
- email_port = "server port"
- email_id = "the full email here"
- email_pass = "the email password"

then you can run the script
it will ask you if you want to send emails to students or not
you can check the seats in seats.txt or from the data before sending emails.

### Algorithim behind the script:
 - it checks for student who registered for the exam then save them in the database
 - then starts to assigning seats and compare it to student last 3 exam seats
    - if it's a new seat it gives it to the student
    - else it tries different seats for 3 times
    - if it fails again it tries to swap the seat with other students with a seat for 10 times
    - if it fails after 10 times it just gives the student the seat
- the reason behind the simple algorithim is time complexity, as the seats really won't matter, as we trust our beloved students.

### To Do list:
- update the examshell where it does a quick checksum to check the user seat
- update the email format with designs given by 42 Abu Dhabi
- set algo_complex var in my_config.py to change the algorithm complexity

### credits
- big thanks to hivehelsinki for the beautiful 42api-lib
- also big thanks to 42 Abu Dhabi for this amazing challenge which pushed me out of my comfort zone and gave me a chance to learn new stuff for the first time like python which I will definitely use it more to do some fun stuff, how to deal with api and databases (sqlite) which was really fun and I will try to use it on side projects.
