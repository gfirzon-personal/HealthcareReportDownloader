from fastapi import APIRouter, Response, Query, HTTPException
from utilities.DateTimeUtils import get_datetime_iso

router = APIRouter()

# Define a simple route
@router.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI web API!"}

# Define another route for a GET request
@router.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Define another route for a GET request
@router.get("/list")
def list():
    directory = '/usr/local/bin/'
    
    # Get the list of files and directories in the specified path
    try:
        contents = os.listdir(directory)
    except FileNotFoundError:
        return json.dumps({"error": "Directory not found"})
    except PermissionError:
        return json.dumps({"error": "Permission denied"})
    
    # Convert the list to a JSON formatted string
    return json.dumps({"contents": contents})    

# Define a POST route
@router.post("/create-item/")
def create_item(name: str, price: float):
    return {"name": name, "price": price}