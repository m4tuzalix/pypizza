from functools import wraps
from typing import Protocol
from dependency import Session
from SQL.order import schemas

class Validator(Protocol):
    """Validator abstract class"""
    def validation(db: Session):
        ...

def validator(validator: Validator):
    """Decorator for dynamic validator allocation"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                db: Session = args[0]
                schema: schemas = args[1]
            except IndexError:
                raise AttributeError("Insufficient amount of arguments for validator")
            exception = validator(schema).validation(db)
            if exception: raise exception
            return func(*args, **kwargs)
        return wrapper
    return decorator