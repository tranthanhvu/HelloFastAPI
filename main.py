from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# status:
# case .maintenance: "1"
# case .maintenanceCannotUpdate: "2"
# case .terminalRegistration: "10"
# case .draftNotFound: "11"
# case .folderNotFound: "12"
# case .limitRegistrtion: "21"
# case .executionError: "22"
# case .duplicateFolder: "23"
# case .sessionTimeOut: "91"
# case .authenticationError: "92"
# case .otherError: "99"

status = "1"

class DeviceInfo(BaseModel):
    id: str
    name: str
    regist_date: str

class Document(BaseModel):
    id: str
    title: str
    text: str
    last_update: str
    folder_id: str
    folder_name: str
    
class Folder(BaseModel):
    id: str
    folder_name: str

@app.get("/api/v1/status/")
def read_root():
    return { "status": status}

@app.get("/api/v1/devices/")
def get_devices():
    return { "devices"}

@app.post("/api/v1/devices/delete/")
def delete_device():
    return { "device delete"}

@app.get("/api/v1/documents/")
def get_documents():
    return { "/api/v1/documents/" }

@app.get("/items/{item_id}") 
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
