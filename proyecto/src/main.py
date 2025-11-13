import flet as ft
from menu_principal import Menu_principal

def main(page: ft.Page):
    # configura la página
    page.title = "Sistema de Modelos de Inventario"
    page.window.width = 650
    page.window.height = 500
    page.window.center()
    
    # muestra el menú principal
    menu = Menu_principal(page)
    page.add(menu)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)