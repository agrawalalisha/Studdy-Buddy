import email
from re import template
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse
from .models import Profile, Room, Message, Course, StudyDate
from .forms import ProfileForm, ProfileViewForm, StudyDateForm
from django.contrib.auth.models import User
from django.views import generic
from studdybuddy import course_list
from django import forms

class CourseProfile:
    def __init__(self, profile):
        self.profile = profile
        self.courses = profile.courses.all()

def create_profile_view(request):
    error = ""
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            # retrieve email from hidden input field
            email = request.POST.get("email", "")
            # set profile with that email
            form.email = email
            # fails if profile with that email already exists
            if form.email_save() == 0:
                error = "User with this email already exists, please use a different Google login"
                return render(request, "studdybuddy/create_profile.html", {"form": form, "error": error})
            # else first profile with that email, saves and shows profile view
            else:
                return HttpResponseRedirect(reverse('dashboard'))
        else:
            print(form.errors)
    else:
        form = ProfileForm()
    return render(request, "studdybuddy/create_profile.html", {"form": form, "error": error})


def create_study_session(request):
    error = ""
    profile = Profile.objects.get(email=request.user.email)
    courses = profile.courses.all()
    if request.method == "POST":
        form = StudyDateForm(request.POST, initial={'participants': profile})
        # make sure all fields are filled out
        if (form.is_valid()):
            # make sure the user making the session is in the session
            if (str(profile.pk) in request.POST.getlist("participants")):
                # make sure there are more than one participants
                if (len(request.POST.getlist("participants")) > 1):
                    form.save()
                    return HttpResponseRedirect(reverse('dashboard'))
                else:
                    error = "You must include at least one other student in the session"
            else:
                error = "You must include yourself in the study session"
        else:
            error = "Please fill out all fields before submitting"
    else:
        form = StudyDateForm(initial={'participants': profile})
    return render(request, "studdybuddy/create_study_sess.html", {"form": form, "courselist": courses, "error": error})


def sessions_view(request):
    profile = Profile.objects.get(email=request.user.email)
    courses = profile.courses.all()
    dates = StudyDate.objects.exclude(participants=profile)
    errorMsg = "No sessions found for that class"
    if request.method == "GET":
        selected = request.GET.get("selected", "")
        for date in dates:
            if selected == date.course:
                errorMsg = ""
    if request.method == "POST":
        dateDesc = request.POST.get("date", "")
        date = StudyDate.objects.get(description=dateDesc)
        date.participants.add(profile)
        date.save()
        return HttpResponseRedirect(reverse('dashboard'))
    return render(request, "studdybuddy/sessions_list.html", {"dates": dates, "profile": profile,
                                                                  "courses": courses, "selected": selected, "error": errorMsg})


def dashboard_view(request):
    profile = Profile.objects.get(email=request.user.email)
    dates = profile.studydate_set.all()
    ordering = ['-date_created']
    return render(request, "studdybuddy/dashboard.html", {"profiles": profile, "dates": dates})


def logout_view(request):
    logout(request)
    return render(request, "studdybuddy/index.html")

def profile_view(request):
    try:
        instance = Profile.objects.get(email=request.user.email)
        form = ProfileViewForm(instance=instance)
        # makes the fields readonly and disabled
        form.fields['first_name'].widget.attrs['readonly'] = True
        form.fields['last_name'].widget.attrs['readonly'] = True
        form.fields['email'].widget.attrs['readonly'] = True
        form.fields['pronouns'].widget.attrs['readonly'] = True
        form.fields['year'].widget.attrs['readonly'] = True
        form.fields['major'].widget.attrs['readonly'] = True
        form.fields['bio'].widget.attrs['readonly'] = True        
        form.fields['first_name'].widget.attrs['disabled'] = True
        form.fields['last_name'].widget.attrs['disabled'] = True
        form.fields['email'].widget.attrs['disable'] = True
        form.fields['pronouns'].widget.attrs['disabled'] = True
        form.fields['year'].widget.attrs['disabled'] = True
        form.fields['major'].widget.attrs['disabled'] = True
        form.fields['bio'].widget.attrs['disabled'] = True
    except Profile.DoesNotExist:
        raise Http404("Profile does not exist")
    return render(request, 'studdybuddy/view_profile.html', {'form': form})

