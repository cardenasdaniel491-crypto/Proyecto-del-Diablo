import flet as ft
import formulario

class Modelo_escases(ft.Column):    
    def __init__(self, page):
        super().__init__()
        self.page = page
        
        self.demanda_field = ft.TextField(label="Demanda (D)", width=200)
        self.costo_pedido_field = ft.TextField(label="Costo pedido (S)", width=200)
        self.costo_mantenimiento_field = ft.TextField(label="Costo Mantenimiento (H)", width=200)
        self.costo_escasez_field = ft.TextField(label="Costo Escasez (a)", width=200)
        self.dias_field = ft.TextField(label="Dias chambeados", width=200)
        
        self.q_result = ft.Text("0", size=16, weight=ft.FontWeight.BOLD)
        self.sm_result = ft.Text("0", size=16, weight=ft.FontWeight.BOLD)
        self.cta_result = ft.Text("0", size=16, weight=ft.FontWeight.BOLD)
        
        self.build_ui()
    
    def build_ui(self):
        self.controls = [
            ft.Row([
                ft.Text("MODELO CON ESCASES", size=24, weight=ft.FontWeight.BOLD),
                ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=self.volver_menu)
            ]),
            ft.Container(height=20),
            
            ft.Row([
                ft.Column([
                    self.demanda_field,
                    self.costo_pedido_field,
                    self.costo_mantenimiento_field,
                    self.costo_escasez_field,
                    self.dias_field,
                ]),
            ]),
            
            ft.Container(height=20),
            
            ft.ElevatedButton("Calcular", on_click=self.calcular,
                             style=ft.ButtonStyle(bgcolor=ft.Colors.CYAN_100)),
            
            ft.Container(height=20),
            
            ft.Column([
                ft.Row([ft.Text("Lote económico (Q):"), self.q_result]),
                ft.Row([ft.Text("Inventario maximo (Sm):"), self.sm_result]),
                ft.Row([ft.Text("Costo Total Anual (CTA):"), self.cta_result]),
            ]),
        ]
    
    def calcular(self, e):
        try:
            D = float(self.demanda_field.value)
            S = float(self.costo_pedido_field.value)
            H = float(self.costo_mantenimiento_field.value)
            a = float(self.costo_escasez_field.value)
            dias = float(self.dias_field.value)
            
            Q = formulario.Q(D, S, H, a, 2)  
            Sm = formulario.Sm(Q, D, a, S, H, 1) 
            
            # calcular costo total anual
            CTA = (D / Q) * S + H * (Sm / 2)
            
            self.q_result.value = f"{Q:.2f}"
            self.sm_result.value = f"{Sm:.2f}"
            self.cta_result.value = f"{CTA:.2f}"
            
        except ValueError:
            self.q_result.value = "Error en los datos ingresados"
            self.sm_result.value ="Error en los datos ingresados"
            self.cta_result.value = "Error en los datos ingresados"
        
        self.page.update()
    
    def volver_menu(self, e):
        from menu_principal import MenuPrincipal
        self.page.clean()
        menu = MenuPrincipal(self.page)
        self.page.add(menu)
        self.page.update()