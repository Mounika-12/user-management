from rest_framework import serializers
from .models import *
from drf_queryfields import QueryFieldsMixin



class usersSerializer(QueryFieldsMixin,serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'

