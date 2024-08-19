import tkinter as tk
from tkinter import messagebox, simpledialog
from Maquina__ExpendedoramjF import *
from ConexionBD import *

class InterfazMaquina:
    def __init__(self, root):
        self.root = root
        self.root.title("Máquina Expendedora")
        self.root.attributes('-fullscreen', True)
        self.root.bind("<Escape>", self.quit_fullscreen)

        self.db_connection = conexionBD()
        if self.db_connection is None:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos.")
            self.root.quit()

        self.maquina = MaquinaExpendedora("Vending machine", self.db_connection)
        self.create_widgets()

    def create_widgets(self):
        # Crear frames
        self.frame_main = tk.Frame(self.root, bg='#f0f0f0')
        self.frame_main.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.frame_product_selection = tk.Frame(self.root, bg='#f0f0f0')
        self.frame_product_selection.pack(fill=tk.BOTH, expand=True)
        self.frame_product_selection.pack_forget()

        # Widgets de login
        self.label_matricula = tk.Label(self.frame_main, text="Ingrese su matrícula:", font=("Arial", 18), bg='#f0f0f0')
        self.label_matricula.pack(pady=20)
        
        self.entry_matricula = tk.Entry(self.frame_main, font=("Arial", 18))
        self.entry_matricula.pack(pady=10)
        
        self.button_login = tk.Button(self.frame_main, text="Iniciar sesión", command=self.login, font=("Arial", 18), bg='#4CAF50', fg='white', width=20, height=2)
        self.button_login.pack(pady=20)

        self.button_view_sales = tk.Button(self.frame_main, text="Ver registros de ventas", command=self.view_sales, font=("Arial", 18), bg='#2196F3', fg='white', width=20, height=2)
        self.button_view_sales.pack(pady=20)
        
        # Widgets de selección de producto
        self.label_product_list = tk.Label(self.frame_product_selection, text="VENDING MACHINE", font=("monocraft", 28), bg='#f0f0f0')
        self.label_product_list.pack(pady=20)
        
        self.text_product_list = tk.Text(self.frame_product_selection, height=20, width=80, font=("Arial", 14))
        self.text_product_list.pack(pady=20)
        
        self.entry_product_code = tk.Entry(self.frame_product_selection, font=("Arial", 18))
        self.entry_product_code.pack(pady=10)
        
        self.button_select_product = tk.Button(self.frame_product_selection, text="Seleccionar producto", command=self.select_product, font=("Arial", 18), bg='#4CAF50', fg='white', width=20, height=2)
        self.button_select_product.pack(pady=20)
        
        self.button_logout = tk.Button(self.frame_product_selection, text="Cerrar sesión", command=self.logout, font=("Arial", 18), bg='#f44336', fg='white', width=20, height=2)
        self.button_logout.pack(pady=20)

    def login(self):
        matricula = self.entry_matricula.get().strip().upper()
        if not self.maquina.buscar_estudiante(matricula):
            messagebox.showerror("Error", "Matrícula no registrada.")
        else:
            self.frame_main.pack_forget()
            self.frame_product_selection.pack(fill=tk.BOTH, expand=True)
            self.update_product_list()

    def logout(self):
        self.frame_product_selection.pack_forget()
        self.frame_main.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.entry_matricula.delete(0, tk.END)

    def update_product_list(self):
        self.text_product_list.delete(1.0, tk.END)
        for producto in self.maquina.lista_productos:
            self.text_product_list.insert(tk.END, f"{producto.nombre}\nCodigo: {producto.codigo}\nPrecio: ${producto.precio}\nStock: {producto.stock}\n\n")

    def select_product(self):
        codigo_producto = self.entry_product_code.get().strip().upper()
        producto = self.maquina.seleccionar_producto(codigo_producto)
        if producto:
            valor_moneda = simpledialog.askinteger("Ingreso de moneda", f"Introduce el valor de la moneda (5 o 10):")
            if valor_moneda not in [5, 10]:
                messagebox.showerror("Error", "Moneda no aceptada.")
                return
            moneda = Moneda(valor_moneda)
            self.maquina.ingresar_moneda(moneda)

            total_insertado = valor_moneda
            while total_insertado < producto.precio:
                valor_moneda = simpledialog.askinteger("Ingreso de moneda", f"Total insertado: ${total_insertado}. Introduce el valor de la moneda (5 o 10):")
                if valor_moneda not in [5, 10]:
                    messagebox.showerror("Error", "Moneda no aceptada.")
                    continue
                moneda = Moneda(valor_moneda)
                self.maquina.ingresar_moneda(moneda)
                total_insertado += moneda.getValor()

            producto_entregado = self.maquina.entregar_producto(producto, self.entry_matricula.get().strip().upper())
            cambio = total_insertado - producto.precio
            if producto_entregado:
                messagebox.showinfo("Éxito", f"Producto entregado: {producto_entregado.nombre}\nCambio devuelto: ${cambio}")
            else:
                messagebox.showwarning("Advertencia", "No se pudo completar la transacción.")
                if cambio > 0:
                    self.maquina.monedero.devolver_cambio()
                    messagebox.showinfo("Cambio", f"Se devolvió el dinero insertado: ${cambio}")
                else:
                    messagebox.showwarning("Advertencia", "No se insertó suficiente dinero.")
        else:
            messagebox.showerror("Error", "Producto no encontrado o fuera de stock.")

    def view_sales(self):
        ventas = fetch_all(self.db_connection, "SELECT * FROM ventas")
        ventas_text = "Ventas realizadas:\n\n"
        for venta in ventas:
            id_venta = venta[0]  
            fecha = venta[1]
            hora = venta[2]
            matricula = venta[3]
            codigo = venta[4]
            ventas_text += f"ID: {id_venta}, Fecha: {fecha}, Hora: {hora}, Matrícula: {matricula}, Código: {codigo}\n"
        
        messagebox.showinfo("Registros de ventas", ventas_text)

    def quit_fullscreen(self, event=None):
        self.root.attributes('-fullscreen', False)

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazMaquina(root)
    root.mainloop()


