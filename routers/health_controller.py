import json
from fastapi import APIRouter, Response, Query, HTTPException
from fastapi.responses import JSONResponse
from utilities.DateTimeUtils import get_datetime_iso

router = APIRouter()

#--------------------------------------------------------------------
@router.get("/")
def health(response: Response):
    data = {
        'status': 'Healthy',
        'description': 'This is an API for the processing downloads requests.',
        'applicationName': 'healthcare-reports-api',
        'datetime_iso':  get_datetime_iso()
    }

    response.status_code = 200  # Set the desired HTTP status code
    pretty_data = json.dumps(data, indent=4)
    return Response(content=pretty_data, media_type="application/json")
    #return data
