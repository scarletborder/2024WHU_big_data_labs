from pydantic import BaseModel

# Define models to mirror proto messages
class ExampleRequestModel(BaseModel):
    id: str

class ExampleResponseModel(BaseModel):
    message: str

class ETTRequestModel(BaseModel):
    date: str
    HUFL: float
    HULL: float
    MUFL: float
    MULL: float
    LUFL: float
    LULL: float
    OT: float

class StandardResponseModel(BaseModel):
    result: str
    msg: str
