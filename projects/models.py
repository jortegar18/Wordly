from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, username, name, last_name, genre, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given username, name, email, genre, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
            name=name,
            last_name=last_name,
            genre=genre,
            email=email,
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, name, last_name, genre, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given username, name, email, genre, date of
        birth and password.
        """
        user = self.create_user(
            username=username,
            name=name,
            last_name=last_name,
            genre=genre,
            email=email,
            date_of_birth=date_of_birth, 
            password=password,              
        )
        
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(
        verbose_name='username',
        max_length=255,
        unique=True,
    )
    name = models.CharField(
        max_length=255,
    )
    last_name = models.CharField(
        max_length=255,
    )
    genre = models.CharField(
        max_length=255,
    )
    email = models.EmailField()
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)


    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name','last_name', 'genre', 'email','date_of_birth']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
class Tutor(MyUser):
    EXPERIENCE_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
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
    PAYMENT_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
    ]

    experience = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES)
    languages = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    payment_methods = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    availability = models.TextField()
