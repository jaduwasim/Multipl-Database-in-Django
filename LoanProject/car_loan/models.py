from django.db import models

# Create your models here.
class CarLoanUser(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        app_label = 'car_loan'