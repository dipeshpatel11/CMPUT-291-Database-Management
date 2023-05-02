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


#TASK-2

client = MongoClient('localhost',port_number)

db = client["A4dbEmbed"] 

#recordings
read_records = open('recordings.json','r')
recordings = read_records.read()
data_recordings = loads(recordings)

#song_writers
read_song = open('songwriters.json','r')
song_writers = read_song.read()
data_writers = loads(song_writers)

rec_collection = {}   # creating dictonary for recording collection 

for document in data_recordings:
    recording_ids = document["recording_id"]
    rec_collection[recording_ids] = document # assign key value to recording collection.
    
for writer in data_writers:
    writers_recording = writer["recordings"]    # all the song_writers for each recording.
    #print(writers_recording)
        
    for i in range(len(writers_recording)):
        recording = rec_collection[writers_recording[i]]
        writers_recording[i] = recording
        #print(writers_recording)    

recordings_collection = db['SongwritersRecordings']
recordings_collection.delete_many({})   # delete documents from recordings collection if exists
one_collection = recordings_collection.insert_many(data_writers)

# db_all_data = db.SongwritersRecordings.find()

# for i in db_all_data:
#     print(i)

client.close()



  


