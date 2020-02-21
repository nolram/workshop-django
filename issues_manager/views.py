from django.contrib.auth.decorators import login_required

from django.http import HttpResponse


@login_required(login_url='/accounts/login/')
def pagina_inicial(request):
    # GET, POST, PUT, DELETE, PATCH
    return HttpResponse("Hello World")
