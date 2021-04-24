from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.TextField(max_length=100)
    email = models.EmailField()
    mobile = models.TextField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Person"

class Adhar(models.Model):
    person = models.OneToOneField("Person",on_delete=models.CASCADE)
    signature = models.TextField()
    adhar_no = models.TextField(max_length=100)

    def __str__(self):
        return self.adhar_no

    class Meta:
        db_table = "Adhar"