from django.db import models

# Create your models here.
class MysqlAppModel(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'MysqlDBTable'
        app_label = 'mysqlapp'