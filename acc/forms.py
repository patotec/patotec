from .models import *
from django.contrib.auth import get_user_model
from django import forms
User = get_user_model()


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = ['image']