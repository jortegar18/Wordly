from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.core.validators import MaxValueValidator

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
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    # Type Identification for all users
    user_type = models.CharField(max_length=100)    
    birthday = models.DateField(default=timezone.now, null=True)
    # Fields for tutor

    # Fields for student
   
    def __str__(self):
        return str(self.name)
    
class Tutor(CustomUser):

    description = models.CharField(max_length=250, default='')
    payment = models.IntegerField(default='0000000000000000')
    expire_date = models.DateField(default=timezone.now, null=True)
    ccv = models.IntegerField(validators=[MaxValueValidator(999)], null=True)

class Student(CustomUser):

    #profile_picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
     
    payment = models.IntegerField(default='0000000000000000')
    expire_date = models.DateField(default=timezone.now, null=True)
    ccv = models.IntegerField(validators=[MaxValueValidator(999)], null=True)

class Work_Experience(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    company = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
    lenght = models.IntegerField()

class Paymenth_Method(models.Model):
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    number = models.IntegerField()
    expire_date = models.DateField()
    ccv = models.IntegerField(validators=[MaxValueValidator(999)])

    def get_expire_date(self, obj):
        return obj.expire_date.strftime("%Y-%m")

class Session(models.Model):

    date = models.DateTimeField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.CharField(max_length=200)

   
    SESSION_STATUS = [
        (0, "En espera"),
        (1, "Aprobado"),
        (2, "Rechazado"),
    ]
    
    status = models.IntegerField(choices = SESSION_STATUS, default = 0)
    
    # Foreign Keys and Relationships

    tutor = models.ForeignKey(Tutor, on_delete=models.DO_NOTHING, related_name="Tutor")    
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, related_name="Student")

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