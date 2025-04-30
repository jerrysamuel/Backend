
from fastapi import APIRouter

router = APIRouter()

@router.get("/login-check")
def login_check():
    return {"msg": "Login system coming soon!"}
