import pymongo
import math
import sys
from datetime import datetime

def calc_student_id(school_number, student_number):
	sum = 0
	for x in range(1000):
		sum += x*x
	return str(school_number)  + str(student_number) + str(sum)

school_number = int(sys.argv[1]) || 1
print datetime.now(), 'START PROCESS ', school_number

# obtain a mongo connection
connection = pymongo.MongoClient("localhost", 27017)

# obtain a handle to the database
db = connection.project
# create the collection
students = db['students'+str(school_number)] 


# get the school
school = db.schools.find({'school_number': school_number}).limit(1)


student_number = school['first_student']
school_number = school['school_number']
no_students = school['no_students']

documents = []

school_index=1;
while (school_index < no_students) is True: # Going East...
	student_id = calc_student_id(school_number, student_number)

	document = {
		'number': student_number,
		'name': 'Student' + str(student_number),
		'school_number': school_number,
		'school_index': school_index,
		'student_id': student_id,
	}

	documents.append(document)

	if(student_number % 10000 == 0 ): 
		# todo - try students.batch(...)
		students.insert_many(documents)
		documents = [] # reempty

		print datetime.now().time(), 'school', school_number, student_number

	if(student_number > (math.floor(student_number/10000) *10000)): # the remainder
		
		students.insert(document)
		documents = [] # reempty

	student_number += 1;
	school_index += 1;
	


print datetime.now(), 'END PROCESS ', school_number