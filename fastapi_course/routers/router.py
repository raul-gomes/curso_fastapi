"""
Router
"""
from fastapi import APIRouter

from fastapi_course.controllers import items_controllers as items


router = APIRouter()

router.include_router(items.router, prefix='/item')
