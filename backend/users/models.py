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
        Create and save a SuperUser with the given email and password.
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
    teacher_subject = models.CharField("Предмет", max_length=15,unique=True)
    teacher_class = models.CharField("Класс", unique=True)
    phone = models.CharField(
        'Номер Телефона',
        null=True,
        max_length=10
    )


    class Meta:
        verbose_name="Учитель"
        verbose_name_plural ="Учителя"


    objects = UserManager()



class Student (models.Model):
    name = models.CharField('Имя', max_length=100)
    surname = models.CharField('Фамилия', max_length=100)
    father_name = models.CharField('Отчество', max_length=100)
    birth_d = models.DateField('День Рождения')
    student_class = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    address = models.CharField('Адрес', max_length=100)
    GENDER_CHOICES = (
        ('M', 'Мужской'),
        ('F', 'Женский'),
    )
    photo = models.ImageField('Фото', upload_to='student_photos', blank=True)



    class Meta:
        verbose_name="Ученик"
        verbose_name_plural ="Ученики"


class Classroom(models.Model):
    name = models.CharField('Название класса', max_length=100)
    teacher = models.OneToOneField(Teacher, on_delete= models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)

    class Meta:
        verbose_name="Класс"
        verbose_name_plural ="Классы"


class School(models.Model):
    name = models.CharField('Название Школы', max_length=100)
    classrooms = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Школа"
        verbose_name_plural = "Школы"





