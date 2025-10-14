# menu_catalog.py
from typing import List
from ElementoMenu import CrearMenu
from Ingrediente import Ingrediente
from IMenu import IMenu

def get_default_menus() -> List[IMenu]:
    return [
        CrearMenu(
            "Papas Fritas",
            [ Ingrediente("Papas", "unid", 5)],
            precio=500
        ),
        CrearMenu(
            "Pepsi",
            [ Ingrediente("Pepsi", "unid", 1)],
            precio=1100
        ),
        CrearMenu(
            "Completo",
            [
                Ingrediente("Vienesa","unid", 1),
                Ingrediente("Pan de completo","unid", 1),
                Ingrediente("Palta","kg",0.5),
                Ingrediente("Tomate","kg",0.2),
            ],
            precio=1800,
            icono_path="IMG/icono_hotdog_sin_texto_64x64.png",
        ),
        CrearMenu(
            "Hamburguesa",
            [ 
            Ingrediente("Pan de hamburguesa", "unid", 1),
            Ingrediente("lámina de queso", "unid", 1),
            Ingrediente("churrasco de carne", "unid", 1),
            ],
            precio=3500
        ),
        CrearMenu(
            "Panqueques",
            [ 
            Ingrediente("panqueques", "unid", 2),
            Ingrediente("manjar", "unid", 1),
            Ingrediente("azúcar flor", "unid", 1),
            ],
            precio=2000
        ),
        CrearMenu(
            "Pollo frito",
            [
            Ingrediente("presa de pollo", "unid", 1),
            Ingrediente("porción de harina", "unid", 1),
            Ingrediente("porción de aceite", "unid", 1),
            ],
            precio=2800
        ),
        CrearMenu(
            "Ensalada mixta",
            [
            Ingrediente("lechuga", "unid", 1),
            Ingrediente("tomate", "unid", 1),
            Ingrediente("zanahoria", "unid", 1),
            ],
            precio=1500
        ),
        CrearMenu(
            "Sopa de verduras",
            [
            Ingrediente("calabacín", "unid", 1),
            Ingrediente("zanahoria", "unid", 1),
            Ingrediente("apio", "unid", 1),
            Ingrediente("caldo de verduras", "litro", 1),
            ],
            precio=1200
        ),
    ]