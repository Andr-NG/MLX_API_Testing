from pydantic import BaseModel


class Status(BaseModel):
    error_code: str
    http_code: int
    message: str


class ApiExceptionError(BaseModel):
    status: Status
