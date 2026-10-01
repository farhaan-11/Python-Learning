from typing import List, Dict, Optional,Annotated,Literal
from pydantic import BaseModel,Field,ConfigDict,BeforeValidator


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

PyObjectId = Annotated[str, BeforeValidator(str)]

class ProductOut(ProductCreate):
    model_config = ConfigDict(populate_by_name=True)
    id: PyObjectId = Field(alias="_id")


# ProductOut(**{"_id": "abc123", "name": "iPhone", "price": 79999})

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    brand: Optional[str] = None
    price: Optional[int] = None
    discount_percent: Optional[int] = None
    stock: Optional[int] = None
    in_stock: Optional[bool] = None
    rating: Optional[float] = None
    tags: Optional[List[str]] = None
    seller: Optional[Dict[str, str]] = None



class ProductOutQuery(ProductUpdate):
     model_config = ConfigDict(populate_by_name=True)
     id: PyObjectId = Field(alias="_id")


class ProductFilter(BaseModel):
    category: Optional[str] = None
    brand: Optional[str] = None
    min_price: Optional[int] = None
    max_price: Optional[int] = None
    in_stock: Optional[bool] = None
    price: Optional[int] = None
    sort_by_price: Optional[Literal["asc", "desc"]] = None


    # naya filter chahiye? bas yahan ek line add karo


class ProductListResponse(BaseModel):
    message: str
    total: int
    data: list[ProductOutQuery]

    