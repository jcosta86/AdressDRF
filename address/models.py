from django.db import models


class Country(models.Model):
    description = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.description


class State(models.Model):
    description = models.CharField(max_length=50, null=False, blank=False)
    id_coutry = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class City(models.Model):
    description = models.CharField(max_length=50, null=False, blank=False)
    id_state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class District(models.Model):
    description = models.CharField(max_length=50, null=False, blank=False)
    id_city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Address(models.Model):
    description = models.CharField(max_length=50, null=False, blank=False)
    id_city = models.ForeignKey(City, on_delete=models.CASCADE)
    number = models.IntegerField(null=False, blank=False)
    cep = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return f'{self.description} - cep {self.cep}'
