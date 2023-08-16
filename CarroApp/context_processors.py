from .Carro import Carro

def import_total_carro(request):
    carro = Carro(request)
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total = total + float(value["Precio"])
    return {'Importe_Total_Carro': total}
    