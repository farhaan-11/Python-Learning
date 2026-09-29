from typing import List, Dict, Optional
from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    category: Optional[str] = None
    brand: Optional[str] = None
    price: int
    discount_percent: int = 15
    stock: int = 10
    in_stock: bool = True
    rating: float = 3.5
    tags: List[str] = []
    seller: Dict[str, str] = {}


class ProductOut(ProductCreate):
    id: str