from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.core.validators import MaxValueValidator
from cloudinary.models import CloudinaryField
from issimplecrud.settings import CLOUDINARY_ROOT_URL

# Create your models here.

class CustomUser(AbstractUser):

    first_name = None

    

    MALE = "M"
    FEMALE = "F"
    OTHER = "O"
    GENDER_CHOICES = [
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other")
        ]

    class Meta:
        
        verbose_name = 'User'
    username = models.CharField(max_length=40, unique=True, default='')
    email = models.EmailField(max_length=254, unique=True)
    is_verified = models.BooleanField(default=True)
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    # Type Identification for all users
    user_type = models.CharField(max_length=100)    
    birthday = models.DateField(default=timezone.now, null=True)
    description = models.CharField(max_length=250)
    profile_picture = CloudinaryField(resource_type='image', null=True)
    file = CloudinaryField(resource_type='auto', null=True)
    video = CloudinaryField(resource_type = 'video', null = True)
    cost = models.CharField(max_length=256, null=True)

    # Fields for tutor

    # Fields for student
    
    
    
    def __str__(self):
        return str(self.email)
    

    
    
    
class Tutor(CustomUser):

    
    
    payment = models.CharField(max_length=16, default='0000000000000000', null=True)
    expire_date = models.DateField(default=timezone.now, null=True)
    ccv = models.IntegerField(validators=[MaxValueValidator(999)], null=True)

class Student(CustomUser):

    #profile_picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
     
    payment = models.CharField(max_length=16, default='0000000000000000', null=True)
    expire_date = models.DateField(default=timezone.now, null=True)
    ccv = models.IntegerField(validators=[MaxValueValidator(999)], null=True)

class Work_Experience(models.Model):

    tutor = models.ForeignKey(CustomUser, related_name='work_exp', on_delete=models.CASCADE)
    company = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
    lenght = models.IntegerField()

    def __str__(self):
        return '%s: %s: %s' % (self.company, self.position, self.lenght)

    

class Paymenth_Method(models.Model):
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    number = models.CharField(max_length=16, unique=True)

    expire_date = models.DateField()
    ccv = models.IntegerField(validators=[MaxValueValidator(999)])

    def get_expire_date(self, obj):
        return obj.expire_date.strftime("%Y-%m")

class Session(models.Model):

    date = models.DateTimeField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.CharField(max_length=200, null=True)
    calification = models.CharField(max_length=5, null = True)

   
    SESSION_STATUS = [
        (0, "En espera"),
        (1, "Aprobado"),
        (2, "Rechazado"),
    ]
    
    status = models.IntegerField(choices = SESSION_STATUS, default = 0)
    
    # Foreign Keys and Relationships

    tutor = models.ForeignKey(Tutor, on_delete=models.DO_NOTHING, related_name="Tutor")    
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, related_name="Student")

    def __str__(self):
        return '%s: %s: %s: %s' % (self.date, self.description, self.status, self.calification)

class StudentRequest(models.Model):

    SESSION_STATUS = [
        (0, "En espera"),
        (1, "Aprobado"),
        (2, "Rechazado"),
    ]
    status = models.IntegerField(choices=SESSION_STATUS, default=0)
    # Foreign keys and Relationships
    session = models.ForeignKey(
        Session, on_delete=models.CASCADE, related_name="SesionSolicitada")
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="EstudianteSolicitando", default=None)
    tutor = models.ManyToManyField(Tutor, related_name="TutorSolicitado")


class Language(models.Model):

    LANGUAGE_CHOICES = [
        ('english', 'English'),
        ('spanish', 'Spanish'),
        ('french', 'French'),
        ('german', 'German'),
        ('italian', 'Italian'),
        ('portuguese', 'Portuguese'),
        ('chinese', 'Chinese'),
        ('japanese', 'Japanese'),
        ('korean', 'Korean'),
        ('arabic', 'Arabic'),
        ('russian', 'Russian'),
    ]

    LANGUAGE_LEVEL = [
        ('a1', 'A1'),
        ('a2', 'A2'),
        ('b1', 'B1'),
        ('b2', 'B2'),
        ('c1', 'C1'),
        ('c2', 'C2')
    ]

    name = models.CharField(max_length=16, choices=LANGUAGE_CHOICES)
    level = models.CharField(max_length=20, choices=LANGUAGE_LEVEL)
    user = models.ForeignKey(CustomUser, related_name='languages', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return '%s: %s' % (self.name, self.level)
    
class Time_Av(models.Model):
    user = models.ForeignKey(CustomUser, related_name='availability', on_delete=models.CASCADE)
    day_of_week = models.IntegerField()  # 0 para lunes, 1 para martes, etc.
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return '%s: %s: %s' % (self.day_of_week, self.start_time, self.end_time)

class Calification(models.Model):

    user = models.ForeignKey(CustomUser, related_name='calification', on_delete=models.CASCADE)

    one = models.PositiveIntegerField(default=0, null=True, blank=True)
    two = models.PositiveIntegerField(default=0, null=True, blank=True)
    three = models.PositiveIntegerField(default=0, null=True, blank=True)
    four = models.PositiveIntegerField(default=0, null=True, blank=True)
    five = models.PositiveIntegerField(default=0, null=True, blank=True)

    class Meta:
        ordering = ['user']

    def __str__(self):
        # Extraiga todos los valores y devuelva el valor máximo.
        # Invierte este dictado si hay un empate y quieres la última clave.
        rating_list = {
            '1': self.one,
            '2': self.two,
            '3': self.three,
            '4': self.four,
            '5': self.five
        }
        return str(max(rating_list, key=rating_list.get))
    
