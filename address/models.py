from django.db import models


class Country(models.Model):
    description = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.description


