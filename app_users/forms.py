# app_users/forms.py
from django.contrib.auth.forms import UserCreationForm
from django import forms
from app_users.models import Profile, CustomUser

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email',) 

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser  # แก้ไขจาก model = User เป็น model = CustomUser
        fields = ('first_name', 'last_name')

class ExtendedProfileForm(forms.ModelForm):
    prefix = 'extend'
    class Meta:
        model = Profile
        fields = ('gender', 'date_of_birth', 'height', 'weight', 'activity_level', 'user_cal')
        labels = {
            'gender': 'เพศ',
            'date_of_birth': 'วัน/เดือน/ปี เกิด',
            'height': 'ส่วนสูง (CM)',
            'weight': 'น้ำหนัก (KG)',
            'activity_level': 'กิจกรรมการออกกำลังกาย',
            'user_cal': 'จำนวนแคลอรี่/วัน',
        }
