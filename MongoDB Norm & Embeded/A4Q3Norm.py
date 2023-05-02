from pymongo import MongoClient
import sys
import argparse

comm_input = argparse.ArgumentParser()
comm_input.add_argument('port_number', type=int)
argument = comm_input.parse_args()
port_number = argument.port_number


client = MongoClient('localhost', port_number)

db = client["A4dbNorm"]


query = db.songwriters.aggregate([
    {'$lookup': {
        'from': 'recordings',
        'localField': 'recordings',
        'foreignField': 'recording_id',
        'as': 'recordings'
    }},
    {"$unwind": "$recordings"},
    {"$group": {
        "_id": "$songwriter_id",
        "total_length": {"$sum": "$recordings.length"}
    }},
    {"$addFields": {"songwriter_id": "$_id"}}
])

for q in query:
    print(q)