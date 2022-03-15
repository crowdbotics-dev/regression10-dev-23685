from django.conf import settings
from django.db import models


class Testapps(models.Model):
    "Generated Model"
    oktested = models.TextField()
    newtest = models.URLField()
