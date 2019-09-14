from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import people
from .serializers import peopleSerializer


class PeopleList(APIView):

    def get(self, request): #get method is to get all data from people table
        peoples = people.objects.all() #peoples is a variable to store all the objects from people
        serializer = peopleSerializer(peoples, many=True)
        return Response(serializer.data)

    def post(self): #post method is to create a new person in people
        pass