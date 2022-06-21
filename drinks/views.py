from asyncio.windows_events import NULL
import imp
import re
from webbrowser import get
from django import db
from django.http import JsonResponse

import drinks
from .models import Drink, Section, Sentence
from .serializer import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from drinks import serializer

import json

@api_view(['GET', 'POST'])
def drink_list(request):

    if request.method == 'GET':
        drinks = Drink.objects.all()
        drinkserializer = DrinkSerializer(drinks, many=True)
        return Response(drinkserializer.data)

    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def drink_detail(request, id):

    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def insert_pages(request):
    # body_unicode = request.data.decode('utf-8')
    # d1=json.dumps(request.data) 	
    # body = json.loads(d1)
    body=request.data
    print(type(body["Page1"]["3.2.2"]))
    for p in body:
        for sec in body[p]:
            temp=Section.objects.filter(section=sec)
            if(temp.count()>0):
                print(sec + "already exists")
                sec1=Section.objects.get(section=sec)
            else:
                sec1= Section.objects.create(section=sec)
            
            for sen in body[p][sec]:
                sen1= Sentence.objects.create(sentence=sen,page_number=p)
                sec1.sentences.add(sen1)
    return Response(body, status=status.HTTP_201_CREATED)
