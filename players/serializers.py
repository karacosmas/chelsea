from rest_framework  import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class meta:
        model = Person
        fields =("ID", "First", "Last", "title")
