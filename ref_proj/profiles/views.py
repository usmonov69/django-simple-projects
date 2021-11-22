from django.shortcuts import render
from .models import Profile


def my_recommendation_view(request):
	profile = Profile.objects.get(user=request.user)
	my_recs = profile.get_recommened_profiles()
	context = {'my_recs': my_recs}
	return render(request, 'profiles/main.html', context) 