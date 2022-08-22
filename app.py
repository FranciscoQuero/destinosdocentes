from fastapi import FastAPI
from server.routers.travel_destinations import router as travel_destination_router

app = FastAPI()

app.include_router(travel_destination_router, tags=['TravelDestination'], prefix='/travel-destination')
