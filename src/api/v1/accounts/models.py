from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField

from api.v1.accounts.validators import validate_phone
from .servises import upload_avatar_path, upload_resume_path


class CustomUser(AbstractUser):

    LICENSE_CHOICE = (
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
        ('b+e', 'B+E'),
        ('c+e', 'c+E'),
        ('d+e', 'D+E'),
        ('yoq', 'YOQ')
    )
    phone_number = models.CharField(max_length=13, unique=True, validators=[validate_phone])
    about = models.TextField()
    year_of_birth = models.DateField(blank=True ,null=True)
    avatar = models.ImageField(
        upload_to=upload_avatar_path,
        default='user/defaultuser/defaultuser.png')
    money = models.FloatField()
    other_skills = models.CharField(max_length=300)
    hobby = models.CharField(max_length=300)
    resume = models.FileField(upload_to=upload_resume_path, blank=True, null=True)

    # Education
    edu1_name = models.CharField(max_length=250)
    edu1_direction = models.CharField(max_length=150)
    edu1_start_date = models.DateField(blank=True ,null=True)
    edu1_end_date = models.DateField(blank=True ,null=True)
    edu1_now = models.BooleanField(default=False)
    
    edu2_name = models.CharField(max_length=250)
    edu2_direction = models.CharField(max_length=150)
    edu2_start_date = models.DateField(blank=True ,null=True)
    edu2_end_date = models.DateField(blank=True ,null=True)
    edu2_now = models.BooleanField(default=False)

    # Driver's license
    license_category = MultiSelectField(choices=LICENSE_CHOICE, default=LICENSE_CHOICE[7][0])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    


class UserDataOnDelete(models.Model):
    first_name = models.CharField('first_name', max_length=150)
    last_name = models.CharField('last_name', max_length=150)
    email = models.EmailField()
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Experience(models.Model):
    user = models.ForeignKey(CustomUser, related_name='experience_user' , on_delete=models.CASCADE)
    position_name = models.CharField(max_length=150)
    employer = models.CharField(max_length=150)
    work_start_date = models.DateField(blank=True ,null=True)
    work_end_date = models.DateField(blank=True ,null=True)
    work_now = models.BooleanField(default=False)
    work_duties = models.TextField()


class Language(models.Model):
    LANGUAGE_CHOICE = (
        ('uzbek', 'Uzbek'),
        ('english', 'English'),
        ('german', 'German'),
    )

    LEVEL_CHOICE = [
        ('ilg\'or', 'Ilg\'or'),
        ('boshlang\'ich', 'Boshlang\'ich'),
        ('erkin', 'Erkin'),
        ('o\'rta', 'O\'rta')
    ]

    user = models.ManyToManyField(CustomUser, related_name='language_user')
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICE, default=LANGUAGE_CHOICE[0][0])
    level = models.CharField(max_length=50, choices=LEVEL_CHOICE, default=LEVEL_CHOICE[3][3])

class DesiredJob(models.Model):
    REGION_CHOICE = (
        ('toshkent_shahri', 'Toshkent shahri'),
        ('surxondaryo', 'Surxondaryo')
    )

    DISTRICT_CHOICE = (
        ('olmazor', 'Olmazor'),
        ('chilonzor', 'Chilonzor')
        ('denov', 'Denov')
    )

    TIME_CHOICE = (
        ('butun', 'To\'liq stavkada bandlik'),
        ('yarim', 'To\'liq bo\'lmagan bandlik')
    )

    CONTRACT_CHOICE = (
        ('doimiy', 'Doimiy bandlik'),
        ('vaqtincha', 'Vaqtinchalik bandlik')
    )

    CHOICE_CURRENCY = (
        ('uzs', 'UZS'),
        ('usd', 'USD'),
    )

    WAGE_TIME_CHOICE = (
        ('soat', 'Har soatda'),
        ('oy', 'Har oyda')
    )
    
    user = models.OneToOneField(CustomUser, related_name='desireduser', on_delete=models.CASCADE)
    position = models.CharField(max_length=250)
    region = models.CharField(max_length=50, choices=REGION_CHOICE, default=REGION_CHOICE[0][0])
    district = models.CharField(max_length=50, choices=DISTRICT_CHOICE, default=DISTRICT_CHOICE[0][0])
    work_time = models.CharField(max_length=50, choices=TIME_CHOICE, default=TIME_CHOICE[0][0])
    contract = models.CharField(max_length=50, choices=CONTRACT_CHOICE, default=CONTRACT_CHOICE[0][0])
    min_wage = models.PositiveSmallIntegerField()
    currency = models.CharField(max_length=3, choices=CHOICE_CURRENCY, default=CHOICE_CURRENCY[0][0])
    wage_time = models.CharField(max_length=50, choices=WAGE_TIME_CHOICE, default=WAGE_TIME_CHOICE[0][0])