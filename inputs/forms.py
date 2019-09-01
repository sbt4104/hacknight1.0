from django import forms
from inputs.models import filldetails, Document

class Reg_Case(forms.ModelForm):
    class Meta:
        model = filldetails
        fields =  "__all__"
