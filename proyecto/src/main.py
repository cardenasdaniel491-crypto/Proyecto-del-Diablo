import flet as ft

def main(page: ft.Page):
    t = ft.Text(value="Hola!", color="green")
    page.controls.append(t)
    page.update()

ft.app(main)