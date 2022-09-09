# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Testimonial(models.Model):

    text = models.TextField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    affiliation = models.CharField(max_length=100, blank=True)
    added = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)
