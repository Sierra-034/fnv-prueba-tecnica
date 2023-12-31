import peewee
from fastapi import APIRouter, status, HTTPException, Depends
from src.schemas import ProductoSchema
from src.models import Producto
from src.dependencies import oauth2_schema

router = APIRouter(
    prefix='/productos',
    dependencies=[Depends(oauth2_schema)]
)

@router.post(
    '', response_model=ProductoSchema,
    status_code=status.HTTP_201_CREATED
)
def create_producto(producto: ProductoSchema):
    try:
        producto_nuevo = Producto.create(**producto.dict())
    except peewee.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='El producto ya existe'
        )
    
    return producto_nuevo