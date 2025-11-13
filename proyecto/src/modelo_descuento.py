import flet as ft
import formulario 

class Modelo_descuento(ft.Column):
    def __init__(self, page):
        super().__init__()
        self.page = page
        
        self.demanda_field = ft.TextField(label="Demanda (D)", width=200)
        self.costo_pedido_field = ft.TextField(label="Costo por pedido (S)", width=200)
        self.costo_mantenimiento_field = ft.TextField(label="Costo Mantenimiento (H)", width=200)
        self.d1_field = ft.TextField(label="Precio mas caro (C1))", width=200)
        self.d2_field = ft.TextField(label="Precio mas barato (C2)", width=200)
        self.q_min_field_= ft.TextField(label="Cantidad minima para descuento (Qmin)", width=200)

        self.q_resultado = ft.Text("0", size=16, weight=ft.FontWeight.BOLD)
        self.decision_resultado = ft.Text("0", size=16, weight=ft.FontWeight.BOLD)

        self.build_ui()

    def build(self):
        self.controls = [
            ft.Row([
                ft.text("MODELO CON DESCUENTO", size=24, weight=ft.FontWeight.BOLD),
                ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=self.volver_menu)
            ]),
            ft.Container(height=20),

            ft.Row([
               ft.Column([self.demanda_field, self.costo_pedido_field, self.costo_mantenimiento_field]),
                ft.Column([self.d1_field, self.d2_field, self.q_min_field]),
            ]),
            
            ft.Container(height=20),
            
            ft.ElevatedButton("Calcular", on_click=self.calcular,
                             style=ft.ButtonStyle(bgcolor=ft.Colors.CYAN_100)),
            
            ft.Container(height=20),
            
            ft.Column([
                ft.Row([ft.Text("Lote economico (Q):"), self.q_result]),
                ft.Row([ft.Text("Decision optima:"), self.decision_result]),
            ]),
        ]
    
    def calcular(self, e):
        try:
            D = float(self.demanda_field.value)
            S = float(self.costo_pedido_field.value)
            H = float(self.costo_mantenimiento_field.value)
            C1 = float(self.d1_field.value)
            C2 = float(self.d2_field.value)
            q = float(self.q_min_field.value)
            
            # Calcular Q sin descuento
            Q_sin = formulario.Q(D, S, H, 0, 1)
            
            # Calcular costos totales
            CT_sin = (D / Q_sin) * S + H * (Q_sin / 2) + C1 * D
            CT_con = (D / q) * S + H * (q / 2) + C2 * D
            
            if CT_con < CT_sin:
                decision = f"Pedir {q} unidades con precio {C2}"
            else:
                decision = f"Pedir {Q_sin:.2f} unidades con precio {C1}"
            
            self.q_result.value = f"{Q_sin:.2f}"
            self.decision_result.value = decision
            
        except ValueError:
            self.q_result.value = "Error en los datos ingresados"
            self.decision_result.value = "Error en los datos ingresados"
        
        self.page.update()
    
    def volver_menu(self, e):
        from menu_principal import MenuPrincipal
        self.page.clean()
        menu = MenuPrincipal(self.page)
        self.page.add(menu)
        self.page.update()