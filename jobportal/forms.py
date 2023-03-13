from .models import Profile, Skill
from django import forms


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('full_name', 'country', 'location',
                  'resume', 'grad_year', 'looking_for',)


class NewSkillForm(forms.ModelForm):
    class Meta: 
        model = Skill
        fields = ('skill', )
