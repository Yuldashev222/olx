from random import randint
from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField
from django.core.validators import MinValueValidator
from languages.fields import LanguageField

from .validators import validate_phone
from .servises import upload_avatar_path, upload_resume_path
from .enums import Licences, LanguageLevel


class CustomUser(AbstractUser):
    __id = models.CharField(max_length=8, unique=True)
    username = None
    phone_number = models.CharField(max_length=13, blank=True, validators=[validate_phone])
    email = models.EmailField(unique=True, blank=True)
    balance = models.FloatField(default=0, validators=[MinValueValidator(0.0)])

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

    license_category = MultiSelectField(choices=Licences, blank=True)
    is_deleted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.__id = randint(10000000, 99999999)
        while CustomUser.objects.filter(__id=self.__id):
            self.__id = randint(10000000, 99999999)
        super().save(*args, **kwargs)

    def __str__(self):
        if self.get_full_name():
            return self.get_full_name()
        return self.email


class UserLanguage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    language = LanguageField()
    level = models.CharField(max_length=4 ,choices=LanguageLevel)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.language



class Experience(models.Model):
    role = models.CharField(max_length=150)
    company_name = models.CharField(max_length=255)
    work_start_date = models.DateField()
    work_end_date = models.DateField(blank=True, null=True)
    work_now = models.BooleanField(default=False)
    work_duties = models.CharField(max_length=500, blank=True)
    date_created = models.DateField(auto_now_add=True)

    user = models.ForeignKey(CustomUser, related_name='experiences', on_delete=models.CASCADE)

    def __str__(self):
        return self.role