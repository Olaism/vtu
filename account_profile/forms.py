from django import forms

from .models import Profile


class ProfileEditForm(forms.ModelForm):
    first_name = forms.CharField(max_length=200, required=False)
    last_name = forms.CharField(max_length=200, required=False)

    class Meta:
        model = Profile
        fields = ("phone",)
