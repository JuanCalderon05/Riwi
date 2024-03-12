"""
Ejercicio nivel 2: Empanadas
Modulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritméticas.
* Instrucciones básicas y consola.
* Dividir y conquistar: funciones y paso de párametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.

@author: Cupi2

"""

def crear_empanada(nombre: str, precio: int, vegana: bool, ingredientes: str, toppings: str, rating: float, unidades_vendidas: int, proxima_fecha_entrega: int) -> dict:
    """
    Función para crear una empanada en la plataforma.

    Parámetros
    ----------
    nombre : str
        Nombre de la empanada.
    precio : int
        Precio de la empanada.
    vegana : bool
        Indica si la empanada es vegana.
    ingredientes : str
        Cadena de caracteres separados por comas de los ingredientes de la empanada.
    toppings : str
        Cadena de caracteres separados por comas de los toppings sugeridos para la empanada.
    rating : float
        Rating de la empanada.
    unidades_vendidas : int
        Unidades vendidas de la empanada.
    proxima_fecha_entrega : int
        Próxima fecha de entrega de la empanada en formato YYYYMMDD.

    Retorno
    -------
    dict
        Diccionario con la información de la empanada.

    """
    # TODO - Implementar

def buscar_empanada_por_nombre(e1: dict, e2: dict, e3: dict, e4: dict, nombre: str) -> dict:
    """
    Busca una empanada en la plataforma por su nombre.

    Parámetros
    ----------
    e1 : dict
        Diccionario que contiene la información de la primera empanada.
    e2 : dict
        Diccionario que contiene la información de la segunda empanada.
    e3 : dict
        Diccionario que contiene la información de la tercera empanada.
    e4 : dict
        Diccionario que contiene la información de la cuarta empanada.
    nombre : str
        Nombre de la empanada a buscar.

    Retorno
    -------
    dict
        Diccionario con la información de la empanada buscada. Si no se encuentra la empanada, retorna None.

    """
    # TODO - Implementar

def buscar_empanada_mas_ganancias(e1: dict, e2: dict, e3: dict, e4: dict) -> dict:
    """
    Busca la empanada que ha generado más ganancias.

    Parámetros
    ----------
    e1 : dict
        Diccionario que contiene la información de la primera empanada.
    e2 : dict
        Diccionario que contiene la información de la segunda empanada.
    e3 : dict
        Diccionario que contiene la información de la tercera empanada.
    e4 : dict
        Diccionario que contiene la información de la cuarta empanada.

    Retorno
    -------
    dict
        Diccionario con la información de la empanada que ha generado más ganancias.

    """
    # TODO - Implementar

def buscar_empanadas_por_ingrediente(e1: dict, e2: dict, e3: dict, e4: dict, ingrediente: str) -> str:
    """
    Busca las empanadas que contengan un ingrediente específico.

    Parámetros
    ----------
    e1 : dict
        Diccionario que contiene la información de la primera empanada.
    e2 : dict
        Diccionario que contiene la información de la segunda empanada.
    e3 : dict
        Diccionario que contiene la información de la tercera empanada.
    e4 : dict
        Diccionario que contiene la información de la cuarta empanada.
    ingrediente : str
        Ingrediente a buscar.

    Retorno
    -------
    str
        Cadena con el nombre de las empanadas que contienen el ingrediente especificado. Si no se encuentra ninguna empanada, retorna None.

    """
    # TODO - Implementar

def buscar_empanada_con_mejor_rating_por_topping(e1: dict, e2: dict, e3: dict, e4: dict, topping: str) -> dict:
    """
    Busca la empanada con mejor rating que contenga un topping específico.

    Parámetros
    ----------
    e1 : dict
        Diccionario que contiene la información de la primera empanada.
    e2 : dict
        Diccionario que contiene la información de la segunda empanada.
    e3 : dict
        Diccionario que contiene la información de la tercera empanada.
    e4 : dict
        Diccionario que contiene la información de la cuarta empanada.
    topping : str
        Topping a buscar.

    Retorno
    -------
    dict
        Diccionario con la información de la empanada con mejor rating que contenga el topping especificado. Si no se encuentra ninguna empanada, retorna None.

    """
    # TODO - Implementar

def calcular_promedio_rating_empanadas(e1: dict, e2: dict, e3: dict, e4: dict, es_vegana: bool) -> float:
    """
    Calcula el promedio de rating de las empanadas veganas.

    Parámetros
    ----------
    e1 : dict
        Diccionario que contiene la información de la primera empanada.
    e2 : dict
        Diccionario que contiene la información de la segunda empanada.
    e3 : dict
        Diccionario que contiene la información de la tercera empanada.
    e4 : dict
        Diccionario que contiene la información de la cuarta empanada.
    es_vegana : bool
        Booleano que representa si se va a calcular el promedio de rating de empanadas veganas o no veganas. (True para veganas, False de lo contrario)

    Retorno
    -------
    float
        Promedio de rating de las empanadas.

    """
    # TODO - Implementar

def comparar_promedio_rating_empanadas_veganas_no_veganas(e1: dict, e2: dict, e3: dict, e4: dict) -> str:
    """
    Compara el promedio de rating de las empanadas veganas y no veganas.

    Parámetros
    ----------
    e1 : dict
        Diccionario que contiene la información de la primera empanada.
    e2 : dict
        Diccionario que contiene la información de la segunda empanada.
    e3 : dict
        Diccionario que contiene la información de la tercera empanada.
    e4 : dict
        Diccionario que contiene la información de la cuarta empanada.
    
    Retorno
    -------
    str
        Cadena con el mensaje de comparación entre el promedio de rating de las empanadas veganas y no veganas.

    """
    # TODO - Implementar

def modificar_rating_y_toppings(empanada: dict, nuevo_rating: float, nuevos_toppings: str) -> dict:
    """
    Modifica el rating y los toppings de una empanada

    Parámetros
    ----------
    empanada : dict
        Diccionario de la empanada a modificar
    nuevo_rating : float
        Nuevo rating de la empanada.
    nuevos_toppings : str
        Nuevos toppings de la empanada

    Retorno
    -------
    dict
        El diccionario modificado de la empanada.
    """
    # TODO - Implementar


def calcular_tiempo_proxima_fecha_entrega(fecha: int, empanada: dict) -> str:
    """
    Calcula los anios, meses y dias que faltan entre una fecha y la próxima fecha de entrega de una empanada.

    Parámetros
    ----------
    fecha : int
        Fecha en formato YYYYMMDD.
    empanada : dict
        Diccionario de la empanada.

    Retorno
    -------
    str
        Cadena con el mensaje de los anios, meses y dias que faltan entre una fecha y la próxima fecha de entrega de una empanada.
    """
    # TODO - Implementar


