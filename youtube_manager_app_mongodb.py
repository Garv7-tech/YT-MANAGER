import dotenv
import pymongo
import os
import bson

# Load environment variables from .env file
dotenv.load_dotenv()

# Get the MongoDB URI and database name from environment variables

uri=os.getenv('MONGODB_URI')
db_name=os.getenv('DB_NAME')

# Connect to MongoDB
client = pymongo.MongoClient(uri)
db=client[db_name]

video_collection=db['videos']

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name:{video['name']} and Time: {video['time']}")

def add_video(name,time):
    video_collection.insert_one({'name':name, 'time':time}) 

def update_video(video_id, new_name, new_time):
    video_collection.update_one({'_id':bson.ObjectId(video_id)},{'$set':{'name':new_name, 'time':new_time}})

def delete_video(video_id):
    video_collection.delete_one({'_id':bson.ObjectId(video_id)})



def main():
    while True:
        print("\n Youtube manager App")
        print("1. List all videos")
        print("2. Add a new videos")
        print("3. Update a videos")
        print("4. Delete a videos")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the video id to update: ")
            name = input("Enter the updated video name: ")
            time = input("Enter the updated video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the video id to update: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice")


if __name__=="__main__":
    main()