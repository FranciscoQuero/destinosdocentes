from typing import Optional

from pydantic import BaseModel, EmailStr, Field, constr, conint, confloat


class SchemaTravelDistance(BaseModel):
    from_town: constr(strict=True) = Field(..., alias='from')
    to_town: constr(strict=True) = Field(..., alias='to')
    travel_time: confloat() = Field(..., alias='time')
    distance: confloat() = Field(...)
    state: constr(strict=True) = Field(...)

    class Config:
        schema_extra = {
            'example': {'from': 'Abla', 'to': 'Abla', 'time': 0, 'distance': 0, 'state': 'Almería'}
        }


def ResponseModel(data, message):
    return {
        'data': [data],
        'code': 200,
        'message': message,
    }


def ErrorResponseModel(error, code, message):
    return {'error': error, 'code': code, 'message': message}
