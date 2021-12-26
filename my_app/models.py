from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return 'images/{0}/'.format(filename)


# Create your models here.
