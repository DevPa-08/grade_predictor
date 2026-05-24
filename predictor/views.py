# predictor/views.py

from django.shortcuts import render
from .forms import StudentForm
from .ml_utils import predict_score

def predict_view(request):
    result = None
    color = None
    message = None
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Получаем данные из формы
            gpa = form.cleaned_data['GPA_previous']
            attendance = form.cleaned_data['attendance']
            study_hours = form.cleaned_data['study_hours']
            assignments = form.cleaned_data['assignments_done']
            prep = int(form.cleaned_data['previous_prep'])

            print(f"Данные из формы: GPA={gpa}, Посещаемость={attendance}, Часы={study_hours}, ДЗ={assignments}, Подготовка={prep}")
            
            # Вызываем нашу ML-функцию
            result = predict_score(gpa, attendance, study_hours, assignments, prep)

            print(f"Прогноз модели: {result}")
            
            # Определяем цвет и сообщение
            if result >= 4.0:
                color = "green"
                message = "Высокая успеваемость ✅"
            elif result >= 3.0:
                color = "orange"
                message = "Средняя успеваемость, требуется внимание ⚠️"
            else:
                color = "red"
                message = "Группа риска, необходима поддержка 🔴"
    else:
        form = StudentForm()
    
    return render(request, 'predictor/predict.html', {
        'form': form,
        'result': result,
        'color': color,
        'message': message,
    })


