from django.test import TestCase, Client
import datetime
from dateutil.relativedelta import relativedelta
# Create your tests here.
from .models import *


class ProfileModelTestCase(TestCase):

    def test_profile_model(self):
        gender = Gender.objects.create(name="Male")
        relationship_type = RelationshipType.objects.create(name="Long-term relationship")
        birth_date_dict = {"year": 2000, "month": 1, "day": 1}
        birth_date = datetime.date(birth_date_dict["year"], birth_date_dict["month"], birth_date_dict["day"])
        age = relativedelta(datetime.datetime.today(), birth_date).years
        profile = Profile.objects.create(username="username", email="user@mail.com", gender=gender, birth_date=birth_date, short_description="short description", long_description="long description")
        profile.genders_attracted_to.add(gender)
        profile.relationship_types_interested_in.add(relationship_type)
        self.assertEqual(profile.serialize(), {
            "id": profile.id, 
            "username": profile.username, 
            "email": profile.email, 
            "first_name": profile.first_name, 
            "gender": profile.gender.serialize(), 
            "genders_attracted_to": [gender.serialize()],
            "relationship_types_interested_in": [relationship_type.serialize()],
            "birth_date": birth_date_dict, 
            "age": age,
            "short_description": profile.short_description,
            "long_description": profile.long_description,
            "photos": []
            })

class GenderModelTestCase(TestCase):

    def test_gender_model(self):
        gender = Gender.objects.create(name="Male")
        self.assertEqual(gender.serialize(), {"id": gender.id, "name": gender.name})


class RelationshipTypeModelTestCase(TestCase):
    
    def test_relationship_type_model(self):
        relationship_type = RelationshipType.objects.create(name="Long-term relationship")
        self.assertEqual(relationship_type.serialize(), {"id": relationship_type.id, "name": relationship_type.name})

class RegisterViewTestCase(TestCase):

    def setUp(self):
        location = Location.objects.create(name='location')
        gender = Location.objects.create(name='gender')
        
        Profile.objects.create_user(username='username')
