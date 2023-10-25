from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignupForm(UserCreationForm):
    email = forms.EmailField(label='', required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email address'}))
    first_name = forms.CharField(label='', max_length=100, required=False,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First name'}) )
    last_name = forms.CharField(label='', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last name'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
    

    def __init__(self, *args, **kwargs):
        super(SignupForm,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required'

        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder']='Password-1'
        self.fields['password1'].label = ''
        self.fields['password1'].widget.attrs['class']='form-control'

        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['placeholder']='Password-2'
        self.fields['password2'].label = ''
        self.fields['password2'].widget.attrs['class']='form-control'
        

#AddRecord Form

class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"First Name",'class':'form-control'}),label='')
    last_name = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name",'class':'form-control'}),label='')

    email = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Email",'class':'form-control'}),label='')

    phone = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Phone",'class':'form-control'}),label='')

    address = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Adress",'class':'form-control'}),label='')

    city = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"City",'class':'form-control'}),label='')

    state = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Stete",'class':'form-control'}),label='')

    zipcode = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Zip code",'class':'form-control'}),label='') 

    class Meta:
        model = Record
        #fields = '__all__'
        exclude = ["user"]