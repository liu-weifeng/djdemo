from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=255)
    except_num = models.IntegerField()

    class Meta:
        db_table = 'department'


class Employee(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    department = models.ForeignKey(Department)

    class Meta:
        db_table = 'employee'


class Article(models.Model):
    category = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.FloatField()

    class Meta:
        db_table = 'article'


class Application(models.Model):
    emp = models.ForeignKey(Employee)
    article = models.ForeignKey(Article)
    count = models.IntegerField()

    class Meta:
        db_table = 'application'
