import datetime
from django.utils import timezone
from django.db import models


class Filament(models.Model):

    class Material(models.TextChoices):
        PLA = "PLA", "PLA"
        PLACF = "PLACF", "PLA with carbon fiber"
        PLAsilk = "PLAsilk", "PLA silk"
        PLAplus = "PLA+", "PLA+ (generic)"
        PETG = "PETG", "PETG"
        ABS = "ABS", "ABS"
        ASA = "ASA", "ASA"
        TPU = "TPU", "TPU"
        TPE = "TPE", "TPE"

    material = models.CharField(max_length=10, choices=Material.choices)
    colour = models.CharField(max_length = 30)
    brand = models.CharField(max_length=50)
    weight = models.IntegerField() # weight in grams
    price = models.DecimalField(max_digits = 5, decimal_places = 2) # max 999.99
    print_temperature = models.IntegerField()
    bed_temperature = models.IntegerField()
    flow = models.DecimalField(default = 0.97, max_digits = 3, decimal_places = 2)
    max_flowrate = models.DecimalField(default = 12, max_digits = 3, decimal_places = 1)
    k_value = models.DecimalField(max_digits = 4, decimal_places = 3)
    purchase_date = models.DateField("Purchase date")

    def __str__(self):
        return f"{self.material} {self.colour} {self.brand}"
    
    def was_purchased_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.purchase_date <= now



class Comment(models.Model):
    Filament = models.ForeignKey(Filament, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=400)

