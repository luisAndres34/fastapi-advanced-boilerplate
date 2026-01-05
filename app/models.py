from sqlmodel import SQLModel, Field

class ItemBase(SQLModel):
    name: str = Field(index=True, unique=True)
    price: int = Field(gt=0)
    stock: int = Field(ge=0)

class Item(ItemBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class UpdateItem(SQLModel):
    name: str | None = Field(default=None)
    price: int | None = Field(default=None, gt=0)
    stock: int | None = Field(default=None, ge=0)

class FilterItem(SQLModel):
    name: str | None = Field(default=None)
    exact_price: int | None = Field(default=None, gt=0)
    stock: int | None = Field(default=None, ge=0)
    min_price: int | None = Field(default=None, ge=0)
    max_price: int | None = Field(default=None, gt=0)