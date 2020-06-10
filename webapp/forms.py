from django import forms
from .models import User,customer,Restaurant

#create your forms here.
class user_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class login_form(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)

class CustomerSignUpForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields="__all__"
		def save(self, commit=True):
			user = super().save(commit=False)
			user.is_customer=True
			if commit:
				user.save()
			return user


class RestuarantSignUpForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model =User
		fields="__all__"
		def save(self,commit=True):
			user=super().save(commit=False)
			user.is_restaurant=True
			if commit:
				user.save()
			return user

class CustomerForm(forms.ModelForm):
	class Meta:
		model = customer
		fields =['first_name','last_name','city','phone','address']


class RestuarantForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields =['first_name','last_name','rname','info','min_ord','location','r_logo','status','approved']
