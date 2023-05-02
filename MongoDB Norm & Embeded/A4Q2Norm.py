from pymongo import MongoClient
import argparse

comm_input = argparse.ArgumentParser()
comm_input.add_argument('port_number', type=int)
argument = comm_input.parse_args()
port_number = argument.port_number


client = MongoClient('localhost', port_number)
db = client["A4dbNorm"]

query = db.recordings.aggregate([
    {"$match": {"recording_id": {"$regex": '^70'}}},
    {"$group": 
        {"_id": '',
         "avg_rhythmicality": {"$avg": "$rhythmicality"}
         }
    }
    ])    

for q in query:
    print(q)
    
