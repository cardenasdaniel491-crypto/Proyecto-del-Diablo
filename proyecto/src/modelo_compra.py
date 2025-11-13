import flet as ft
import formulario 

class Modelo_compra(ft.Column):
    def __init__(self, page):
        super().__init__()
        self.page = page

        # campos de entrada para los parámetros del modelo de compra
        self.demanda_field = ft.TextField(label="Demanda (D)", width=200)
        self.costo_pedido_field = ft.TextField(label="Costo por pedido (S)", width=200)
        self.dias_field = ft.TextField(label="Días trabajados", width=200)
        self.costo_mantenimiento_field = ft.TextField(label="Costo Mantenimiento (H)", width=200)

        # resultados 
        self.q_restultado = ft.Text("", size=16, weight=ft.FontWeight.BOLD)
        self.cta_resultado = ft.Text("", size=16, weight=ft.FontWeight.BOLD)
        self.ctu_resultado = ft.Text("", size=16, weight=ft.FontWeight.BOLD)    

        self.build_ui()

        def build_ui(self):
            self.controls = [
            ft.Row([
                ft.Text("MODELO DE COMPRA", size=24, weight=ft.FontWeight.BOLD),
                ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=self.volver_menu)
            ]),
            ft.Container(height=20),
            
            ft.Row([
                ft.Column([
                    self.demanda_field,
                    self.costo_pedido_field,
                    self.dias_field,
                    self.costo_mantenimiento_field,
                ]),
            ]),
            
            ft.Container(height=20),
            
            ft.ElevatedButton("Calcular", on_click=self.calcular,
                             style=ft.ButtonStyle(bgcolor=ft.Colors.CYAN_100)),
            
            ft.Container(height=20),
            
            ft.Column([
                ft.Row([ft.Text("Cantidad potima del lote (Q):"), self.q_result]),
                ft.Row([ft.Text("Costo Total Anual(CTA):"), self.cta_result]),
                ft.Row([ft.Text("Costo Total Unitario(CTU):"), self.ctu_result]),
            ]),
        ]
            
    def calcular(self, e):
        try:
            D = float(self.demanda_field.value)
            S = float(self.costo_pedido_field.value)
            H = float(self.costo_mantenimiento_field.value)
            dias = float(self.dias_field.value)

            Q = formulario.calcular_q_optima(D, S, H)
            CTU = formulario.calcular_ctu(CTA, D)
            CTA = formulario.calcular_cta(D, S, H, Q)

            self.q_resultado.value = f"{Q:.2f}"
            self.cta_resultado.value = f"${CTA:.2f}"
            self.ctu_resultado.value = f"${CTU:.2f}"
        except ValueError:
            self.q_restultado.value = "Error en los datos ingresados"
            self.cta_resultado.value = "Error en los datos ingresados"
            self.ctu_resultado.value = "Error en los datos ingresados"
        self.page.update()

        def volver_menu(self, e):
            from menu_principal import Menu_principal
            self.page.controls.clean()
            menu = Menu_principal(self.page)
            self.page.add(menu)
            self.page.update()