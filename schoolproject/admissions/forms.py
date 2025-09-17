from django import forms 
from admissions.models import student

class studentmodelforms(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'
    
    
