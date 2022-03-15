from django.conf import settings
from django.db import models


class Testapps(models.Model):
    "Generated Model"
    oktested = models.TextField(
        blank=True,
    )
    newtestss = models.URLField(
        blank=True,
    )
