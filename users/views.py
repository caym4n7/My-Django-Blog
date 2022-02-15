from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from blog.models import Category

# Create your views here.

def register(request):
	categories_list = Category.objects.all()
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You are now able to log in')
			return redirect('login')
	else:
		form = UserRegisterForm()

	context = {
		"form" : form,
		"categories_list" : categories_list
	}
	
	return render(request, 'register.html', context)

@login_required
def profile_view(request, slug):
	template_name = "profile.html"
	uprofile = get_object_or_404(Profile, slug=slug)
	categories_list = Category.objects.all()
	
	context = {
		"profile" : uprofile,
		"categories_list" : categories_list
	}

	return render(request, template_name, context)

@login_required
def profile_update(request):
	categories_list = Category.objects.all()
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('profile')

	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form': u_form,
		'p_form': p_form,
		"categories_list" : categories_list
	}

	return render(request, 'profile_update.html', context)