from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

# Create your views here.


def students(request):
    students = Student.objects.all().order_by('-id')
    return render(request, 'student.html', {
        'students': students
    })


def students_detail(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        try:
            student.name = request.POST['name']
            student.lastname = request.POST['lastname']
            student.save()
            return redirect('students')
        except ValueError:
            return render(request, 'student_detail.html', {
                'error': 'Escribe datos válidos',
            })
            
    return render(request, 'student_detail.html', {
        'student': student
    })


def students_create(request):
    if request.method == 'POST':
        try:
            input_id = request.POST['id']
            existing_student = Student.objects.filter(id=input_id).first()
            if existing_student:
                return render(request, 'student_create.html', {
                    'error': 'El ID ya existe en la base de datos'
                })

            student = Student(
                id=request.POST['id'],
                name=request.POST['name'],
                lastname=request.POST['lastname'])
            student.save()
            return redirect('students')
        except ValueError:
            return render(request, 'student_create.html', {
                'error': 'Escribe datos válidos'
            })
    return render(request, 'student_create.html')


def students_delete(request, id):
    if request.method == 'POST':
        student = get_object_or_404(Student, id=id)
        student.delete()
        return redirect('students')
