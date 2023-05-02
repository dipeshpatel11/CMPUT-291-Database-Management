import pymongo
import argparse
from bson.json_util import loads
from pymongo import MongoClient

#to get the port number from command input
parser = argparse.ArgumentParser()
parser.add_argument('port_number', type=int)
comm_input = parser.parse_args()
port_number = comm_input.port_number

# print(f"Using port number {port_number}")
# print("Mongo version",pymongo.__version__)

# TASK 1

client = MongoClient('localhost',port_number)
db = client["A4dbNorm"]
# opening recordings .json file
read_records = open('recordings.json','r')
recordings = read_records.read()
data_recordings = loads(recordings)

# opening song_writers .json file
read_song = open('songwriters.json','r')
song_writers = read_song.read()
data_writers = loads(song_writers)

#Creating songwriters collection
songwriters_collection = db['songwriters']
songwriters_collection.delete_many({})  # delete documents from songwriters collection if exists

#Creating recordings collection
recordings_collection = db['recordings']
recordings_collection.delete_many({})   # delete documents from recordings collection if exists

for row in data_recordings:
    recordings_collection.insert_one(row)  # inserting document to recordings collection

for col in data_writers:
    songwriters_collection.insert_one(col)   # inserting document to songwriters collection
    
#cursor = recordings_collection.find({})
#for document in cursor:
    #print(document)
    
# cursor1 = songwriters_collection.find({})
# for documents in cursor1:
#     print(documents)    

client.close()

