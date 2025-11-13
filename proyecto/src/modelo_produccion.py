import flet as ft 
import formulario

class Modelo_produccion(ft.Column):
    def __init__(self, page):   
        super().__init__()
        self.page = page

        # campos de entrada para los parámetros del modelo de producción
        self.s_field = ft.TextField(label="Costo de produccion (S)", width=200)
        self.d_field = ft.TextField(label="Demanda (D)", width=200)
        self.h_field = ft.TextField(label="Costo de Mantenimiento (H)", width=200)
        self.t_field = ft.TextField(label="Dias trabajados", width=200)
        self.a_field = ft.TextField(label="Tasa de produccion (A)", width=200)

        self.q_resultado = ft.Text("0", size=16, weight=ft.FontWeight.BOLD)
        self.sm_resultado = ft.Text("0", size=16, weight=ft.FontWeight.BOLD)
        self.cta_resultado = ft.Text("0", size=16, weight=ft.FontWeight.BOLD)
        self.ctu_resultado = ft.Text("0", size=16, weight=ft.FontWeight.BOLD)
        self.t1_resultado = ft.Text("0", size=16, weight=ft.FontWeight.BOLD)
        self.build_ui()

    def build_ui(self):
        self.controls = [
            ft.Row([
                ft.Text("MODELO DE PRODUCCIÓN", size=24, weight=ft.FontWeight.BOLD),
                ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=self.volver_menu)
            ]),
            ft.Container(height=20),
            
            ft.Row([
                ft.Column([self.s_field, self.d_field, self.h_field]),
                ft.Column([self.t_field, self.a_field])
            ]),
            
            ft.Container(height=20),
            
            ft.Row([
                ft.ElevatedButton("Calcular", on_click=self.calcular,
                                 style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_100)),
                ft.ElevatedButton("Limpiar", on_click=self.limpiar,
                                 style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_100))
            ]),
            
            ft.Container(height=20),
            
            ft.Column([
                ft.Row([ft.Text("Lote econonico (Q):"), self.q_result]),
                ft.Row([ft.Text("Inventario maximo (Sm):"), self.sm_result]),
                ft.Row([ft.Text("Costo Total Anual(CTU):"), self.cta_result]),
                ft.Row([ft.Text("Tiempo producción (t1):"), self.t1_result]),
            ]),
        ]

    def calcular(self, e):
        try:
            S = float(self.s_field.value)
            D = float(self.d_field.value)
            H = float(self.h_field.value)
            t = float(self.t_field.value)
            A = float(self.a_field.value)
            
            Q = formulario.Q(D, S, H, A, 3) 
            Sm = formulario.Sm(Q, D, A, S, H, 2)  
            t1 = formulario.t1(Q, D, A, 2)  
            
            # se calcula el costo total anual
            CTA = (D / Q) * S + H * (Sm / 2)
            
            self.q_result.value = f"{Q:.2f}"
            self.sm_result.value = f"{Sm:.2f}"
            self.cta_result.value = f"{CTA:.2f}"
            self.t1_result.value = f"{t1:.2f}"
            
        except ValueError:
            self.q_result.value = "Error en los datos ingresados"
            self.sm_result.value = "Error en los datos ingresados"
            self.cta_result.value = "Error en los datos ingresados"
            self.t1_result.value = "Error en los datos ingresados"
        
        self.page.update()
    
    def limpiar(self, e):
        self.s_field.value = ""
        self.d_field.value = ""
        self.h_field.value = ""
        self.t_field.value = ""
        self.a_field.value = ""
        self.q_result.value = "0"
        self.sm_result.value = "0"
        self.cta_result.value = "0"
        self.t1_result.value = "0"
        self.page.update()
    
    def volver_menu(self, e):
        from menu_principal import MenuPrincipal
        self.page.clean()
        menu = MenuPrincipal(self.page)
        self.page.add(menu)
        self.page.update()