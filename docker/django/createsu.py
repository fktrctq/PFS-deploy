from django.db import IntegrityError
from django.contrib.auth.models import User
import os

try:
    if not User.objects.filter(is_superuser=True).exists():
        superuser = User.objects.create_superuser(
            username=os.environ.get('DJANGO_SUPERUSER_USERNAME', 'sber'),
            email=os.environ.get('DJANGO_SUPERUSER_EMAIL', 'sber@sber.ru'),
            password=os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'sber'))
        superuser.save()
        print(f'A superuser "{os.environ.get('DJANGO_SUPERUSER_USERNAME')}" has been created!!!')
    else:
        print(f'The superuser "{os.environ.get('DJANGO_SUPERUSER_USERNAME')}" already exists!') 
except IntegrityError:
    print(f'The superuser "{os.environ.get('DJANGO_SUPERUSER_USERNAME')}" already exists!')
except Exception as e:
    print(e)