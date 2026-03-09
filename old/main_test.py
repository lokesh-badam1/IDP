# import os
# import uuid
# import json


# import shutil
# from fastapi import FastAPI,UploadFile
# from services.pipeline_services import pipeline
# from routers import api


# app = FastAPI()
# app.include_router(api.router)
# # upload_dir = "uploads"

# @app.get("/")
# def home():
#     return {"hello": "World!"}


# # response_model=FileDetailsResponse
# @app.post("/api/extract_details")
# def post_extract_details(file: UploadFile):
#     # content = file.file.read()
#     file_name = f"{uuid.uuid4()}_{file.filename}"
#     file_path = os.path.join(upload_dir,file_name)
#     with open(file_path,"wb") as buffer:
#         shutil.copyfileobj(file.file,buffer)

#     response = pipeline(file_path)

#     return json.loads(response)
