from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save


class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, email, password, **extra_fields):
        user = self.model( email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)



class User(AbstractUser):

    first_name = models.CharField('First Name',max_length=255, blank=True, null=True)
    last_name = models.CharField('Last Name',max_length=255, blank=True, null=True)
    avatar = models.ImageField('Avatar', upload_to='user/avatars',blank=True,null=True)
    email = models.EmailField('Email', blank=True, null=True, unique=True)
    username = models.CharField('Username',max_length=255, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return '{id}: {user}'.format(id=self.id, user=self.email)

    def get_avatar(self):
        if self.avatar:
            return self.avatar.url
        else:
            return '/media/no-avatar.svg'


