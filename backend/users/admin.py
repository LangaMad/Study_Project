from django.contrib import admin

# Register your models here.
from .models import Teacher , Student , Classroom,School
# Register your models here.

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'teacher_subject',
        'phone',


    ]



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'surname',
        'email',
        'father_name',
        'birth_d',
        'student_class',
        'address',
        'GENDER_CHOICES',
        'photo',


    ]


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'teacher',




    ]

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'classrooms',



    ]


