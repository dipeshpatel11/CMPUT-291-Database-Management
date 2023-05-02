from pymongo import MongoClient
import argparse

#to get the port number from command input
comm_input = argparse.ArgumentParser()
comm_input.add_argument('port_number', type=int)
argument = comm_input.parse_args()
port_number = argument.port_number


client = MongoClient('localhost', port_number)

db = client["A4dbEmbed"]

result = db.SongwritersRecordings.aggregate([

    {"$project": 
        {"_id": 1,
         "songwriter_id": 1,
         "name": 1,
        "num_recordings" : {'$size': "$recordings"},
        }
    },
    {
        "$match": 
            {"num_recordings": {"$gt":0}}
    }
])

for i in result:
    print(i)
    