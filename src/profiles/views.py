from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm

# Create your views here.
def my_profile(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileForm(request.POST or None, request.FILES or None ,instance=profile)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'profiles/myprofile.html', context)