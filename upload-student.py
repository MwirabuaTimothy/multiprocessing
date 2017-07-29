import pymongo
import math
import sys
from datetime import datetime

def calc_student_id(school_number, student_number):
	sum = 0
	for x in range(1000):
		sum += x*x
	return str(school_number)  + str(student_number) + str(sum)

school_number = int(sys.argv[1])
print datetime.now(), 'START PROCESS ', school_number

# obtain a mongo connection
connection = pymongo.MongoClient("localhost", 27017)

# obtain a handle to the database
db = connection.multiprocessing
# create the collection
students = db['students'+str(school_number)] 


# get the school
if db.schools.find({'school_number': school_number}).count() > 0:
	school = db.schools.find_one({'school_number': school_number})

	student_number = school['first_student']
	school_number = school['school_number']
	no_students = school['no_students']

	documents = []

	student_index=1;
	while (student_index < no_students) is True: # Going East...
		student_id = calc_student_id(school_number, student_number)

		document = {
			'number': student_number,
			'name': 'Student' + str(student_number),
			'school_number': school_number,
			'student_index': student_index,
			'student_id': student_id,
		}

		documents.append(document)

		# Insert students in batches
		remainder = no_students - student_index 
		if(len(documents) % 10000 == 0): 
			students.insert_many(documents)
			documents = [] # reempty
		else:
			if(remainder < 10000 and len(documents) % 1000 == 0):
				students.insert_many(documents)
				documents = [] # reempty
			else:
				if(remainder < 1000 and len(documents) % 100 == 0):
					students.insert_many(documents)
					documents = [] # reempty
				else:
					if(remainder < 100 and len(documents) % 10 == 0):
						students.insert_many(documents)
						documents = [] # reempty
					else:
						if(remainder < 10):
							students.insert(document)
							documents = [] # reempty

		student_number += 1;
		student_index += 1;

else:
	print 'no school', school_number

		


print datetime.now(), 'END PROCESS ', school_number