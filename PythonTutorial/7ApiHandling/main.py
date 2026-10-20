import requests;

# 1. Get requests:

# try:
#     headers = {'active':"aplication/json"};

#     url = "https://api.freeapi.app/api/v1/public/randomusers/user/random";

#     response = requests.get(url,headers=headers);
#     res = response.json();  # it is used to convert the response in the json object.
#     # response.url          # return the requested url.
#     # response.text         # it is used to convert the reposne into string/unicode.
#     # response.status_code  # return the status code.
#     # response.request      # return the requested object.

#     if res["success"] and res["data"]:
#         print("Message is: ",res["message"]);
#         print("Success is: ",res["success"]);
#         print("Status Code is: ",res["statusCode"]);
#         print("Data is: ",res["data"]);
#         print("Complete resposne object is: ",res);
#     else:
#         print("Something Went wrong.");
# except Exception as e:
#     print(f"Error is: {e}");

# 2. Post request:

# data= {
#     'title': 'foo',
#     'body': 'bar',
#     'userId': 1,
#   }

# headers = {'Authorization': 'Bearer YOUR_TOKEN'}  # you can also send the bearer token in authorization header.

# url = "https://jsonplaceholder.typicode.com/posts";
# try:
#     response = requests.post(url,json=data); # if you wanna to send the data in json format you need to use "json=" they internally convert into the json and send.

#     res = response.json();
#     print(response.status_code);
    
#     if response.status_code == 201:
#         print("data is: ",res);
#     else:
#         print("Something went wrong.");
# except Exception as e:
#     print(f"Error is: {e}");
    

# 3. You can also send files using the like images/photos :

# files = {'file': open('example.png', 'rb')}
# response = requests.post('https://api.example.com/upload', files=files)
# print(response.status_code)
    











