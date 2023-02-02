def upload_avatar_path(instance, image):
    return f'users/{instance.USERNAME_FIELD}/{image}'


def upload_resume_path(instance, resume):
    return f'users/{instance.USERNAME_FIELD}/{resume}'


def upload_tariff_path(instance, logo):
    return f'tariff/{instance.name}/{logo}'

def upload_product_path(instance, image):
    return f'products/{instance.author.USERNAME_FIELD}/{instance.title}/{image}'
