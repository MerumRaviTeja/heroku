from django import forms
from .models import *
class AddNumbersForm(forms.Form):
    box1=forms.IntegerField()
    box2=forms.IntegerField()
    box3=forms.IntegerField()
    box4=forms.IntegerField()
    box5=forms.IntegerField()
    box6=forms.IntegerField()
    box7=forms.IntegerField()
    box8=forms.IntegerField()
    box9=forms.IntegerField()
class login(forms.ModelForm):
    class Meta:
          model=data
          fields=['Enter_Name','Securitycode','Email_Address']
          widgets = {
           'Securitycode':forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Securitycode'}),
           "Enter_Name":forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your name'}),
           "Email_Address":forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your email address'}),
           }
class chatbox(forms.Form):
    chater=forms.CharField()
    chatermail=forms.EmailField()
    message=forms.CharField()
