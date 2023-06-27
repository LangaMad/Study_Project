from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """

        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)

class Teacher(AbstractUser):
    username = models.CharField('ФИО препадователя', max_length=100 , unique= True)
    email = models.EmailField('Почта препадователя', unique=True)
    teacher_subject = models.CharField("Предмет", max_length=15,unique=True)
    phone = models.CharField(
        'Номер Телефона',
        null=True,
        max_length=10
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Учитель"
        verbose_name_plural ="Учителя"


    objects = UserManager()



class Classroom(models.Model):
    name = models.CharField('Название класса', max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete= models.CASCADE , related_name='classes')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Класс"
        verbose_name_plural ="Классы"


class Student (models.Model):
    name = models.CharField('Имя', max_length=100)
    email = models.EmailField('Почта',unique=True)
    surname = models.CharField('Фамилия', max_length=100)
    father_name = models.CharField('Отчество', max_length=100)
    birth_d = models.DateField('День Рождения')
    student_class = models.ForeignKey(Classroom,on_delete=models.CASCADE, related_name='student_class')
    address = models.CharField('Адрес', max_length=100)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    photo = models.ImageField(upload_to='student_photos', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Ученик"
        verbose_name_plural ="Ученики"







class School(models.Model):
    name = models.CharField('Название Школы', max_length=100)
    classrooms = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='school_class')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Школа"
        verbose_name_plural = "Школы"





