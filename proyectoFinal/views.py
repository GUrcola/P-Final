from django.http import HttpResponse
from django.template import Context, Template, loader
from mercaderia.models import producto

def crear_producto(request, tipo, modelo):
    
    Producto= producto(tipo= tipo ,modelo= modelo)
    Producto.save()
    template = loader.get_template("crear_producto.html")
    template_renderizado = template.render({"Producto": Producto})
    
    return HttpResponse(template_renderizado)


def ver_producto(request):
    
    productos=producto.objects.all()
    
    template = loader.get_template("ver_producto.html")
    template_renderizado = template.render({"productos": productos})
    
    return HttpResponse(template_renderizado)