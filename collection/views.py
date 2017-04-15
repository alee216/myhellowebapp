from django.shortcuts import render
from collection.models import Profile

# Create your views here.
def index(request):
	profiles = Profile.objects.all()

	return render(request, 'index.html', {
		'profiles': profiles,
	})