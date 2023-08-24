from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

class Profile(models.Model):
    GENDER_CHOICES = (
        (1, 'ชาย'),
        (0, 'หญิง'),
    )
    ACTIVITY_CHOICES = (
        (1, 'เคลื่อนไหวน้อยมาก นั่งเป็นส่วนใหญ่'),
        (2, 'ออกกำลังกายเบา ๆ 1–3 วันต่อสัปดาห์'),
        (3, 'ออกกำลังกายหนักปานกลาง 3–5 วันต่อสัปดาห์'),
        (4, 'ออกกำลังกายอย่างหนัก 6–7 วันต่อสัปดาห์'),
        (5, 'ออกกำลังกายหรือทำกิจกรรมที่ต้องใช้แรงอย่างหนักทุกวัน'),
    )
    gender = models.IntegerField(choices=GENDER_CHOICES, null=False)
    date_of_birth = models.DateField(null=False)
    height = models.DecimalField(null=False, max_digits=5, decimal_places=2)
    weight = models.DecimalField(null=False, max_digits=5, decimal_places=2)
    activity_level = models.IntegerField(choices=ACTIVITY_CHOICES, null=False)
    user_cal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    user = models.OneToOneField("app_users.CustomUser", on_delete=models.CASCADE)

    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age


    def calculate_tdee(self):
        if self.gender == 1:  # ชาย
            bmr = 66 + (13.7 * float(self.weight)) + (5 * float(self.height)) - (6.8 * self.calculate_age())
        else:  # หญิง
            bmr = 665 + (9.6 * float(self.weight)) + (1.8 * float(self.height)) - (4.7 * self.calculate_age())

        activity_multiplier = {
            1: 1.2,
            2: 1.375,
            3: 1.55,
            4: 1.725,
            5: 1.9,
        }
        
        tdee = bmr * activity_multiplier[self.activity_level]
        return tdee

    def save(self, *args, **kwargs):
        self.user_cal = self.calculate_tdee()
        super().save(*args, **kwargs)

