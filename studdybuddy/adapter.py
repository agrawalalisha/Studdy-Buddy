from django.conf import settings
from models import Profile
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        # if profile already in database send to dashboard
        print(request.user.email)
        if (Profile.objects.filter(email=request.user.email).exists()):
            return "/dashboard"
        # else profile is new and needs to accept code of conduct
        else:
            return "/code_of_conduct"
