from pymongo import MongoClient
from pymongo_get_database import get_database
dbname = get_database()
collection_name = dbname["user_1_items"]

def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://mnguyen:Ntmntm1019@cluster0.ybulhme.mongodb.net/"
 
    client = MongoClient(CONNECTION_STRING)

    return client['user_shopping_list']
  
if __name__ == "__main__":   
  
    dbname = get_database()