"""
Main file
"""

from fastapi import FastAPI

from fastapi_course.routers import router


app = FastAPI()

app.include_router(router, prefix="")
