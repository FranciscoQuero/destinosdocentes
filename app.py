from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server.routers.travel_destinations import router as travel_destination_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(travel_destination_router, tags=['TravelDestination'], prefix='/travel-destination')
