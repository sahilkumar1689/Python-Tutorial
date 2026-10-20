
import sqlite3;

# Creating connetion from the sqlite database:
conn = sqlite3.connect("todo.db");  # This command will create the new database if not exists other wise use existing.
cur = conn.cursor();   # Now that cursor object us used for all tasks.

# Creating todo table:

cur.execute("""
    CREATE TABLE IF NOT EXISTS todoTable(
        videoId INTEGER PRIMARY KEY AUTOINCREMENT,
        videoName TEXT NOT NULL,
        duration TEXT NOT NULL
    )
""");


# Function list todos:

def list_Todos():
    try:
        # Fetch data from the table:
        cur.execute("Select * from todoTable;");
        print("\n");
        print("*"*18);
        
        # After that we fetch all the row of data from the table:
        videosArr = cur.fetchall();
        
        if len(videosArr) == 0:
            print("No todo found.");
            print("*"*18);
            return False;

        for video in videosArr:
            print(f"{video[0]}. {video[1]}, Duration: {video[2]}");
        
        print("*"*18);
        return True;
    except Exception as e:
        print(f"Error is: {e}");
        exit();

# Function add one todo:
def add_Todo():
    
    name = input("Enter todo Name: ");
    duration = input("Enter todo Duration: ");
    
    try:
    
        # Query to add todo in the table:
        cur.execute("INSERT INTO todoTable (videoName,duration) values (?,?)",(name,duration));
        conn.commit();  # You need to commit in order to show changes in the main table:
        
        # check how many rows were updated
        if cur.rowcount == 0:
            print("\n" + "*" * 18)
            print("Some Error Occurs,Try Again");
            print("*" * 18)
        else:
            print("\nVideo Added successfully!")
    except Exception as e:
        print(f"Error is: {e}");
        exit();
        
    

def update_Todos():
    if list_Todos() != True:
        return
    
    print("\n")
    
    try:
        changeIdx = int(input("Enter the videoNumber to update: "))
        updatedName = input("Enter the new name: ")
        updatedDuration = input("Enter the new duration: ")

        # Query to update in the table:
        cur.execute(
            "UPDATE todoTable SET videoName = ?, duration = ? WHERE videoId = ?",
            (updatedName, updatedDuration, changeIdx)
        )
        conn.commit()

        # check how many rows were updated
        if cur.rowcount == 0:
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
        
        deleteIdx = int(input("Enter video Number to delete: "));
        
        # Query to delete the video from the table:
        
        cur.execute("Delete from todoTable where videoId = ?",(deleteIdx,)) # It very important to not that if you have only one value then it complusary to add a "," at the end. 
       
        if cur.rowcount == 0:
            print("\n" + "*" * 18)
            print("Invalid Video Id. Nothing deleted.")
            print("*" * 18)
        else:
            print("\nVideo deleted successfully!")
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
    

# Note = This is the basic CRUD operation using sqlite , if you wanna to go for advanced usage you can refer the gfg documentation or sqlite3.html documentation.