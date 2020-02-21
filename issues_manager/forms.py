from django import forms

from .models import Issues


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issues
        fields = ["description", "is_open"]
