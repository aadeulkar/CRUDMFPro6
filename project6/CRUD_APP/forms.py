from django import forms
from . models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'sid' : 'STUDENT ID',
            'fname': 'FULL NAME',
            'dob': 'DATE OF BIRTH',
            'mail':'EMAIL ADDRESS',
            'city': 'CITY'
        }

        widgets = {
            'sid': forms.NumberInput(attrs={'class': 'form-control'}),
            'fname': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'placeholder': 'eg. VIRAT N KOHLI'}),
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'mail': forms.EmailInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'})
        }
