from django import forms
from .models import Participant, Task, Module


class ParticipantForm(forms.ModelForm):
    task = forms.ModelChoiceField(queryset=Task.objects.all(), required=True, label="Выберите задание")

    class Meta:
        model = Participant
        fields = ['name', 'email', 'task']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваше имя'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите вашу электронную почту'})
        }
        labels = {
            'name': 'Имя',
            'email': 'Электронная почта',
            'task': 'Задание'
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Participant.objects.filter(email=email).exists():
            raise forms.ValidationError("Участник с таким адресом электронной почты уже существует.")
        return email


class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['title', 'description']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название модуля'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание модуля'})
        }
        labels = {
            'title': 'Название модуля',
            'description': 'Описание модуля'
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['module', 'title', 'description', 'skills']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название задания'}),
            'skills': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите необходимые знания'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание задания'})
        }
        labels = {
            'title': 'Название задания',
            'description': 'Описание задания',
            'skills': 'Необходимые знания',
            'module': 'Модуль задания'
        }



