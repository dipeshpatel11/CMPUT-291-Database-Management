from pymongo import MongoClient
import datetime
import argparse

comm_input = argparse.ArgumentParser()
comm_input.add_argument('port_number', type=int)
argument = comm_input.parse_args()
port_number = argument.port_number


client = MongoClient('localhost', port_number)
db = client["A4dbEmbed"]

query = db.SongwritersRecordings.aggregate([

    {'$unwind': '$recordings'},
    {'$match': {
        "recordings.issue_date": {"$gt": datetime.datetime(1950, 1, 1)}
    }},
    {"$project": {
        "_id": "$_id",
        "name": "$name",
        "r_name": "$recordings.name",
        "r_issue_date": "$recordings.issue_date"
    }}
])


for q in query:
    print(q)
