from pydantic import BaseModel


class Product(BaseModel):
    """
        id: int
        name: str
        description: str
        price: float
    """
    id: int
    name: str
    description: str
    price: float


class ProductRequest(BaseModel):
    name: str
    description: str
    price: float
