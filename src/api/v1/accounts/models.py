from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField

from api.v1.accounts.validators import validate_phone
from .servises import upload_avatar_path, upload_resume_path
from .enums import Licences


class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=13, blank=True, validators=[validate_phone])
    email = models.EmailField(unique=True)
    balance = models.FloatField(default=0)  # kamida 0 bolishi kerak

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    about = models.CharField(max_length=255, blank=True)
    birthdate = models.DateField(blank=True, null=True)
    avatar = models.ImageField(
        upload_to=upload_avatar_path,
        default='user/defaultuser/defaultuser.png'
    )
    other_skills = models.CharField(max_length=300, blank=True)
    hobby = models.CharField(max_length=300, blank=True)
    resume = models.FileField(upload_to=upload_resume_path, blank=True, null=True)

    # Education
    edu1_name = models.CharField(max_length=250, blank=True)
    edu1_direction = models.CharField(max_length=150, blank=True)
    edu1_start_date = models.DateField(blank=True, null=True)
    edu1_end_date = models.DateField(blank=True, null=True)
    edu1_now = models.BooleanField(default=False)

    edu2_name = models.CharField(max_length=250, blank=True)
    edu2_direction = models.CharField(max_length=150, blank=True)
    edu2_start_date = models.DateField(blank=True, null=True)
    edu2_end_date = models.DateField(blank=True, null=True)
    edu2_now = models.BooleanField(default=False)
    license_category = MultiSelectField(choices=Licences)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        if self.get_full_name():
            return self.get_full_name()
        return self.email


class Language(models.Model):
    LANGUAGE_CHOICE = (
        ('uz', 'Uzbek'),
        ('en', 'English'),
        ('gr', 'German'),
    )
    name = models.CharField(max_length=2, choices=LANGUAGE_CHOICE)


class UserLanguage(models.Model):
    LEVEL_CHOICE = [
        ('il', 'Ilg\'or'),
        ('bo', 'Boshlang\'ich'),
        ('er', 'Erkin'),
        ('or', 'O\'rta')
    ]
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    level = models.CharField(max_length=2, choices=LEVEL_CHOICE)


class Experience(models.Model):
    role = models.CharField(max_length=150)
    company_name = models.CharField(max_length=255)
    work_start_date = models.DateField()
    work_end_date = models.DateField(blank=True, null=True)
    work_now = models.BooleanField(default=False)
    work_duties = models.CharField(max_length=500, blank=True)

    user = models.ForeignKey(CustomUser, related_name='experiences', on_delete=models.CASCADE)
