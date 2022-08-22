from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (retrieve_travel_destination, add_travel_destination,)
from server.models.travel_destinations import (
    ErrorResponseModel,
    ResponseModel,
    SchemaTravelDistance,
)

router = APIRouter()


@router.get('/{from_town}/{to_town}', response_description='Travel between two towns')
async def get_travel_destination(from_town, to_town):
    travel_destination = await retrieve_travel_destination(from_town, to_town)
    if travel_destination:
        return ResponseModel(travel_destination, 'Travel info')
    return ErrorResponseModel('An error occurred', 404, 'No travel found.')


@router.post('/', response_description='Travel added')
async def add_travel_data(travel: SchemaTravelDistance = Body(...)):
    travel_data = jsonable_encoder(travel)
    new_travel = await add_travel_destination(travel_data)
    return ResponseModel(new_travel, 'Travel added')
