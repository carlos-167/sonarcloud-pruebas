"""Funciones para calcular importes de una venta."""


def calcular_total(precio_unitario: float, cantidad: int) -> float:
    """Regresa el importe total de una compra.

    Args:
        precio_unitario: precio de un solo articulo.
        cantidad: numero de articulos comprados.

    Returns:
        El precio unitario multiplicado por la cantidad.

    Raises:
        ValueError: si el precio o la cantidad son negativos.
    """
    if precio_unitario < 0 or cantidad < 0:
        raise ValueError("El precio y la cantidad no pueden ser negativos")
    return precio_unitario * cantidad
