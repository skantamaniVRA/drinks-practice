from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id','name','description']

# class PageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=
#         fields=['section','values']

# class SentenceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Sentence
#         fields=['sentence','page_number']