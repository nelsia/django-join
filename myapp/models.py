from django.db import models


class Record(models.Model):
  phone_number = models.CharField(max_length=15)


class Customer(models.Model):
  phone_number = models.CharField(max_length=15)
  customer_name = models.CharField(max_length=100)
