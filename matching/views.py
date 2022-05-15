# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# from django.urls import reverse
# from .models import Profile 
# from .forms import ProfileForm


# def home(request):
#     return render(request, "base.html")

# def profile_list(request):
#     profiles = Profile.objects.exclude(user=request.user) # retrieve objects from profile table and store them in variable "profiles"; we exclude our own
#     return render(request, "matching/profile_list.html", {"profiles": profiles})

# def profile(request, pk):
#     profile = Profile.objects.get(pk=pk)
#     return render(request, "matching/profile.html", {"profile": profile})

