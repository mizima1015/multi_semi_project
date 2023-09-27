from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class TestCsv_Subway(models.Model):
    SW_ID = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9)], blank=True, null=True)
    SW_Station = models.CharField(max_length=100, blank=True, null=True)
    SW_Num = models.IntegerField(validators=[MinValueValidator(1)], blank=True, null=True)

class Selection_Result(models.Model):
    Station_ON = models.TextField(max_length=100, blank=False)
    Station_OFF = models.TextField(max_length=100, blank=False)
    Get_Time = models.IntegerField(validators=[MinValueValidator(00), MaxValueValidator(24)])

class ALL_LN_HS_F(models.Model):
    SW_ID = models.IntegerField(validators=[MinValueValidator(1)], blank=True, null=True)
    LINE = models.IntegerField(validators=[MinValueValidator(1)], blank=True, null=True)
    STATION = models.CharField(max_length=100, blank=True, null=True)