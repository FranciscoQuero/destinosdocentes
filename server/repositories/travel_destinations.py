import os
import motor.motor_asyncio


client = motor.motor_asyncio.AsyncIOMotorClient(os.environ['DB_URL'])

database = client.traveldestinations

travel_destinations_collection = database.get_collection("traveldestinationscollections")


def travel_destination_helper(travel_destination) -> dict:
    return {'from': travel_destination['from'], 'to': travel_destination['to'], 'time': str(travel_destination['time']),
            'distance': str(travel_destination['distance']), 'state': travel_destination['state']}


async def retrieve_travel_destination(from_town: str, to_town: str) -> dict:
    search_dict = {'from': from_town, 'to': to_town}
    travel_destination = await travel_destinations_collection.find_one(search_dict)
    if travel_destination:
        return travel_destination_helper(travel_destination)


async def retrieve_n_nearest_travel_destinations(from_town: str, limit: int = 0) -> [dict]:
    search_dict = {'from': from_town}
    travel_destinations = travel_destinations_collection.find(search_dict).sort('time').limit(limit)

    if travel_destinations:
        return [travel_destination_helper(travel_destination) async for travel_destination in travel_destinations]


async def retrieve_destinations_from_list(from_town: str, sipri_destinations: str) -> [dict]:
    destinations_list = sipri_destinations.split(',')
    search_dict = {'from': from_town, 'to': {'$in': destinations_list}}
    travel_destinations = travel_destinations_collection.find(search_dict).sort('time')
    print(travel_destinations)
    if travel_destinations:
        return [travel_destination_helper(travel_destination) async for travel_destination in travel_destinations]
