from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseRedirect

from .forms import IssueForm

from .models import Issues

from django.shortcuts import render

@login_required(login_url='/accounts/login/')
def pagina_inicial(request):
    issues = Issues.objects.all()
    return render(request, "index.html", {"issues": issues})

@login_required(login_url='/accounts/login/')
def issue_create_view(request):
    if request.method == "POST":
        form = IssueForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = IssueForm()

    return render(request, "form_issue.html", {"form": form})

