import pymongo
import subprocess
import math

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


# Number of schools
no_schools = schools.count(); 
no_schools = 10; 

def runProcess(school_number): 
  subprocess.call(['python', 'upload-student.py', str(school_number)])


if __name__ == '__main__':
  p = Pool()
  for school_number in xrange(1, no_schools+1):
    p.apply_async(runProcess, args=(school_number,))
  p.close()
  p.join()


end = datetime.now();
print end.time(), '--------------------- ENDED PROCESSING ---------------------'
print (end - start).total_seconds(), 's'