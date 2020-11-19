from django import forms
import datetime
from .models import Project


class TaskAddForm(forms.Form):
    name = forms.CharField(max_length=255)
    descr = forms.CharField(required=False)
    added_date = forms.DateField(initial=datetime.date.today(), required=False)
    end_date = forms.DateField(initial=(datetime.date.today() + datetime.timedelta(weeks=2)), required=False)
    project_id = forms.ModelChoiceField(queryset=Project.objects.all())
