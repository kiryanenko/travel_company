from django.db import models


class Resort(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    country = models.CharField(max_length=50, db_index=True)
