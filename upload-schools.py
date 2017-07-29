import pymongo
from random import randint
from multiprocessing import Pool
from datetime import datetime

start = datetime.now();
print start.time(), '--------------------- STARTED PROCESSING ---------------------'

# obtain a mongo connection
connection = pymongo.MongoClient("localhost", 27017)

# obtain a handle to the project database
db = connection.multiprocessing
# get the collection
schools = db.schools 


def uploadSchool(school_number):
	document = {
		'school_number': school_number,
		'name': 'School ' + str(school_number),
		'no_students': randint(5000, 10000),
		'first_student': school_number,
	}
	schools.insert(document)

if __name__ == '__main__':
	p = Pool()
	# 'map' - the process of dividing the input between multipe cores
	# 'reduce' - the process of aggregating results
	result = p.map(uploadSchool, range(1, 200001)) # does both mapping and reducing
	p.close()
	p.join()
	

end = datetime.now();
print end.time(), '--------------------- ENDED PROCESSING ---------------------'

print (end - start).total_seconds(), 's'

	