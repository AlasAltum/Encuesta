from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.points = 10
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.points = 1000
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.points = 1000
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    points = models.IntegerField(
        verbose_name='points',
        default=1,
    )
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)

    def get_full_name(self):
        return self.email

    def __str__(self):
        return self.email

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    objects = UserManager()


class Survey(models.Model):
    finished = models.BooleanField(verbose_name='finished', default=False)
    link = models.URLField(verbose_name='link_encuesta', max_length=1024)
    name = models.CharField(verbose_name='nombre_encuesta', max_length=100)
    avg_duration = models.FloatField(verbose_name='duracion_promedio', default=5.0)
    prize = models.CharField(verbose_name='premio', default='', max_length=200)
    created_at = models.DateTimeField(verbose_name='fecha_de_creacion', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='fecha_ultima_actualizacion', auto_now=True)

