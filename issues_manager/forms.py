from django import forms

from .models import Issue


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ["description", "is_open"]


class SearchForm(forms.Form):
    search = forms.CharField(max_length=255)
    is_open = forms.BooleanField(required=False)
