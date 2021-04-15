from typing import Optional
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# status:
STATUS_normal = "00"
STATUS_maintenance = "01"
STATUS_maintenanceCannotUpdate = "02"
STATUS_terminalRegistration = "10"
STATUS_draftNotFound = "11"
STATUS_folderNotFound = "12"
STATUS_limitRegistrtion = "21"
STATUS_executionError = "22"
STATUS_duplicateFolder = "23"
STATUS_sessionTimeOut = "91"
STATUS_authenticationError = "92"
STATUS_otherError = "99"

STATUS_SERVER = STATUS_normal

#--------------- Model ------------------
class Document(BaseModel):
    id: str
    title: str
    text: str
    last_update: str
    folder_id: str
    folder_name: str

class Folder(BaseModel):
    folder_id: str
    folder_name: str

class DeviceInfo(BaseModel):
    id: str
    name: str
    regist_date: str

#--------------- Request ------------------
class RequestDataUpdateDraft(BaseModel):
    device_id: str
    document_id: str
    folder_id: str
    document_title: str
    document_text: str
    document_last_update: str
    document_overwrite: bool

#--------------- Response ------------------
class ResponseStatusCode(BaseModel):
    status: str
    error_code: Optional[str]

class ResponseDraftDetail(BaseModel):
    status: str
    error_code: Optional[str]
    document_title: str
    document_text: str
    document_last_update: str

class ResponseDrafts(BaseModel):
    status: str
    error_code: Optional[str]
    total: int
    offset: str
    limit: str
    folder_id: str
    folder_name: str
    documents: List[Document]

class ResponseFolders(BaseModel):
    status: str
    error_code: Optional[str]
    devices: List[Folder]

class ResponseUpdateDrafts(BaseModel):
    status: str
    error_code: Optional[str]
    last_update: str

class ResponseDevices(BaseModel):
    status: str
    error_code: Optional[str]
    devices: List[DeviceInfo]

class ResponseAccountName(BaseModel):
    status: str
    error_code: Optional[str]
    account_name: str

#--------------- DB ------------------
fakeDB_docs = [
    Document(
        id = "1",
        title = "title 1",
        text = "text 1",
        last_update = "20201112202020",
        folder_id = "",
        folder_name = ""
        ),
    Document(
        id = "2",
        title = "title 2",
        text = "text 2",
        last_update = "20201112202021",
        folder_id = "folder_id",
        folder_name = "folder_name"
    )
]   

fakeDB_folders = [
    Folder(
        folder_id = "3K0XXXXX-83XX-HEXX-KIXX-29KH83XXXXX1",
        folder_name = "ドラえもん 1"
    ),
    Folder(
        folder_id = "3K0XXXXX-83XX-HEXX-KIXX-29KH83XXXXX2",
        folder_name = "ドラえもん 2"
    )
]

fakeDB_devices = [
    DeviceInfo(
        id = "6E94A2DC-E3DD-4E05-A663-D601DA298F29",
        name = "iPhone 12",
        regist_date = "20210121"
    )
    # ,DeviceInfo(
    #     id = "ED8C2079-E22C-4445-B493-A075E154570F",
    #     name = "iPhone 6S",
    #     regist_date = "20210121"
    # )
]

#--------------- API ------------------
@app.get("/api/v2/devices/")
def getRegisteredDevices():
    return ResponseDevices(
        status = STATUS_SERVER,
        devices = fakeDB_devices
    )


@app.post("/api/v2/devices/delete/")
def delete_device():
    return ResponseStatusCode(
        status = STATUS_SERVER
    )


@app.post("/api/v2/devices/add/")
def addDevice():
    return ResponseStatusCode(
        status = STATUS_SERVER
    )


@app.get("/api/v2/status/")
def getAPIStatus():
    return ResponseStatusCode(
        status = STATUS_SERVER,
        error_code = "ABC"
    )


@app.get("/api/v2/documents/")
def getDraftList(device_id: str, filtering: bool, folder_id: str, offset: str, limit: str):
    return ResponseDrafts(
        status = STATUS_SERVER,
        total = 100,
        offset = offset,
        limit = limit,
        folder_name = "test",
        folder_id = folder_id,
        documents = fakeDB_docs
    ) 

@app.get("/api/v2/documents/{item_id}")
def getDraftDetail(item_id: str):
    doc = fakeDB_docs[int(item_id) - 1]
    return ResponseDraftDetail(
        status = STATUS_SERVER,
        document_title = doc.title,
        document_text = doc.text + "long long long long long",
        document_last_update = doc.last_update
    )


@app.post("/api/v2/documents/add/")
def addOrUpdateDraft(request: RequestDataUpdateDraft):
    return ResponseUpdateDrafts(
        status = STATUS_SERVER,
        error_code = "CODE",
        last_update = "20201112202021"
    )


@app.post("/api/v2/documents/delete/")
def deleteDrafts():
    return ResponseStatusCode(
        status = STATUS_SERVER
    )


@app.post("/api/v2/documents/move/")
def moveDrafts():
        return ResponseStatusCode(
        status = STATUS_SERVER
    )


@app.get("/api/v2/folders/")
def getFolderList():
    return ResponseFolders(
        status = STATUS_SERVER,
        devices = fakeDB_folders
    )


@app.post("/api/v2/folders/add/")
def addOrUpdateFolder():
    return ResponseStatusCode(
        status = STATUS_SERVER,
        error_code = "ABC"
    )


@app.post("/api/v2/folders/delete/")
def deleteFolder():
    return ResponseStatusCode(
        status = STATUS_SERVER,
        error_code = "ABC"
    )


@app.get("/api/v2/account/")
def getAccountInfo():
    return ResponseAccountName(
        status = STATUS_SERVER,
        account_name = "hihi"
    ) 


@app.get("/api/v2/ios_device_name/{device_code}")
def getDeviceName(device_code: str):
    return {
        "status": "00",
        "device_name": device_code + " name"
    }
