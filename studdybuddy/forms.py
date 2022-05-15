from django.forms import ModelForm
from .models import Profile, StudyDate
from django.forms import widgets
from django import forms
from studdybuddy import course_list

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
            'email': widgets.TextInput(attrs={
                'class': "form-control py-2 my-3", 
                'style': 'max-width: 200px; display: inline-block;'
                }),
            'pronouns': widgets.TextInput(attrs={
                'class': "form-control py-2 my-3", 
                'style': 'max-width: 200px; display: inline-block;'
                }),
            'major': widgets.TextInput(attrs={
                'class': "form-control py-2 my-3", 
                'style': 'max-width: 200px; display: inline-block;'
                }),
            'bio': widgets.Textarea(attrs={
                'class': "form-control py-2 my-3", 
                'style': 'max-width: 800px; height: 150px; display: inline-block;'
                })
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['email'].disabled = True

    def email_save(self, commit=True):
        # check that there are no other users with same email before saving
        try:
            Profile.objects.get(email=self.email)
        # if profile with this email has not been created before
        except Profile.DoesNotExist:
            super().save(self)
        # email already exists
        else:
            # raise ValueError("User with entered email already exists")
            return 0

class ProfileViewForm(ProfileForm):
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
            'email': widgets.TextInput(attrs={
                'class': "form-control py-2 my-3", 
                'style': 'max-width: 200px; display: inline-block;'
                }),
            'pronouns': widgets.TextInput(attrs={
                'class': "form-control py-2 my-3", 
                'style': 'max-width: 200px; display: inline-block;'
                }),
            'year': widgets.TextInput(attrs={
                'class': "form-control py-2 my-3", 
                'style': 'max-width: 200px; display: inline-block;'
                }),
            'major': widgets.TextInput(attrs={
                'class': "form-control py-2 my-3", 
                'style': 'max-width: 200px; display: inline-block;'
                }),
            'bio': widgets.Textarea(attrs={
                'class': "form-control py-2 my-3", 
                'style': 'max-width: 800px; height: 150px; display: inline-block;'
                })
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['first_name'].disabled = True
            self.fields['last_name'].disabled = True
            self.fields['email'].disabled = True
            self.fields['pronouns'].disabled = True
            self.fields['year'].disabled = True
            self.fields['major'].disabled = True
            self.fields['courses'].disabled = True
            self.fields['bio'].disabled = True


MONTH_CHOICES = [
    ('Jan', 'January'),
    ('Feb', 'February'),
    ('March', 'March'),
    ('Apr', 'April'),
    ('May', 'May'),
    ('Jun', 'June'),
    ('Jul', 'July'),
    ('Aug', 'August'),
    ('Sep', 'September'),
    ('Oct', 'October'),
    ('Nov', 'November'),
    ('Dec', 'December')
]

DAY_CHOICES = [tuple([x,x]) for x in range(1,32)]

YEAR_CHOICES = [tuple([x,x]) for x in range(2022,2026)]

HOUR_CHOICES = [tuple([x,x]) for x in range(0,25)]

MINUTE_CHOICES = [tuple([x,x]) for x in range(0,60)]

class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, profile):
        return '%s %s (%s)' % (profile.first_name, profile.last_name, profile.email)

class DateTimePickerInput(forms.DateTimeInput):
    input_type = 'datetime'


class StudyDateForm(ModelForm):
    class Meta:
        model = StudyDate
        fields = ['month', 'day', 'year', 'hour', 'minute', 'course', 'description', 'participants']
        widgets = {
            'month': widgets.Select(choices=MONTH_CHOICES),
            'day': widgets.Select(choices=DAY_CHOICES),
            'year': widgets.Select(choices=YEAR_CHOICES),
            'hour': widgets.Select(choices=HOUR_CHOICES),
            'minute': widgets.Select(choices=MINUTE_CHOICES),
            # 'datetime': DateTimePickerInput(),
            # 'description': widgets.Textarea(attrs={
            #     'class': "form-control py-2 my-3",
            #     'style': 'max-width: 800px; height: 150px; display: inline-block;'
            #     }),
            'description': widgets.TextInput(attrs={
                'class': "form-control py-2 my-3", 
                'style': 'max-width: 400px; display: inline-block;'
            }),
        }

    participants = CustomMMCF(
        queryset=Profile.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].readonly = True

    # def date_save(self, commit=True):
    #     super().save(self)