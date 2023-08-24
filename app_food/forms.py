from django import forms
from .models import foodtable

class FoodInfoForm(forms.ModelForm):
    class Meta:
        model = foodtable
        fields = '__all__'  
        labels = {
            'name_of_food_th' : 'ชื่ออาหาร (ไทย):',
            'name_of_food_eng' : 'Name (eng):',
            'kcal' : 'Energy (kcal):',
            'water' : 'Water:',
            'protein' : 'Protein:',
            'fat' : 'Fat:',
            'carb' : 'Carbohydrate',
            'dietary_fiber' : 'Fiber:',
            'ash' : 'Ash:',
            'calcium' : 'Calcium:',
            'phosphorus' : 'Phosphorus:',
            'magnesium' : 'Magnesium:',
            'sodium' : 'Sodium:',
            'protassium' : 'Protassium:',
            'iron' : 'Iron:',
            'copper' : 'Copper:',
            'zinc' : 'Zinc:',
            'iodine' : 'Iodine:',
            'betacarotene' : 'Betacarotene:',
            'retinol' : 'Retinol:',
            'RAE' : 'Total Vitamin A RAE:',
            'thiamin' : 'Thiamin:',
            'riboflavin' : 'Riboflavin:',
            'niacin' : 'Niacin:',
            'vitamin_C' : 'Vitamin C:',
            'vitamin_E' : 'Vitamin E:',
            'sugar' : 'Sugar:',
            'vegan' : 'Vegan food?:',
            'food_image' : 'Image food:',
        }
