"""
Schemas class
"""

from dataclasses import dataclass

#from pydantic import BaseModel



@dataclass
class Item:
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """
    id: int
    quantitiy: int
    description: str
    price: float


#class Item(BaseModel):
#    """_summary_
#
#    Args:
#        BaseModel (_type_): _description_
#    """
#    id: int
#    quantitiy: int
#    description: str
#    price: float
