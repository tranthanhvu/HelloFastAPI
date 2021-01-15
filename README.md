# HelloFastAPI
Build a simple server with FastAPI
https://fastapi.tiangolo.com

# Setup
- First: install python

- Install FastAPI and Uvicorn
"pip install fastapi"
"pip install uvicorn"

*if uvicorn is installed in a path which is not on PATH, you have to update the $PATH
"export PATH=$PATH:{newPath}" <-- newPath is the path which is mention above
"echo $PATH". <-- to double check the path

// Start server
"uvicorn main:app --reload"
