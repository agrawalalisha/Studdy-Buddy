from django.forms import ModelForm
from .models import Profile
from django.forms import widgets

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': widgets.TextInput(attrs={
                'class': "form-control py-2 my-3",
                'style': 'max-width: 200px; display: inline-block;'
                }),
            'last_name': widgets.TextInput(attrs={
                'class': "form-control py-2 my-3", 
                'style': 'max-width: 200px; display: inline-block;'
                }),
            'pronouns': widgets.TextInput(attrs={
                'class': "form-control py-2 my-3", 
                'style': 'max-width: 200px; display: inline-block;'
                }),
            # 'year': widgets.TextInput(attrs={
            #     'class': "form-control py-2 my-3", 
            #     'style': 'max-width: 200px;'
            #     }),
            'major': widgets.TextInput(attrs={
                'class': "form-control py-2 my-3", 
                'style': 'max-width: 200px; display: inline-block;'
                }),
            # 'courses': widgets.SelectMultiple(attrs={
            #     'class': "form-control py-2 my-3", 
            #     'style': 'display: inline-block;'
            #     }),
            'bio': widgets.TextInput(attrs={
                'class': "form-control py-2 my-3", 
                'style': 'max-width: 200px; display: inline-block;'
                })
        }

# class UserForm(forms.ModelForm):
    
#     class Meta:
#         model = User
#         fields = ['First Name', 'Last Name', 'Password']