from  pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://<username>:<password>@cluster0.fq0w9rc.mongodb.net/", tlsAllowInvalidCertificates = True)  # not a good idea to include id and password in code files

print(client)
db = client["ytdatabase"]

videos_collection = db["videos"]

print(videos_collection)

def list_videos():
    for video in videos_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")

def add_video(name, time):
    videos_collection.insert_one({"name": name, "time": time}) #we have to pass it as object

def update_video(video_id, new_name, new_time):
    videos_collection.update_one(
        {"_id": ObjectId(video_id)}, 
        {"$set": {"name": new_name, "time": new_time}})    
  
def delete_video(video_id):
    videos_collection.delete_one({"_id": ObjectId(video_id)})

        
def main():
    while True:
        print("\n Youtube manager App")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_videos()
        elif choice == "2":     
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)   
        elif choice == "3":
             video_id = input("Enter video ID to update: ")
             new_name = input("Enter new video name: ")     
             new_time = input("Enter new video time: ")   
             update_video(video_id, new_name, new_time)
        elif choice == "4":
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id, name, time)
        elif choice == "5":
            print("Exiting the app.")
            break
        else:
            print("Invalid choice. Please try again.")    



if __name__ == "__main__":
    main()