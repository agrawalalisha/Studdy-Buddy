from email.policy import default
from django.db import models
from datetime import datetime


class Room(models.Model):
    name = models.CharField(max_length=1000)


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)


class Profile(models.Model):
    class Year(models.TextChoices):
        FIRST_YEAR = "First Year"
        SECOND_YEAR = "Second Year"
        THIRD_YEAR = "Third Year"
        FOURTH_YEAR = "Fourth Year"

    first_name = models.CharField(max_length=25, default="")
    last_name = models.CharField(max_length=25, default="")
    email = models.CharField(max_length=50, default="")
    pronouns = models.CharField(max_length=15, default="")
    year = models.CharField(max_length=11, choices=Year.choices, default="")
    major = models.CharField(max_length=30, default="")
    bio = models.CharField(max_length=560, default="")

    def __str__(self):
        return "First name: {} Last name: {} Email: {} Pronouns: {} Year: {} Major: {} Bio: {}".format(self.first_name,
                                                                                                       self.last_name,
                                                                                                       self.email,
                                                                                                       self.pronouns,
                                                                                                       self.year,
                                                                                                       self.major,
                                                                                                       self.bio)

class Course(models.Model):
    name = models.CharField(max_length=9)
    profile = models.ForeignKey(to=Profile, on_delete=models.CASCADE, related_name="courses", default=1)


class StudyDate(models.Model):
    participants = models.ManyToManyField(Profile)
    course = models.CharField(max_length=50, default="")
    month = models.CharField(max_length=25, default="")
    day = models.IntegerField(null=True)
    hour = models.IntegerField(null=True)
    minute = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    description = models.CharField(max_length=100, default="")


    def __str__(self):
        return "{} study session on {}. {}, {} at {}:{}".format(self.course,    
                                                                self.month,
                                                                self.day,
                                                                self.year,
                                                                self.hour,
                                                                self.minute
                                                                )