from pydantic import BaseModel, Field


class AdminCreate(BaseModel):
    username: str
    password: str

class AdminModel(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    password_hash: str = Field(exclude=True)
    is_verified: bool


class SuperAdminCreate(BaseModel):
    username: str
    password: str


class SuperAdminModel(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    password_hash: str = Field(exclude=True)
    is_verified: bool


class PasswordChange(BaseModel):
    pass

class PasswordReset(BaseModel):
    pass