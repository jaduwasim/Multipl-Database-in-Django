from django.db import models

# Create your models here.
class MongoAppModel(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'MongDBTable'
        app_label = 'mongoapp'