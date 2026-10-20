# 1. List = It is a linear data structure which is used to store the different datatypes in a contigous memory location.It is mutable.
# Syntax:
# variableName = [elem1,elem2,elem3,...];

# list1 = ["akshay",23,1,2,3];

# print(list1[0]);
# print(list1[1]);
# print(list1[2]);
# print(list1);

# Some of the method of the list:

# 1. list.append(value) = Add at the end of the list.
# 2. list.insert(idx,value) = Insert value at specific index.
# 3. list1.extend(list2) = Basically concat two list. Also do with "+" operator.
# 4. list.pop(idx) = Remove specific idx value and return that value.
# 5. list.remove(value) = Simple remove specific value.
# 6. list.clear() = Empty list.
# 7. list.index(value) = Return the index of first occurance of particular value.
# 8. list.count(value) = Return the count of occurance of element.
# 9. list.sort() and list.reverse()
# 10. list.copy() = used to create the deep copy of the list.




# 2. Tuples = It is a linear data structure which is used to store the multiple data types.It is immutable.All thought tuple is immutable but if it contains any mutable element then we can easily do changes in that elements.
# Syntax:
# variableName = (elem1,elem2,elem3,...);

# tup = ("akshay",23,1,2,3);

# print(tup[0]);
# print(tup[1]);
# print(tup[2]);
# print(tup);

# Tuple only have two methods:

# 1. tp.count(value) = Count the occurance od the sepecific element.
# 2. tp.index(value,afterIdx) = Return the index of the specific value.It also contain one optional idx argument that used to starting point.




# 3. Array = Althought in python we does not have array as a built in data type but we can use arrays in python by simply importing them.Array is a linear data structure which is used to store the same data types only.Also mutable.

# import array;

# syntax:
# variableName = array(type,listOfElements);

# arr1 = array.array('i',[1,2,3,4,5]);

# Note = 1. i = for int , f = for float , d = for double , u = for character.
# 2. It cannot store the strings.
# 3. Array supports all the methods of lists.




# 4. String = A sequence of character are called string.It is immutable data type in python.

# Syntax:
# variableName = "...";

# Some of the methods of the strings are:

# 1. str.lower(), str.upper() , str.title() = Capitalize the first character of each word , str.Capitalize(),str.swapcase().
# 2. str.find(elem) , str.index(elem) , str.count(elem), str.startswith(elem) , str.endswith(elem).
# 3. str.replace(old,new) ,str.strip() = remove whitespaces from both side, str.lstrip() = remove space from left side only,str.rstrip() = remove whitespace from right side only, str.removeprefix(value),str.removesuffix(value).
# 4. str.split(value) , value.join(list)
# 5. str.isalnum() = Is all letter and numbers only, str.isdigit(),str.alpha(),str.islower(),str.isupper().




# 5. Dictionary = It is a unordered data structure in python which is used to store the data in key value pair format.It is mutable.It only contains the unique value.Only immutable data types can be used as key for dictionary.

# Syntax:
# variableName = {key:value,...};

# stdDetails = {
#     "name":"Akshay",
#     "age":23
# }

# # Change value easily:
# stdDetails["age"] = 24;

# # Add new value easily:
# stdDetails["roll"] = 1;

# # Access Value easily:
# print(stdDetails["name"]);
# print(stdDetails["age"]);
# print(stdDetails["roll"]);


# Some of the methods of the dictionary are:

# 1. dict.get(key,failureMessage) = Used to return the value for specific key.
# 2. dict.keys() = Return the list of keys.
# 3. dict.value() = Return the list of values.
# 4. dict.clear() = empty all the dictionary.
# 5. dict.pop(key) = Used to delete specific element from the dictionary.
# 6. dict1.update(dict2) = Used to merge two dictionary into one.
# 7. dict.popitem() = delete the last inserted items and also return them.




# 6. Set = It is a mutable and unordered data types which is used to store the unique but mixed data.

# Syntax:
# varaibleName = {elem1,elem2,...};

# Some of the method of the sets:

# 1. st.add(value),st.discard(value) = not thorown error if not present,st.remove(value),st.clear()
# 2. st.pop() = used to remove any random element from the array.
# 3. st1.update(st2) = Merge two sets.
# 4. st1.union(st2),st1.interection(st2),st1.difference(st2)















