from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def get_users():
    return {"msg": "User list coming soon!"}

@router.post("/signup")
def signup():
    return {"msg": "Signup system coming soon!"}

@router.get("/user/{user_id}")
def get_user(user_id: int):
    return {"msg": f"User details for user {user_id} coming soon!"}

