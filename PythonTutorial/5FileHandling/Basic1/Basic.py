# File handling = In python it is mechanism by using which we can easily do CRUD operation on the files.

# 1. open(fileName,accessMode,buffer) = This method is used to open the file in various mode.

# Various Mode:
# 1. r = reading mode, r+ = read and write mode.
# 2. w = write mode and create if not exists, w+ = read and write mode create if not exists.
# 3. a = append mode and create if not exists, a+ = append and read mode create if not exists.

# Various methods:
# 1. close() = After performing the operation it is important to close the file.
# 2. read() = 
# 3. readline() = 
# 4. readlines() =
# 5. write() = 
# 6. writelines() = 

# e.g. :

# # 1. Wrinting in the file:
# list1 = ["\nthis is first line","\nthis is second line","\nthis is third line"];
# file1 = open("temp1.txt",'a+');
# file1.write("Hello World!");
# file1.writelines(list1);
# file1.close();

# # 2. Reading from the file:
# file2= open("temp1.txt",'r');

# print("Read: ",file2.read());
# file2.close();


# file3= open("temp1.txt",'r');
# print("Readline1: ",file3.readline());
# print("Readline2: ",file3.readline());

# lineArr = file3.readlines();

# for line in lineArr:
#     print(line);

# file3.close();


# 2. with keyword = It automatically close the file.It is also called context manager.

# e.g.:

# with open("temp1.txt",'r') as file:
#     lineArr = file.readlines();
#     for line in lineArr:
#         print(line);

# 3. Reading json files = In order to read the json file you firstly need to import the json module.

# Methods in json:

# 1. json.load(f) = Read JSON from a file and convert to Python object
# 2. json.loads(s)	= Read JSON from a string and convert to Python object
# 3. json.dump(obj, f) = Write Python object as JSON into a file
# 4. json.dumps(obj) = Convert Python object to JSON string

# 4. While working with the documents and pdf you can use the docx and the pyPDF packages in order to read the text from them.
 
#  5. If you don't  wanna to use the docx and pyPDF packages even though you can also easily deal with them by using the "wb" or "rb" modes.