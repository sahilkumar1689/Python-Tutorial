from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Access a specific database or they create a new:
db = client["TodoDatabase"]

# Access a collection or they create it new.You can also create more than one collection in one database.After that using that collection object you can execute all standard mongodb methods.
collection = db["TodoCollections"]


# Function list todos:

def list_Todos():
    try:
        # Fetch data from the table:
        
        print("\n");
        print("*"*18);
        
        # After that we fetch all the data from the documents:
        videosArr = list(collection.find());  # Collection.find() by default return an cursor object so you need to convert it into list.
        print(list(videosArr));
        if len(videosArr) == 0:
            print("No todo found.");
            print("*"*18);
            return False;
        
        # for video in videosArr:
        for idx,video in enumerate(videosArr,start=1):
            print(f"{idx}. {video["videoName"]}, Duration: {video["duration"]}, videoId = {video["videoId"]}");
            
            
        print("*"*18);
        return True;
    except Exception as e:
        print(f"Error is: {e}");
        exit();

videoCount = 0;

# Function add one todo:
def add_Todo():
    
    name = input("Enter todo Name: ");
    duration = input("Enter todo Duration: ");
    
    # Here we deal with the global variable:
    # global videoCount;
    # videoCount += 1;
    globals()["videoCount"] += 1;
    
    try:
    
        # Function to add todo in the table:
        result = collection.insert_one({"videoName":name,"duration":duration,"videoId":globals()["videoCount"]});

        print(dir(result));
        # If successful, `inserted_id` will not be None:
        if result.inserted_id:
            print("\n" + "*" * 18)
            print(f"✅ Document inserted successfully with _id: {result.inserted_id}")
            print("*" * 18)
        else:
            print("⚠️ Insert failed!")
        
    except Exception as e:
        print(f"Error is: {e}");
        exit();
        
    

def update_Todos():
    if list_Todos() != True:
        return
    
    print("\n")
    
    try:
        changeIdx = int(input("Enter the videoId to update: "))
        updatedName = input("Enter the new name: ")
        updatedDuration = input("Enter the new duration: ")

        result = collection.update_one(
        {"videoId": changeIdx},                                          # filter
        {"$set": {"videoName":updatedName,"duration": updatedDuration}}  # update operation
        )
        
        print(dir(result));
        # check how many data were updated
        if result.modified_count == 0:
            print("\n" + "*" * 18)
            print("Invalid Video Id. Try Again")
            print("*" * 18)
        else:
            print("\nVideo updated successfully!")
            
    except Exception as e:
        print(f"⚠️ Error while updating: {e}")
        exit();


# Function delete one todo:
def delete_Todos():
    if list_Todos() != True:
        return
    
    print("\n")
    try:
        
        deleteIdx = int(input("Enter video Id to delete: "));
        
        # Function to delete the video from the table:
        
        result = collection.delete_one({"videoId":deleteIdx});
        
        print(dir(result));
        
        if result.deleted_count > 0:
            print("\n✅ Document deleted successfully")
        else:
            print("\n" + "*" * 18);
            print("❌ No matching document found")
            print("*" * 18)
        
        
    except Exception as e:
        print(f"⚠️ Error while updating: {e}")
        exit();
        


def main():
    
    while True:
        
        # print("Videos data: ",videos);
        print("\n");
        print("******** Todo Manager ********");
        print("Enter 1 for list all todo's.");
        print("Enter 2 for add new todo.");
        print("Enter 3 for update todo.");
        print("Enter 4 for delete todo.");
        print("Enter 5 exit.");
        
        choice = input("Please enter your choice: ");
        
        match choice:
            case '1':
                list_Todos();
            case '2':
                add_Todo();
            case '3':
                update_Todos();
            case '4':
                delete_Todos();
            case '5':
                break;
            case _:
                print("\n" + "*" * 18)
                print("Invalid Option! Try Again.");
                print("*" * 18)

    
if __name__ == "__main__":
    main();