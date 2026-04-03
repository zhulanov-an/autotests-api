# {
#   "course": {
#     "id": "string",
#     "title": "string",
#     "maxScore": 0,
#     "minScore": 0,
#     "description": "string",
#     "previewFile": {
#       "id": "string",
#       "filename": "string",
#       "directory": "string",
#       "url": "https://example.com/"
#     },
#     "estimatedTime": "string",
#     "createdByUser": {
#       "id": "string",
#       "email": "user@example.com",
#       "lastName": "string",
#       "firstName": "string",
#       "middleName": "string"
#     }
#   }
# }

from pydantic import BaseModel


class ShortUserSchema(BaseModel):
    id: str
    email: str


class UserSchema(ShortUserSchema):
    lastName: str
    firstName: str
    middleName: str


class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: str


class CourseSchema(BaseModel):
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: FileSchema
    estimatedTime: str
    createdByUser: UserSchema


class GetCourseResponseSchema(BaseModel):
    course: CourseSchema
