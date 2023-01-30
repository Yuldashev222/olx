from django.dispatch import receiver
from django.db.models.signals import pre_delete
from django.forms import model_to_dict
from .models import CustomUser, UserDataOnDelete

@receiver(pre_delete, sender=CustomUser)

def save_user_data_on_delete(instance, *args, **kwargs):
    deliveries = instance.delivery_user.all()

    user_data = UserDataOnDelete.objects.create(
        **model_to_dict(instance, fields=[
            'first_name', 'last_name', 'email'
        ]))
    
    if deliveries.exists():
        deliveries.update(author_id=user_data.id)
