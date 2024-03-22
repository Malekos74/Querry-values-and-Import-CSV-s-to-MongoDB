# Querry values and Import CSV's to a MongoDB instance
## 1.Import CSV
### Description:
Python program that helps you to import a .csv file into a fresh or pre-existing Mongo DB
### Input
  - Mongo Client connection string (Default: mongodb://localhost:27017)
  - Database name
  - Collection name
  - csv file path
  - number of rows to import (Default: All rows)
### Output
  - Edits/ Creates a database with the specified name, creates a collection with the specified name
    and imports the specified number of rows of the csv file
### Notes
  - If the program times out at any point, please check your inputs and try again.

## 2.Querry
### Description:
Python program that helps you to querry data from a specific MongoDB collection.
### Input:
  - Database name
  - Collection name
  - Time step
### Output:
  - Querries the P and Q values of the specified time step of the Database and Collection wanted
### Notes
  - If the program times out at any point, please check your inputs and try again.
