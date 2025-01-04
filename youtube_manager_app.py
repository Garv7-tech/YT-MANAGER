import json

def load_data():
    try:
        with open('youtube_manager.txt','r') as file:
            test=json.load(file) #reads and converts all the file data into json format
            return test
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube_manager.txt','w') as file:
        json.dump(videos,file) #save videos to file
        #json.dump(): 1st parameter -> what is to be written, 2nd parameter -> where the what is to be written
        
def list_all_videos(videos):
    print('\n')
    print("*"*70)
    for index,video in enumerate(videos,start=1):
        print(f"{index}, {video['name']}, Duration: {video['time']}")
    print('\n')
    print("*"*70)

def add_video(videos):
    name=input("Enter video name: ")
    time=input("Enter video time: ")
    videos.append({'name':name, 'time':time})
    save_data_helper(videos)

def update_video(videos):
   list_all_videos(videos)
   index=int(input("Enter the index of the video"))
   
   if 1<=index<=len(videos):
       updated_name=input("Enter video name: ")
       updated_time=input("Enter video time: ")
       videos[index-1]={'name':updated_name,'time':updated_time}
       save_data_helper(videos)

   else:
       print("Invalid video index selected")

def delete_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the index of the video"))
   
    if 1<=index<=len(videos):
        del videos[index-1] #in-place modification
        save_data_helper(videos)
    else:
        print("Invalid video index selected")

   

def main():
    videos=load_data()

    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__== "__main__":
    main()
