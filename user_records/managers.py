from django.db import models

class PostgresModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().using('default')

class MongoDBModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().using('mongodb')
