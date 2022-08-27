from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.repositories.travel_destinations import retrieve_travel_destination, retrieve_n_nearest_travel_destinations
from server.models.travel_destinations import ErrorResponseModel, ResponseModel, SchemaTravelDistance


router = APIRouter()


@router.get('/{from_town}', response_description='Travel between two towns')
async def get_n_nearest_travel_destinations(from_town: str, limit: int = 120):
    travel_destinations = await retrieve_n_nearest_travel_destinations(from_town, limit)
    if travel_destinations:
        return ResponseModel(travel_destinations, 'Travel info')
    return ErrorResponseModel('An error occurred', 404, 'No travel found.')


@router.get('/{from_town}/{to_town}', response_description='Travel between two towns')
async def get_travel_destination(from_town: str, to_town: str):
    travel_destination = await retrieve_travel_destination(from_town, to_town)
    if travel_destination:
        return ResponseModel(travel_destination, 'Travel info')
    return ErrorResponseModel('An error occurred', 404, 'No travel found.')
