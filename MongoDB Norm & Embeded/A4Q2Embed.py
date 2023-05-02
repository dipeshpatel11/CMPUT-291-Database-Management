from pymongo import MongoClient
import argparse

#to get the port number from command input
comm_input = argparse.ArgumentParser()
comm_input.add_argument('port_number', type=int)
argument = comm_input.parse_args()
port_number = argument.port_number


client = MongoClient('localhost', port_number)
db = client["A4dbEmbed"]

query = db.SongwritersRecordings.aggregate([
    {"$unwind": "$recordings"},
    {"$match": {"recordings.recording_id": {"$regex": '^70'}}},
    {"$group": 
        {"_id": '',
         "avg_rhythmicality": {"$avg": "$recordings.rhythmicality"}
        }
    }
    ])    

for q in query:
    print(q)

