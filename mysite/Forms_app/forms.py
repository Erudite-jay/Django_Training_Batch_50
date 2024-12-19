from django import forms
from . models import Contact

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     file=forms.FileField()

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
    