import os
import motor.motor_asyncio
from bson.objectid import ObjectId


client = motor.motor_asyncio.AsyncIOMotorClient(os.environ['DB_URL'])

database = client.travel_destinations

travel_destinations_collection = database.get_collection("travel_destinations_collections")


def travel_destination_helper(travel_destination) -> dict:
    return {'from': travel_destination['from'], 'to': travel_destination['to'], 'time': str(travel_destination['time']),
            'distance': str(travel_destination['distance'])}


async def retrieve_travel_destination(from_town: str, to_town: str) -> dict:
    search_dict = {'from': from_town, 'to': to_town}
    travel_destination = await travel_destinations_collection.find_one(search_dict)
    if travel_destination:
        return travel_destination_helper(travel_destination)


async def add_travel_destination(travel_destination_data: dict) -> dict:
    search_dict = {'from': travel_destination_data['from'], 'to': travel_destination_data['to']}
    travel = await travel_destinations_collection.insert_one(travel_destination_data)
    new_travel = await travel_destinations_collection.find_one(search_dict)
    return travel_destination_helper(new_travel)