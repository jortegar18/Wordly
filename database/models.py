from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.deletion import CASCADE
from django.utils import timezone
from multiselectfield import MultiSelectField

# Create your models here.
class CustomUser(AbstractUser):
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
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    created_at = models.DateField(auto_now_add=True)
    # Type Identification for all users
    user_type = models.CharField(max_length=100)    
    birthday = models.DateField(default=timezone.now, null=True)
    # Fields for tutor

    # Fields for user
   
    def __str__(self):
        return str(self.name)
    
class Tutor(CustomUser):
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
    description = models.CharField(max_length=250, default='')
    language = MultiSelectField(choices=LANGUAGE_CHOICES,
                                 max_choices=3,
                                 max_length=10)
    payment = models.IntegerField(default='0000000000000000')

class Student(CustomUser):
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

    level = models.CharField(max_length=20, choices=LANGUAGE_LEVEL)
    
    language = models.CharField(choices=LANGUAGE_CHOICES,
                                 max_length=16)
    payment = models.IntegerField(default='0000000000000000')

class Work_Experience(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    company = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
    lenght = models.IntegerField()

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

    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name="Tutor")    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="Student")

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