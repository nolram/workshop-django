from django_filters import FilterSet

from .models import Issue

class FilterIssues(FilterSet):
    class Meta:
        model = Issue
        fields = ['description', 'date_creation', 'date_update', 'user', 'is_open']