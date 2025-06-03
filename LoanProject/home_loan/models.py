from django.db import models

# Create your models here.
class HomeLoanUser(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        app_label = 'home_loan'