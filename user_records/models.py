from django.db import models
from djongo import models as djongo_models
from .managers import PostgresModelManager, MongoDBModelManager

# PostgreSQL Model
class User(models.Model):
    objects = PostgresModelManager()
    username = models.CharField(null=False, max_length=255, unique=True)
    password = models.CharField(null=False, max_length=255)

# MongoDB Model
class Product(djongo_models.Model):
    objects = MongoDBModelManager()
    name = models.CharField(null=True, blank=True, max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(null=True, blank=True)
