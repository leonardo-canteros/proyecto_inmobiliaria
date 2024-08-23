__all__ = ["Property", "StoredProperty", "UpdationProperty"]

from pydantic import BaseModel, Field
from pydantic_mongo import PydanticObjectId

# Modelo para las propiedades inmobiliarias (campos obligatorios)
class Property(BaseModel):
    seller_id: PydanticObjectId  # ID del vendedor (usuario que crea la propiedad)
    photo: str                   # URL o referencia de la foto
    title: str                   # Título de la propiedad
    general_description: str      # Descripción general de la propiedad
    location: str                # Ubicación de la propiedad
    property_type: str           # Tipo de propiedad (casa, departamento, etc.)
    price: float                 # Precio de la propiedad

    # Campos opcionales para detalles específicos de la propiedad (campos opcionales)
    bedrooms: int = Field(default=None)    # Número de habitaciones
    bathrooms: int = Field(default=None)   # Número de baños
    living_room: bool = Field(default=None)  # Si tiene sala de estar (living)
    kitchen: bool = Field(default=None)      # Si tiene cocina
    dining_room: bool = Field(default=None)  # Si tiene comedor
    garage: bool = Field(default=None)       # Si tiene garage
    patio: bool = Field(default=None)        # Si tiene patio
    balcony: bool = Field(default=None)      # Si tiene balcón
    terrace: bool = Field(default=None)      # Si tiene terraza

# Modelo para la actualización de las propiedades
class UpdationProperty(BaseModel):
    seller_id: PydanticObjectId = Field(default=None)
    photo: str = Field(default=None)
    title: str = Field(default=None)
    general_description: str = Field(default=None)
    location: str = Field(default=None)
    property_type: str = Field(default=None)
    price: float = Field(default=None)

    # Campos opcionales para actualización
    bedrooms: int = Field(default=None)
    bathrooms: int = Field(default=None)
    living_room: bool = Field(default=None)
    kitchen: bool = Field(default=None)
    dining_room: bool = Field(default=None)
    garage: bool = Field(default=None)
    patio: bool = Field(default=None)
    balcony: bool = Field(default=None)
    terrace: bool = Field(default=None)

# Modelo para las propiedades almacenadas en la base de datos
class StoredProperty(Property):
    id: PydanticObjectId = Field(alias="_id")  # ID de la propiedad en la base de datos
