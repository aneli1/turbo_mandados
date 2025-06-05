def calcular_precio(costo):
    try:
        if isinstance(costo, bool):
            return None
        total = float(costo)
        return round(total, 2)
    except (ValueError, TypeError):
        return None