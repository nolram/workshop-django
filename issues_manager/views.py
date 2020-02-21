from django.http import HttpResponse

# Create your views here.
def pagina_inicial(request):
    # GET, POST, PUT, DELETE, PATCH
    return HttpResponse("Hello World")
