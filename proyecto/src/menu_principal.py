import flet as ft
from proyecto.modelo_compra import Modelo_compra
from proyecto.modelo_escases import Modelo_escases
from proyecto.modelo_probabilistico import Modelo_probabilistico
from proyecto.modelo_produccion import Modelo_produccion
from proyecto.modelo_descuento import Modelo_descuento

class Menu_principal(ft.Column):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.build_ui()

    def build_ui(self):
        self.content = ft.Column([
            ft.Text("MODELOS DE INVENTARIO", 
                   size=28, 
                   weight=ft.FontWeight.BOLD,
                   color=ft.Colors.BLUE_900),
            
            ft.Container(height=30),
            
            # bocones para los diferentes modelos
            ft.ElevatedButton(
                "Modelo Compra",
                on_click=lambda _: self.abrir_modelo(Modelo_compra),
                style=ft.ButtonStyle(
                    bgcolor=ft.Colors.CYAN_100,
                    color=ft.Colors.BLACK,
                    padding=20
                ),
                width=300
            ),
            
            ft.ElevatedButton(
                "Modelo Produccion",
                on_click=lambda _: self.abrir_modelo(Modelo_produccion),
                style=ft.ButtonStyle(
                    bgcolor=ft.Colors.CYAN_100,
                    color=ft.Colors.BLACK,
                    padding=20
                ),
                width=300
            ),
            
            ft.ElevatedButton(
                "Modelo Con Descuento",
                on_click=lambda _: self.abrir_modelo(Modelo_descuento),
                style=ft.ButtonStyle(
                    bgcolor=ft.Colors.CYAN_100,
                    color=ft.Colors.BLACK,
                    padding=20
                ),
                width=300
            ),
            
            ft.ElevatedButton(
                "Modelo Con Escases",
                on_click=lambda _: self.abrir_modelo(Modelo_escases),
                style=ft.ButtonStyle(
                    bgcolor=ft.Colors.CYAN_100,
                    color=ft.Colors.BLACK,
                    padding=20
                ),
                width=300
            ),
            
            ft.ElevatedButton(
                "Modelo Probabilistico",
                on_click=lambda _: self.abrir_modelo(Modelo_probabilistico),
                style=ft.ButtonStyle(
                    bgcolor=ft.Colors.CYAN_100,
                    color=ft.Colors.BLACK,
                    padding=20
                ),
                width=300
            ),
            
        ], 
        alignment=ft.MainAxisAlignment.START, 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15)
    
    def abrir_modelo(self, modelo_class):
        self.page.clean()
        modelo = modelo_class(self.page)
        self.page.add(modelo)
        self.page.update()