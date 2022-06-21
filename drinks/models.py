from typing import List
from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name + " : " + self.description

class Sentence(models.Model):
    sentence= models.CharField(max_length=200)
    page_number=models.CharField(max_length=200)


class Section(models.Model):
    section = models.CharField(max_length=200)
    sentences = models.ManyToManyField(Sentence)


