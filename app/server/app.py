from fastapi import FastAPI

from server.routes.travel_destinations import router as travel_destination_router

app = FastAPI()

app.include_router(travel_destination_router, tags=['TravelDestination'], prefix='/travel-destination')


@app.get('/', tags=['root'])
async def read_root():
    return {'message': 'Hello world'}