def edit_profile_view(request):
    # retrieve profile using social account email
    instance = Profile.objects.get(email=request.user.email)
    # if user clicks save, try to save profile
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return HttpResponseRedirect(reverse('view_profile'))
    # else display profile forms prepopulated with current form info
    else:
        form = ProfileForm(instance=instance)
        # make email readonly
        form.fields['email'].widget.attrs['readonly'] = True
        form.fields['email'].widget.attrs['disabled'] = True
    return render(request, "studdybuddy/edit_profile.html", {"form": form})


def edit_classes_view(request):
    profile = Profile.objects.get(email=request.user.email)
    courselist = course_list.getCourseList()
    courses = profile.courses.all()
    if request.method == "POST":
        # first remove all courses
        profile.courses.all().delete()
        # next add all courses from the page to the profile
        first = True
        # iterate over course list and add each course to profile
        for course in request.POST:
            # don't include csrf token
            if not first:
                newCourse = Course(name=course, profile=profile)
                newCourse.save()
            first = False
        courses = profile.courses.all()
    return render(request, "studdybuddy/edit_classes.html", {"courses":courses, "courselist": courselist}) 


def code_of_conduct_view(request):
    base_template = "studdybuddy/base.html"
    # check if a user with this email exists
    try:
        Profile.objects.get(email=request.user.email)
    # if profile with this email doesn't exist
    except Profile.DoesNotExist:
        no_profile = 1
        base_template = "studdybuddy/partial_base.html"
    # else profile already exists
    else:
        no_profile = 0
    return render(request, 'studdybuddy/code_of_conduct.html', {"no_profile": no_profile, "base_template":base_template})


def about_view(request):
    return render(request, 'studdybuddy/about.html')


def profile_list(request):
    # retrieve objects from profile table and store them in variable "profiles"; we exclude our own
    profile = Profile.objects.get(email=request.user.email)
    courses = profile.courses.all()
    other_profiles = Profile.objects.exclude(email=request.user.email) 
    profiles = []
    for p in other_profiles:
        profiles.append(CourseProfile(p))
    return render(request, "studdybuddy/profile_list.html", {"profiles": profiles, "courses": courses}) 


def matchingprofile(request, pk):
    try:
        profile = Profile.objects.get(pk=pk)
        form = ProfileViewForm(instance=profile)
        # makes the fields readonly
        form.fields['first_name'].widget.attrs['readonly'] = True
        form.fields['last_name'].widget.attrs['readonly'] = True
        form.fields['email'].widget.attrs['readonly'] = True
        form.fields['pronouns'].widget.attrs['readonly'] = True
        form.fields['year'].widget.attrs['readonly'] = True
        form.fields['major'].widget.attrs['readonly'] = True
        form.fields['bio'].widget.attrs['readonly'] = True
    except Profile.DoesNotExist:
        raise Http404("Profile does not exist")
    return render(request, "studdybuddy/profile.html", {"profile": profile, "form": form})


def forum(request):
    errorMsg = ""
    profile = Profile.objects.get(email=request.user.email)
    courses = profile.courses.all()
    other_profiles = Profile.objects.exclude(email=request.user.email) 
    profiles = []
    for p in other_profiles:
        profiles.append(CourseProfile(p))
    if request.method == "POST":
        username = request.POST.get('username')
        if (username != ""):
            room = request.POST.get('room_name')
            if Room.objects.filter(name=room).exists():
                return redirect(room + '/?username=' + username)
            else:
                new_room = Room.objects.create(name=room)
                new_room.save()
                return redirect(room + '/?username=' + username)
        else:
            errorMsg = "You must enter a username"
    return render(request, 'studdybuddy/forum.html', {"profiles": profiles, "courses": courses, "error": errorMsg})

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'studdybuddy/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()

def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})
