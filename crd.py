from pymongo import MongoClient

# creating connection for communicating with Mongo DB
client = MongoClient('localhost:27017')
db = client.EmployeeData

def main():

    while(1):
	# chossing option to do CRUD operations
        selection = raw_input('\nSelect 1 to insert, 2 to read, 3 to delete\n')
    
        if selection == '1':
	    insert()
    	elif selection == '2':
	    read()
    	elif selection == '3':
	    print 'delete'
	    delete()
    	else:
	    print '\n INVALID SELECTION \n'


# Function to insert data into mongo db
def insert():
    try:
	employeeId = raw_input('Enter Employee id :')
	employeeName = raw_input('Enter Name :')
	employeeAge = raw_input('Enter age :')
	employeeCity = raw_input('Enter City :')
     
        db.Employees.insert_many ( [
             {
                "Id": 1,
                "name": "John" ,
                "age": 18,
                "city": "New York"
             },
             {
                "Id": 2,
                "name": "Jane" ,
                "age": 20,
                "city: "Seoul"
             },
             {
                "Id": 3,
                "name": "Emily" ,
                "age": 23,
                "city: "Tokyo"
             }
        ] )
        print '\nInserted data successfully\n'
	
    except Exception, e:
        print str(e)
	

# function to read records from mongo db
def read():
    try:
	empCol = db.Employees.find()
	print '\n All data from EmployeeData Database \n'
	for emp in empCol:
	    print emp

    except Exception, e:
	print str(e)

# Function to delete record from mongo db
def delete():
    try:
	criteria = raw_input('\nEnter employee id to delete\n')
        db.Employees.delete_many({"id":criteria})
	print '\nDeletion successful\n'	
    except Exception, e:
	print str(e)

main()
