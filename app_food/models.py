from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def validate_at_least_one_name(value):
    if not value:
        raise ValidationError("กรุณากรอกชื่ออย่างน้อยหนึ่งช่อง")

class foodtable(models.Model):
    Food_ID = models.AutoField(primary_key=True)
    name_of_food_th = models.CharField(max_length=150, validators=[validate_at_least_one_name])
    name_of_food_eng = models.CharField(max_length=150, validators=[validate_at_least_one_name])
    kcal = models.FloatField(null=True, blank=True)
    water = models.FloatField(null=True, blank=True)
    protein = models.FloatField(null=True, blank=True)
    fat = models.FloatField(null=True, blank=True)
    carb = models.FloatField(null=True, blank=True)
    dietary_fiber = models.FloatField(null=True, blank=True)
    ash = models.FloatField(null=True, blank=True)
    calcium = models.FloatField(null=True, blank=True)
    phosphorus = models.FloatField(null=True, blank=True)
    magnesium = models.FloatField(null=True, blank=True)
    sodium = models.FloatField(null=True, blank=True)
    protassium = models.FloatField(null=True, blank=True)
    iron = models.FloatField(null=True, blank=True)
    copper = models.FloatField(null=True, blank=True)
    zinc = models.FloatField(null=True, blank=True)
    iodine = models.FloatField(null=True, blank=True)
    betacarotene = models.FloatField(null=True, blank=True)
    retinol = models.FloatField(null=True, blank=True)
    RAE = models.FloatField(null=True, blank=True)
    thiamin = models.FloatField(null=True, blank=True)
    riboflavin = models.FloatField(null=True, blank=True)
    niacin = models.FloatField(null=True, blank=True)
    vitamin_C = models.FloatField(null=True, blank=True)
    vitamin_E = models.FloatField(null=True, blank=True)
    sugar = models.FloatField(null=True, blank=True)
    vegan = models.BooleanField(default=False)
    food_image = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        db_table = 'foodtable'


   
