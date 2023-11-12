from fastapi import FastAPI


from auth.base_config import auth_backend, fastapi_users

from auth.schemas import UserRead, UserCreate

from operations.router import router as router_operation
from users.router import router as router_user

app = FastAPI(title="Trading App")

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(router_operation)
app.include_router(router_user)
