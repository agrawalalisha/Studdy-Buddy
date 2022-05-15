from django.contrib import admin
from .models import Profile, Room, Message, Course, StudyDate
from django.contrib.auth.models import User

class CourseInline(admin.TabularInline):
  model = Course
  extra = 1

# class RoomInLine(admin.TabularInline):
#   model = Room
#   extra = 1

class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Information', {'fields': ['first_name', 'last_name', 'email', 'pronouns', 'year', 'major']}),
        ('Bio', {'fields': ['bio']})
    ]
    list_display = ('first_name', 'last_name')
    # list_filter = ['courses']
    search_fields = ['first_name', 'last_name', 'courses']
    inlines = (CourseInline,)

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline] # if you click on a user, you can see his/her profile

# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(StudyDate)
# admin.site.unregister(Group)


