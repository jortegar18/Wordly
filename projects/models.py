from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, username, name, genre, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given username, name, email, genre, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
            date_of_birth=date_of_birth,
            name=name,
            genre=genre,
            email=email,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, name, genre, email, date_of_birth, password=None):
        """
        Creates and saves a superuser with the given username, name, email, genre, date of
        birth and password.
        """
        user = self.create_user(
            username,
            date_of_birth=date_of_birth,
            name=name,
            genre=genre,
            email=email,

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
    genre = models.CharField(
        max_length=255,
    )
    email = models.EmailField()
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name','genre', 'email','date_of_birth']

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