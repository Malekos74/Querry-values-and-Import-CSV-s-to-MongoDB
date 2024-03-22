"""
    Python program that helps you to querry data from a specific MongoDB collection.
        
    INPUT:
        - Database name
        - Collection name
        - Time step
    OUTPUT:
        - Querries the P and Q values of the specified time step of the Database and Collection wanted
    
    NB:
        - If the program times out at any point, please check your inputs and try again.
        
"""
from pymongo import MongoClient

# Connect to MongoDB using the inputed connection string. Returns the Client
def connectMongoDB():
    connectionString = input("Input the connection string to the wanted Mongo Client (Press ENTER for the default localhost): ")
    defaultConnectionString = "mongodb://localhost:27017"   
    if connectionString == '':
        client = MongoClient(defaultConnectionString)
    else:
        client = MongoClient(connectionString)
        
    return client

# Give the name of the Database (Must exist). Returns DB
def defineDB(client):
    while True:
        myDB = input('Input the name of the Database you want to querry from: ')
        list_of_databases = client.list_database_names()
    
        if myDB not in list_of_databases :
            print('This Database does not exist!')
        else:
            db = client[myDB]
            break
        
    return db

# Give the name of the collection (Must exist). Returns the collection
def defineCollection(db):
    while True:
        myCollection = input('Input the name of the collection you want to querry from: ');
        list_of_collections = db.list_collection_names()
    
        if myCollection not in list_of_collections :
            print('This collection does not exist!')
        else:
            collection = db[myCollection]
            break
        
    return collection

# Querries from the database based on the input of the user. Returns a list of JSON objects.
def querry(collection):
    while True:
        timeStep = input('Input the time step you want to querry: ')
        myQuery = {'t' : timeStep}
        result = collection.find(myQuery)
    
        # Convert the cursor to a list to check if it's empty
        result_list = list(result)
    
        if not result_list:
            print("Observation for the given time step doesn't exist! Make sure the time step given is right (numbers with decimals should be written with '.')")
        else:
            return result_list
    

# Prints the JSON object returned by the querry in a nice way
# Also returns the values of P and Q as an array
def printResult(result_list):
    for x in result_list:
        [p, q] = [str(x.get("P")), str(x.get("Q"))]

    if p is None:
        p = "NaN"
    if q is None:
        q = "NaN"

    print("\nFor the given time step: ")
    print("The value of P is: " + str(p) + "\nThe value of Q is: " + str(q))
    return [p, q]

        
if __name__ == '__main__':
    myClient = connectMongoDB()
    myDB = defineDB(myClient)
    myCollection = defineCollection(myDB)
    myResultList = querry(myCollection)
    # For presentation purposes
    # print()
    # print(myResultList)
    [p, q] = printResult(myResultList)