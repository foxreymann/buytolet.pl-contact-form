from django import forms

from btlplcontact.models import ContactData

class ContactDataForm(forms.ModelForm):
  class Meta:
    model = ContactData
    fields = ('name', 'email')
