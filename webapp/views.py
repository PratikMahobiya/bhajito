from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .models import User,customer,Restaurant
from .forms import CustomerSignUpForm,RestuarantSignUpForm,CustomerForm,RestuarantForm

# Create your views here.
#-----------------------------------Main Page--------------------------------------------------------
def home(request):
	return render(request, 'home.html')

#-----------------------------------Creation of Customer--------------------------------------------------------
def Customer_regis(request):
	if request.method == "POST":
		form = CustomerSignUpForm(request.POST)
		if form.is_valid():
			try:
				username = request.POST.get('username','')
				email = request.POST.get('email','')
				# first_name = request.POST.get('first_name','')
				# last_name = request.POST.get('last_name','')
				password = request.POST.get('password','')
				form_obj = User(username=username,email=email,password=password)
				form_obj.save()
				messages.add_message(request, messages.INFO, 'User Successfully Created..')
				messages.add_message(request, messages.INFO, 'Now You Can Login..')
				return HttpResponseRedirect('/login')
			except:
				pass
	else:
		form = CustomerSignUpForm()
	return render(request,'Customer/C_signup.html')


#Create customer profile 
def createCustomer(request):
	form = CustomerForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return redirect('/customer/c_profile')
	context={
	'form':form,
	}
	return render(request,'Customer/C_profile_form.html',context)

# customer profile view
def customerProfile(request,pk=None):
	if pk:
		user = User.objects.get(pk=pk)
	else:
		user=request.user
	
	return render(request,'Customer/C_profile.html',{'user':user})


#  Update customer detail
def updateCustomer(request,id):
	form  	 = CustomerForm(request.POST or None,instance=request.user.customer)
	if form.is_valid():
		form.save()
		return redirect('/customerProfile')
	context={
	'form':form,
	}
	return render(request,'Customer/C_profile_form.html',context)


#-----------------------------------Creation of Restaurent--------------------------------------------------------
def Restaurent_regis(request):
	if request.method == "POST":
		form = RestuarantSignUpForm(request.POST)
		if form.is_valid():
			try:
				username = request.POST.get('username','')
				email = request.POST.get('email','')
				# first_name = request.POST.get('first_name','')
				# last_name = request.POST.get('last_name','')
				password = request.POST.get('password','')
				form_obj = User(username=username,email=email,
										password=password)
				form_obj.save()
				messages.add_message(request, messages.INFO, 'Resto. User Successfully Created..')
				messages.add_message(request, messages.INFO, 'Now You Can Login..')
				return redirect('/login')
			except:
				pass
	else:
		form = RestuarantSignUpForm()
	return render(request,'Restaurent/R_signup.html')

#Create Restaurent profile 
def createResto(request):
	form = RestuarantForm(request.POST or None)
	if form.is_valid():
		try:
			first_name = request.POST.get('first_name','')
			last_name  = request.POST.get('last_name','')
			resto_name = request.POST.get('resto_name','')
			info  = request.POST.get('info','')
			min_ord  = request.POST.get('min_ord','')
			location = request.POST.get('location','')
			r_logo  = request.POST.get('r_logo','')
			status  = request.POST.get('status','')
			form_obj = User(first_name=first_name,last_name=last_name,resto_name=resto_name,info=info,
								min_ord=min_ord,location=location,r_logo=r_logo,status=status)
			form_obj.save()
			messages.add_message(request, messages.INFO, 'Resto. Profile Successfully Created..')
			return redirect('/Restaurent/r_profile')
		except:
			pass
	context={
	'form':form,
	}
	return render(request,'Restaurent/R_profile_form.html',context)

# Restaurent profile view
def restoProfile(request,pk=None):
	if pk:
		user = User.objects.get(pk=pk)
	else:
		user=request.user
	
	return render(request,'Restaurent/R_profile.html',{'user':user})


#  Update Restaurent detail
def updateResto(request,id):
	form  	 = CustomerForm(request.POST or None,instance=request.user.customer)
	if form.is_valid():
		form.save()
		return redirect('/restoProfile')
	context={
	'form':form,
	}
	return render(request,'Restaurent/R_profile_form.html',context)

#-----------------------------------Login Module for Customers--------------------------------------------------------------
@login_required()
def index(request):
    messages.add_message(request, messages.INFO, 'You are now Login.')
    return render(request, 'Customer/index.html')

def login(request):
	if request.user.is_authenticated:
		messages.add_message(request, messages.INFO, 'You are already Logged in.')
		return HttpResponseRedirect('/customer/index')
	else:
		return render(request, 'login.html')
        
def auth_view(request):
	if request.method == "POST":
		username = request.POST.get('user')
		password = request.POST.get('pass')
		Type 	 = request.POST.get('Type')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			if Type == "Customer":
				auth.login(request, user)
				messages.add_message(request, messages.INFO, 'Your are now Logged in.')
				return HttpResponseRedirect('/customer/c_customer')
			if Type == "Restaurent":
				auth.login(request, user)
				messages.add_message(request, messages.INFO, 'Your are now Logged in.')
				messages.add_message(request, messages.INFO, 'Welcome to your Restaurent.')
				return HttpResponseRedirect('/restaurent/c_restaurent')
		else:
			messages.add_message(request, messages.WARNING, 'Invalid Login Credentials')
			return HttpResponseRedirect('/login')

#-----------------------------------Logout Module--------------------------------------------------------------
def logout(request):
	if request.user.is_authenticated:
		auth.logout(request)
	messages.add_message(request, messages.INFO, 'You are Successfully Logged Out')
	messages.add_message(request, messages.INFO, 'Thanks for visiting.')
	return HttpResponseRedirect('/login')
