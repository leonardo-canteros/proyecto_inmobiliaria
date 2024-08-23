"""Resumen general:
    El archivo define distintos modelos de usuario para diferentes contextos, 
        como la creación, actualización, login, y la representación pública o privada de un usuario.
   Usa Pydantic para definir y validar los datos de estos usuarios, garantizando que cumplan con las restricciones definidas en los esquemas.
   Utiliza enumeraciones para definir roles específicos y ofrece flexibilidad en el manejo de usuarios dependiendo de las operaciones (creación, actualización, autenticación).
   """
__all__ = [
    "BaseUser",
    "LoginUser",
    "PublicStoredUser",
    "PrivateStoredUser",
    "CreationUser",
    "UpdationUser",
]

from enum import Enum
from pydantic import BaseModel, Field, EmailStr
from pydantic_mongo import PydanticObjectId

# Roles de usuario
class Role(str, Enum):
    admin = "admin"
    customer = "customer"
    seller = "seller"

# Modelo base para el usuario
class BaseUser(BaseModel):
    id: PydanticObjectId = Field(default_factory=PydanticObjectId)
    username: str                          # Usuario
    first_name: str                        # Nombre
    last_name: str                         # Apellido
    email: EmailStr                        # Email (obligatorio y validado)
    phone: str = Field(default=None)       # Teléfono fijo (opcional)
    mobile: str = Field(default=None)      # Teléfono móvil (opcional)
    role: Role = Role.customer             # Rol del usuario (por defecto es customer)
    image: str | None = Field(default=None)# Imagen (opcional)

# Modelo para la creación de usuarios
class CreationUser(BaseUser):
    password: str                          # Contraseña obligatoria

# Modelo para la actualización de usuarios
class UpdationUser(BaseUser):
    username: str = Field(default=None)
    first_name: str = Field(default=None)
    last_name: str = Field(default=None)
    phone: str = Field(default=None)
    mobile: str = Field(default=None)
    role: Role = Field(default=None)
    image: str | None = Field(default=None)
    email: EmailStr = Field(default=None)

# Modelo para el inicio de sesión
class LoginUser(BaseModel):
    username: str
    password: str

# Modelo público de usuario almacenado (sin datos sensibles)
class PublicStoredUser(BaseUser):
    id: PydanticObjectId = Field(alias="_id")

# Modelo privado de usuario almacenado (incluye datos sensibles como el hash de la contraseña)
class PrivateStoredUser(BaseUser):
    id: PydanticObjectId = Field(alias="_id")
    hash_password: str
