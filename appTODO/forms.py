# Create your models form here
from django.contrib.auth.models import User
from django.forms import ModelForm, ModelChoiceField
from .models import Task


class TaskForm(ModelForm):
    created_by = ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = Task
        fields = ['created_by', 'title', 'status', 'description','completed','completed_at']
