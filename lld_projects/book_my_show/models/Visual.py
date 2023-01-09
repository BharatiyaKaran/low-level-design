from django.db import models


class Visual(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
