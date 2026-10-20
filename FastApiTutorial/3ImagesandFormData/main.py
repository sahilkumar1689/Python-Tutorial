from fastapi import FastAPI,Request,HTTPException,File,UploadFile,Form
from fastapi.responses import JSONResponse,FileResponse,StreamingResponse
import json;
import uuid
import os;
import uvicorn;
import aiofiles
from typing import List,Dict

app = FastAPI();

# Default endpoint:

@app.get("/")
def default():
    return {"message:":"Server Starts Serving."}

# 1. We can also accept the request body using "Request" class, it is generally used when you don't know the json body format.

@app.post("/random_data")
async def random_data(json_data : Request):
    try:
        # After that you need to parse the request body:
        data = await json_data.json();

        return JSONResponse(status_code=200,content={
            "success":True,
            "data":data
        })
    except Exception as e:
        raise HTTPException(status_code=400,detail={
            "success":False,
            "message":str(e)
        });


# 2. Now we are create an enpoint which can handle single image upload:

# Note = firstly install the "python-multipart" package to accept the form-data.

# File upload Configurations:
UPLOAD_DIR = "uploads/"
ALLOWED_EXTENSIONS = {"image/jpeg", "image/png", "image/webp"}
MAX_FILE_SIZE = 2 * 1024 * 1024  # 2 MB
MAX_FILES = 5
# Ensure upload directory exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/single_image")
# here the "UploadFile" tells that "file" variable contains the file.
# File() = This function tells that file send via formdata and "..." means compulsary or we can also use "none" to make it optional. "alias" is used to set the key name by using which frontend need to send the image.
async def single_image(file:UploadFile = File(...,alias="profile",description="Send your profile pic here.")):
    try:

        # 1. Firstly check the file_format:

        if file.content_type not in ALLOWED_EXTENSIONS:
            raise HTTPException(status_code=400,detail=f"Invalid file type. Allowed: {ALLOWED_EXTENSIONS}");

        # 2. Check the file size:
        file_bytes = await file.read(); # Note = ones you read the file data the file cursor pointing to end , so either you need to use the stored file data or either you need to reset the cursor to read again file. Recommended only read file onces do not play with the file cursor.
        if len(file_bytes) > MAX_FILE_SIZE:
            raise HTTPException(
                status_code=400,
                detail=f"File too large. Max size is {MAX_FILE_SIZE/1024/1024} MB"
            )
        
        # 3. Create unique file name:

        # extract the extension:
        file_extension = os.path.splitext(file.filename)[1];
        # create unique file name. you can also customize this:
        unique_filename = f"{uuid.uuid4().hex}{file_extension}";
        # create file path where we need to store:
        file_path = os.path.join(UPLOAD_DIR,unique_filename);


        # 4. save file:

        # 1. Method 1 good for small files and when only one user send file.
        
        # with open(file_path,"wb") as file:
        #     file.write(file_bytes);

        # 2. Method 2 good for professional sites where multiple user send files.
        
        async with aiofiles.open(file_path,"wb") as file:
            await file.write(file_bytes);
        
        # 3. Methods 3 good when multiple user send files with large file data.I you use this approach then you no need to check the file size above , you can directly doing there:
        # size = 0
        # async with aiofiles.open(file_path, "wb") as f:
        #     while chunk := await file.read(1024 * 1024):  # 1 MB
        #         size += len(chunk)
        #         if size > MAX_FILE_SIZE:
        #             raise HTTPException(
        #                 status_code=400,
        #                 detail=f"File too large. Max size is {MAX_FILE_SIZE/1024/1024} MB"
        #             )
        #         await f.write(chunk)



        # 5. Sending the response:
        return JSONResponse(
            content={
                "success": True,
                "filename": unique_filename
            },
            status_code=201
        )
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e));

# Note = If you send more than one images using different fields in form-data then the procedure remain same , you just need to handle each image individually.


# 3. Now we can handle that situation when in a single field we can have multiple file.

@app.post("/upload_multiple")
async def upload_multiple(files:List[UploadFile]= File(...,description="Upload atmost 5 profile pics.",alias="ProfilePicArr")):
    try:
        # 1. Check the image array size:
        if len(files) > MAX_FILES:
             raise HTTPException(
                status_code=400,
                detail=f"Too many files! Max allowed: {MAX_FILES}"
            )
        
        # 2. Now loop over each file and doing all the necessary checks one by one:

        saved_files={};

        for file in files:

            # 1. Check the file type:
            if file.content_type not in ALLOWED_EXTENSIONS:
                raise HTTPException(status_code=400,detail=f"Invalid file type of {file.filename}. Allowed: {ALLOWED_EXTENSIONS}");

            # 2. check file size:
            file_bytes = await file.read();

            if len(file_bytes) > MAX_FILE_SIZE:
                raise HTTPException(
                    status_code=400,
                    detail=f"File too large of {file.filename}. Max size is {MAX_FILE_SIZE/1024/1024} MB"
                )
        
            # 3. Create unique file name:

            # extract the extension:
            file_extension = os.path.splitext(file.filename)[1];
            # create unique file name. you can also customize this:
            unique_filename = f"{uuid.uuid4().hex}{file_extension}";
            # create file path where we need to store:
            file_path = os.path.join(UPLOAD_DIR,unique_filename);

            # 4. Save file:
            async with aiofiles.open(file_path, "wb") as f:
                await f.write(file_bytes)
            
            saved_files[file.filename] = unique_filename;
            
        # 3. Sending the response:
        return JSONResponse(status_code=200,content={
            "success":True,
            "storedFiles":saved_files
        })

    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e));


# 4.(i) Now we are creating endpoint which serve the file to frontend for download or preview:

@app.get("/download/{filename}")
async def download_file(filename: str):
    # Create file path:
    file_path = os.path.join(UPLOAD_DIR, filename)

    # Check if file exists
    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )

    # Simply serve the file for download:
    return FileResponse(file_path, media_type="application/octet-stream", filename=filename)

    # We can also send for preview not downlaod:
    # return FileResponse(file_path)


# (ii) Now we can create an endpoint which send the large file to frontend with streaming,usefull for large files or videos:

@app.get("/stream/{filename}")
async def stream_file(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    def iterfile():
        with open(file_path, mode="rb") as f:
            while chunk := f.read(1024 * 1024):  # 1MB chunks
                yield chunk

     # detect MIME type
    import mimetypes
    mime_type, _ = mimetypes.guess_type(file_path)
    mime_type = mime_type or "application/octet-stream"

    headers = {
        "Content-Disposition": f'attachment; filename="{filename}"'
    }

    return StreamingResponse(
        iterfile(),
        media_type=mime_type,
        headers=headers
    )

    # return StreamingResponse(iterfile(), media_type="application/octet-stream")


# 5. Now we create one enpoint where we can handle both the files and the text data:

@app.post("/upload-with-json")
async def upload_with_json(
    username: str = Form(...),
    tagsList: str = Form(...),        # list will come as a string
    metadataDict: str = Form(...),    # dict will come as a string
    age:int=Form(...),               # Fastapi auto convert str->int
    salary:float=Form(...),          # Fastapi auto convert str->flaot
    profile_pic: UploadFile = File(...)):

    tags:List[str] = json.loads(tagsList)
    metadict:Dict[str,str] = json.loads(metadataDict)
    data = {
        "username":username,
        "age":age,
        "salary":salary,
        "tagList": tags,
        "metaDict":metadict,
        "fileName":profile_pic.filename
    }
    return JSONResponse(status_code=200,content={
        "success":True,
        "data":data
    })



    



if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8080,reload=True);