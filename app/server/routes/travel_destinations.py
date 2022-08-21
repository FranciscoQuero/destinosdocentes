from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import retrieve_travel_destination
from server.models.travel_destinations import (
    ErrorResponseModel,
    ResponseModel,
    SchemaTravelDistance,
    UpdateTravelDistanceModel,
)

router = APIRouter()
