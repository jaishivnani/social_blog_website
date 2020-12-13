from django.db.models.signal import post_save
from django.contrib.auth.models import User
from django.dispath import receiver
from . models import Profile


def created_profile