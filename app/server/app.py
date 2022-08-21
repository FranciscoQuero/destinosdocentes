from fastapi import FastAPI

from server.routes.travel_destinations import router as travel_destination_router

app = FastAPI()

app.include_router(travel_destination_router, tags=['TravelDestination'], prefix='/travel-destination')


@app.get('/', tags=['root'])
async def read_root():
    return {'message': 'Hello world'}


@router.get('/{from_town}/{to_town}', response_description='Travel between two towns')
async def get_travel_destination(from_town, to_town):
    travel_destination = await retrieve_travel_destination(from_town, to_town)
    if travel_destination:
        return ResponseModel(travel_destination, 'Travel info')
    return ErrorResponseModel('An error occurred', 404, 'No travel found.')
