from django.shortcuts import render, redirect

from collection.forms import ProfileForm
from collection.models import Profile

# Create your views here.
def index(request):
	profiles = Profile.objects.all()
	return render(request, 'index.html', {
		'profiles': profiles,
	})

def profile_detail(request, slug):
	profile = Profile.objects.get(slug=slug)
	return render(request, 'profiles/profile_detail.html', {
		'profile': profile,
	})

def edit_profile(request, slug):
	profile = Profile.objects.get(slug=slug)
	form_class = ProfileForm
	if request.method == 'POST':
		form = form_class(data=request.POST, instance=profile)
		if form.is_valid():
			form.save()
			return redirect('profile_detail', slug=profile.slug)
	else:
		form = form_class(instance=profile)
	return render(request, 'profiles/edit_profile.html', {
		'profile': profile,
		'form': form,
	})