from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

from rest_framework import viewsets

from utils import mixins

from .forms import IssueForm
from .models import Issue
from .serializers import IssuesSerializer
from .filters import FilterIssues


@login_required(login_url='/accounts/login/')
def pagina_inicial(request):
    issues = Issue.objects.all()
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


# Django Rest Framework
class IssuesViewSet(mixins.DefaultMixin, viewsets.ModelViewSet):
    queryset = Issue.objects.all().order_by('-date_update')
    serializer_class = IssuesSerializer
    pagination_class = mixins.StandartResultsSetPagination
    filter_class = FilterIssues
