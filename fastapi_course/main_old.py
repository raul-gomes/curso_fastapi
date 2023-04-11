import logging
from typing import Optional, Union
from .models import schemas

from fastapi import FastAPI, Header, Response, Cookie


app = FastAPI()



@app.get('/')
def read_root(user_agent: Optional[str] = Header(None)):
    """_summary_

    Returns:
        _type_: _description_
    """
    logging.debug(user_agent)
    return {'User Agent': user_agent}

@app.get('/cookie')
def cookie(response: Response):
    """_summary_

    Args:
        response (Response): _description_

    Returns:
        _type_: _description_
    """
    response.set_cookie(key="meucookie", value="123456")
    return {'cookie': True}


@app.get("/get-cookie")
def get_cookie(meucookie: Optional[str] = Cookie(None)):
    """_summary_

    Args:
        meucookie (Optional[str], optional): _description_. Defaults to Cookie(None).

    Returns:
        _type_: _description_
    """
    return {"Cokkie": meucookie}


@app.get('/items/{item_id}')
def read_item(item_id: int, _: Union[str, None] = None):
    """_summary_

    Args:
        item_id (int): _description_
        q (Union[str, None], optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    return {'item_id': item_id, 'q': _}

@app.post('/item')
def add_item(item: schemas):
    """_summary_

    Args:
        item (Item): _description_

    Returns:
        _type_: _description_
    """
    return item
