from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
async def read_items():
    return[{"user_name" : "Pierre"}]

@router.get("/user_all")
async def read_items():
    return[{"user_name" : "Ismail"}, {"user_name" : "Jacque"}]