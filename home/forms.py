from django import forms
from .models import FoodMenu,Contact,Review,Orgainfo

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'


class FoodMenuForm(forms.ModelForm):
    class Meta:
        model=FoodMenu
        fields='__all__'



class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'


class OrgainfoForm(forms.ModelForm):
    class Meta:
        model=Orgainfo
        fields='__all__'