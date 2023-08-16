class Carro:
    
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"]={}
        self.carro = carro
    
    def agregar(self, producto):
        if (str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={
                "Producto_id":producto.id,
                "Nombre":producto.Nombre,
                "Precio":producto.Precio,
                "Cantidad":1,
                "Imagen":producto.Imagen.url,
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["Cantidad"]=value["Cantidad"]+1
                    value["Precio"]=float(value["Precio"]+producto.Precio)
                    break
        self.guardar_carro()
        
    def guardar_carro(self):
        self.session["carro"]= self.carro
        self.session.modified= True
        
    def eliminar(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()
            
    def restar_producto(self, producto):
        for key, value in self.carro.items():
                if key == str(producto.id):
                    value["Cantidad"]=value["Cantidad"]-1
                    value["Precio"]=float(value["Precio"]-producto.Precio)
                    if value["Cantidad"] < 1:
                        self.eliminar(producto)
                    break
        self.guardar_carro()
        
    def limpiar_carro(self):
        carro = self.session["carro"]={}
        self.guardar_carro()
         ## Video 53 ##Ñ