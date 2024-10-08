from fastapi import APIRouter
from . import users, signup, login, orders, sms

base_router = APIRouter()

base_router.include_router(users.router, tags=["users"])
base_router.include_router(orders.router, tags=["orders"])
base_router.include_router(signup.router)
base_router.include_router(login.router)
base_router.include_router(sms.router)