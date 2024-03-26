from pydantic import BaseModel

# Модель для товара
class ItemBase(BaseModel):
    name: str
    description: str
    price: float

# Модель для пользователя
class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

# Модель для заказа
class OrderBase(BaseModel):
    user_id: int
    item_id: int

# Модели для возврата данных из БД
class Item(ItemBase):
    id: int

class User(UserBase):
    id: int

class Order(OrderBase):
    id: int
    order_date: str
    status: str
