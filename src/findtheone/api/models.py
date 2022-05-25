from django.db import models
from django.contrib.auth.models import User
from dateutil.relativedelta import relativedelta
import base64
import datetime

# Create your models here.


class Gender(models.Model):
    name = models.CharField(max_length=256)

    def serialize(self):
        return {
            "name": self.name, 
            "id": self.id
        }

class Location(models.Model):
    name = models.CharField(max_length=256)


class RelationshipType(models.Model):
    name = models.CharField(max_length=1024)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }



class Profile(User):
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name="profiles", blank=True, null=True)
    genders_attracted_to = models.ManyToManyField(Gender, related_name="profiles_interested", blank=True, null=True)
    #location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="profiles", null=True)
    #locations_interested_in = models.ManyToManyField(Location, related_name="profiles_interested")
    relationship_types_interested_in = models.ManyToManyField(RelationshipType, related_name="profiles")
    short_description = models.CharField(max_length=1024, null=True)
    long_description = models.CharField(max_length=4096, null=True)
    birth_date = models.DateField(null=True)
 





    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "first_name": self.first_name,
            "gender": self.gender.serialize(),
            "genders_attracted_to": [gender.serialize() for gender in self.genders_attracted_to.all()],
            #"location": self.location.name,
            #"locations_interested_in":[location.name for location in self.locations_interested_in],
            "relationship_types_interested_in": [relationship_type.serialize() for relationship_type in self.relationship_types_interested_in.all()],
            "short_description": self.short_description,
            "long_description": self.long_description,
            "birth_date": {
                "year": self.birth_date.year,
                "month": self.birth_date.month,
                "day": self.birth_date.day
            },
            "age": relativedelta(datetime.datetime.today(), self.birth_date).years,
            "photos": [photo.serialize() for photo in self.photos.order_by("priority")]
        }


def user_directory_path(instance, filename):
    return f"photos/{instance.profile.id}"

class Photo(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="photos")
    photo = models.BinaryField()
    priority = models.IntegerField(null=True)

    def serialize(self):
        return {
            "photo": base64.b64encode(self.photo)
        }

class Like(models.Model):
    liking = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liked")
    liked = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liked_by")

class Skip(models.Model):
    skipping = models.ForeignKey(User, on_delete=models.CASCADE, related_name="skipped")
    skipped = models.ForeignKey(User, on_delete=models.CASCADE, related_name="skipped_by")

class Pair(models.Model):
    users = models.ManyToManyField(User, related_name='pairs')

    def serialize(self):
        return {
            "id": self.id,
            "users": [user.serialize() for user in self.users],
            "messages": [message.serialize() for message in self.messages]
        }

class Message(models.Model):
    pair = models.ForeignKey(Pair, on_delete=models.CASCADE, related_name="messages")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=4096)


    def serialize(self):
        return {
            "id": self.id,
            "author_id": self.author.id,
            "datetime": {
                "year": self.datetime.year,
                "month": self.datetime.month,
                "day": self.datetime.day,
                "hour": self.datetime.hour,
                "minute": self.datetime.minute,
            },
            "content": self.content
        }







