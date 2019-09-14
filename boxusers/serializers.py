""" This file will convert models.py data to .json data """

from rest_framework import serializers
from .models import people

class peopleSerializer(serializers.ModelSerializer):

    class Meta:
        model = people
        fields = '__all__'