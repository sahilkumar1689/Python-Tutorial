import json;

# Function load data from the file.

def load_Todos()->list:
    try:
        with open("todoData.json",'r') as file:
            data = json.load(file);
        
        return data;
    except:
        return [];


# Function list todos:

def list_Todos(videosArr):
    print("\n");
    print("*"*18);
    if len(videosArr) == 0:
        print("No todo found.");
        print("*"*18);
        return;

    for idx,video in enumerate(videosArr,start=1):
        print(f"{idx}. {video["name"]}, Duration: {video["duration"]}");
    
    print("*"*18);

# Function add one todo:
def add_Todo(videosArr):
    
    name = input("Enter todo Name: ");
    duration = input("Enter todo Duration: ");
    
    videosArr.append({"name":name,"duration":duration});
    
    save_Todos(videosArr);
    

# Function used to update todo:
def update_Todos(videosArr):
    list_Todos(videosArr);
    
    print("\n");
    
    changeIdx = int(input("Enter the videoNumber to update: "));
    updatedName = input("Enter the new name: ");
    updatedDuration = input("Enter the new duration: ");
    
    if changeIdx >=1 and changeIdx <= len(videosArr):
        videosArr[changeIdx-1] = {"name":updatedName,"duration":updatedDuration};       
    
        save_Todos(videosArr);
    else:
        print("\n");
        print("*"*18);
        print("Invalid Video Id.Try Again");
        print("*"*18);

# Function delete one todo:
def delete_Todos(videosArr):
    deleteIdx = int(input("Enter video Number to delete: "));
    
    if deleteIdx >=1 and deleteIdx <= len(videosArr):
        del videosArr[deleteIdx-1];    
    
        save_Todos(videosArr);
    else:
        print("\n");
        print("*"*18);
        print("Invalid Video Id.Try Again");
        print("*"*18);
    

# Function used to save updated data in the file:
def save_Todos(videosArr):
    
    with open("todoData.json",'w') as file:
        json.dump(videosArr,file);
    
    print("\n");
    print("*"*18);
    print("Data Updated successfully.");
    print("*"*18);


def main():
    
    while True:
        
        videos = load_Todos();
        
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
                list_Todos(videos);
            case '2':
                add_Todo(videos);
            case '3':
                update_Todos(videos);
            case '4':
                delete_Todos(videos);
            case '5':
                break;
            case _:
                print("Invalid Option! Try Again.");

    
if __name__ == "__main__":
    main();