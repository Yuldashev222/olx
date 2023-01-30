def upload_avatar_path(instance, image):

    return f'user/{instance.email}/{image}'

def upload_resume_path(instance, resume):

    return f'user/{instance.email}/{resume}'

def upload_tariff_path(instance, logo):

    return f'tariff/{instance.name}/{logo}'