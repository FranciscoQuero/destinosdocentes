from fastapi import APIRouter

from server.repositories.travel_destinations import retrieve_n_nearest_travel_destinations, \
    retrieve_destinations_from_list
from server.models.travel_destinations import ErrorResponseModel, ResponseModel


router = APIRouter()


@router.get('/{from_town}', response_description='Travel between two towns')
async def get_n_nearest_travel_destinations(from_town: str, limit: int = 120):
    travel_destinations = await retrieve_n_nearest_travel_destinations(from_town, limit)
    if travel_destinations:
        return ResponseModel(travel_destinations, 'Travel info')
    return ErrorResponseModel('An error occurred', 404, 'No travel found.')


@router.get('/{from_town}/sipri', response_description='Sort destinations in a list based on their distance from a town')
async def get_sorter_sipri_travel_destinations(from_town: str, sipri_towns: str):
    travel_destinations = await retrieve_destinations_from_list(from_town, sipri_towns)

    if travel_destinations:
        print(ResponseModel(travel_destinations, 'Travel info'))
        return ResponseModel(travel_destinations, 'Travel info')
    return ErrorResponseModel('An error occurred', 404, 'No travel found.')
