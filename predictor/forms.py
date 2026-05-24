# predictor/forms.py

from django import forms

class StudentForm(forms.Form):
    GPA_previous = forms.FloatField(
        label="Средний балл за прошлый период (2.0–5.0)",
        min_value=2.0, max_value=5.0,
        widget=forms.NumberInput(attrs={'step': '0.1', 'class': 'form-control'})
    )
    attendance = forms.IntegerField(
        label="Посещаемость (%)",
        min_value=50, max_value=100,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    study_hours = forms.FloatField(
        label="Часы самостоятельных занятий в неделю (0–30)",
        min_value=0, max_value=30,
        widget=forms.NumberInput(attrs={'step': '0.5', 'class': 'form-control'})
    )
    assignments_done = forms.IntegerField(
        label="Выполненные домашние задания (0–10)",
        min_value=0, max_value=10,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    previous_prep = forms.ChoiceField(
        label="Уровень предыдущей подготовки",
        choices=[(0, 'Низкий'), (1, 'Средний'), (2, 'Высокий')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )