import math
import flet as ft
import formulario

class Modelo_probabilistico(ft.Column):
    def __init__(self, page):
        super().__init__()
        self.page = page
        
        self.demanda_field = ft.TextField(label="Demanda Promedio (μ)", width=200)
        self.varianza_field = ft.TextField(label="Varianza (σ²)", width=200)
        self.z_field = ft.TextField(label="Valor Z", width=200)
        self.costo_pedido_field = ft.TextField(label="Costo pedido (S)", width=200)
        self.costo_mantenimiento_field = ft.TextField(label="Costo Mantenimiento (H)", width=200)
        self.lead_time_field = ft.TextField(label="Tiempo de entrega (L)", width=200)
        
        self.q_result = ft.Text("0", size=16, weight=ft.FontWeight.BOLD)
        self.pr_result = ft.Text("0", size=16, weight=ft.FontWeight.BOLD)
        
        self.build_ui()
    
    def build_ui(self):
        self.controls = [
            ft.Row([
                ft.Text("MODELO PROBABILISTICO", size=24, weight=ft.FontWeight.BOLD),
                ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=self.volver_menu)
            ]),
            ft.Container(height=20),
            
            ft.Row([
                ft.Column([
                    self.demanda_field,
                    self.varianza_field,
                    self.z_field,
                ]),
                ft.Column([
                    self.costo_pedido_field,
                    self.costo_mantenimiento_field,
                    self.lead_time_field,
                ]),
            ]),
            
            ft.Container(height=20),
            
            ft.ElevatedButton("Calcular", on_click=self.calcular,
                             style=ft.ButtonStyle(bgcolor=ft.Colors.CYAN_100)),
            
            ft.Container(height=20),
            
            ft.Column([
                ft.Row([ft.Text("Lote economico (Q):"), self.q_result]),
                ft.Row([ft.Text("Punto de reorden (PR):"), self.pr_result]),
            ]),
        ]
    
    def calcular(self, e):
        try:
            D = float(self.demanda_field.value)
            varianza = float(self.varianza_field.value)
            Z = float(self.z_field.value)
            S = float(self.costo_pedido_field.value)
            H = float(self.costo_mantenimiento_field.value)
            L = float(self.lead_time_field.value)
            
            # Calcular Q
            Q = formulario.Q(D, S, H, 0, 1)
            
            # Calcular punto de reorden
            demanda_lead_time = D * L
            desviacion = math.sqrt(varianza * L)
            stock_seguridad = Z * desviacion
            PR = demanda_lead_time + stock_seguridad
            
            self.q_result.value = f"{Q:.2f}"
            self.pr_result.value = f"{PR:.2f}"
            
        except ValueError:
            self.q_result.value = "Error en los datos ingresados"
            self.pr_result.value = "Error en los datos ingresados"
        
        self.page.update()
    
    def volver_menu(self, e):
        from menu_principal import MenuPrincipal
        self.page.clean()
        menu = MenuPrincipal(self.page)
        self.page.add(menu)
        self.page.update()