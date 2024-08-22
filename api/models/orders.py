"""Resumen general:
Order: Representa una orden que se está creando, y contiene los detalles del cliente, el producto, el precio y la cantidad.
StoredOrder: Extiende Order y añade el campo id para manejar las órdenes que ya han sido almacenadas en la base de datos MongoDB.
"""

__all__ = ["Order", "StoredOrder"]

from pydantic import BaseModel, Field
from pydantic_mongo import PydanticObjectId


class Order(BaseModel):
    customer_id: PydanticObjectId
    product_id: PydanticObjectId
    price: float
    quantity: int


class StoredOrder(Order):
    id: PydanticObjectId = Field(alias="_id")
