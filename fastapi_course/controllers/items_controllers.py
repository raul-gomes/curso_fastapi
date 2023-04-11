"""
Controller
"""

from typing import Dict, List
from fastapi import APIRouter

from fastapi_course.models import schemas


router = APIRouter()

banco_dados = []


@router.post('/')
def add_item(item: schemas.Item) -> Dict:
    """_summary_

    Args:
        item (Item): _description_

    Returns:
        _type_: _description_
    """
    banco_dados.append(item)

    return {item}

@router.get('/')
def list_items() -> List[Dict]:
    """_summary_

    Returns:
        _type_: _description_
    """
    return banco_dados