import pymongo
import subprocess
import math

from multiprocessing import Process

from datetime import datetime
start = datetime.now();

print start.time(), '--------------------- STARTED PROCESSING ---------------------'


# obtain a mongo connection
connection = pymongo.MongoClient("localhost", 27017)

# obtain a handle to the project database
db = connection.multiprocessing_example
# get the collection
schools = db.schools 

# Number of schools
no_schools = schools.count(); 
# no_schools = 2; 


def runProcess(school_number): 
  subprocess.call(['python', 'upload-student.py', str(school_number)])


processes = []

for m in range(0,no_schools):
  school_number = m + 1
  p = Process(target=runProcess, args=(str(school_number),))
  p.start()
  processes.append(p)

for p in processes:
   p.join()


end = datetime.now();
print end.time(), '--------------------- ENDED PROCESSING ---------------------'
print (end - start).total_seconds(), 's'