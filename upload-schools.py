import pymongo
from random import randint

from multiprocessing import Pool
from multiprocessing import cpu_count

from datetime import datetime
start = datetime.now();

print start.time(), '--------------------- STARTED PROCESSING ---------------------'

# obtain a mongo connection
connection = pymongo.MongoClient("localhost", 27017)

# obtain a handle to the project database
db = connection.project
# get the collection
schools = db.schools 



school_number=1;
while (school_number <= 200000) is True:
  
	document = {
		'school_number': school_number,
		'name': 'School ' + str(school_number),
		'no_students': randint(1000, 10000),
		'first_student': school_number,
	}

	schools.insert(document)
	school_number += 1

end = datetime.now();
print end.time(), '--------------------- ENDED PROCESSING ---------------------'
print (end - start).total_seconds(), 's'