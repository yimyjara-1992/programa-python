"""
Fase 5 - Evaluación Final POA
Curso: Fundamentos de Programación (213022) - Grupo 213022_991
Problema 2: Menú de restaurante con promoción del 15 %
Estudiante: Yimy Alexander Correa Jara 

Un restaurante guarda su menú en una matriz con el formato:
    [Nombre del producto, Categoría, Precio base]

El programa aplica un 15 % de descuento a los productos que:
    1. pertenezcan a la categoría objetivo, y
    2. tengan un precio base MAYOR que el umbral establecido.
Si no se cumplen las dos condiciones, se mantiene el precio base.
"""

# ---------------------------------------------------------------
# Constantes de la promoción (se pueden cambiar sin tocar el resto)
# ---------------------------------------------------------------
DESCUENTO = 0.15                       # 15 % de descuento
CATEGORIA_OBJETIVO = "Platos fuertes"  # categoría que entra en la promoción
UMBRAL_PRECIO = 30000                  # el precio debe ser mayor a este valor

# Posiciones de cada dato dentro de una fila de la matriz
NOMBRE = 0
CATEGORIA = 1
PRECIO = 2

# ---------------------------------------------------------------
# Matriz del menú: [Nombre, Categoría, Precio base]
# ---------------------------------------------------------------
menu = [
    ["Bandeja paisa", "Platos fuertes", 32000],
    ["Sancocho de gallina", "Platos fuertes", 28000],
    ["Churrasco", "Platos fuertes", 30000],
    ["Lomo de res", "Platos fuertes", 45000],
    ["Cazuela de mariscos", "Sopas", 38000],
    ["Limonada de coco", "Bebidas", 9000],
    ["Tres leches", "Postres", 12000],
]


def calcular_precio_final(producto, categoria_objetivo, umbral):
    """Calcula el precio final de un producto del menú.

    Recibe:
        producto: lista [nombre, categoría, precio base].
        categoria_objetivo: categoría que participa en la promoción.
        umbral: el precio base debe ser mayor a este valor.
    Devuelve:
        El precio con 15 % de descuento si cumple las dos condiciones;
        de lo contrario, el precio base sin cambios.
    Lanza:
        ValueError si el precio no es un número válido (negativo o texto).
    """
    precio_base = producto[PRECIO]

    # Validación: el precio debe ser un número no negativo
    if isinstance(precio_base, bool) or not isinstance(precio_base, (int, float)) \
            or precio_base < 0:
        raise ValueError(f"precio inválido para '{producto[NOMBRE]}': {precio_base!r}")

    # Las DOS condiciones deben cumplirse al mismo tiempo (and)
    if producto[CATEGORIA] == categoria_objetivo and precio_base > umbral:
        return round(precio_base * (1 - DESCUENTO), 2)

    return precio_base


def formato_pesos(valor):
    """Devuelve el valor como pesos con punto de miles. Ej.: 27200 -> $27.200"""
    return "$" + f"{valor:,.0f}".replace(",", ".")


def mostrar_informe(matriz_menu, categoria_objetivo, umbral):
    """Recorre el menú y muestra nombre, precio base y precio final."""
    print("=" * 66)
    print("  MENÚ DEL RESTAURANTE - INFORME DE PRECIOS CON PROMOCIÓN")
    print("=" * 66)
    print(f"  Promoción: {int(DESCUENTO * 100)} % en '{categoria_objetivo}' "
          f"con precio base mayor a {formato_pesos(umbral)}")
    print("-" * 66)
    print(f"  {'Producto':<22}{'Precio base':>13}{'Precio final':>14}  Promoción")
    print("-" * 66)

    con_promocion = 0
    for producto in matriz_menu:
        try:
            precio_final = calcular_precio_final(producto, categoria_objetivo, umbral)
        except ValueError as error:
            print(f"  Registro omitido: {error}")
            continue

        precio_base = producto[PRECIO]
        aplica = "Sí" if precio_final < precio_base else "No"
        if aplica == "Sí":
            con_promocion += 1

        print(f"  {producto[NOMBRE]:<22}{formato_pesos(precio_base):>13}"
              f"{formato_pesos(precio_final):>14}  {aplica}")

    print("-" * 66)
    print(f"  Productos con promoción: {con_promocion} de {len(matriz_menu)}")
    print("=" * 66)


# ---------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------
if __name__ == "__main__":
    mostrar_informe(menu, CATEGORIA_OBJETIVO, UMBRAL_PRECIO)