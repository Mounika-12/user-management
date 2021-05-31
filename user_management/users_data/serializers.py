from rest_framework import serializers
from .models import *
from drf_queryfields import QueryFieldsMixin

class usersSerializer(QueryFieldsMixin,serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'

    # Custom validation can be performed on the fields
    def validate(self, data):
        """
        Check that input data and raise validation errors
        """
        return data

    # Customize the user data before saving to database
    def create(self, validated_data):

        users = Users.objects.create(**validated_data)

        return users

    # Customize the user data before updating and saving to database
    def update(self, instance, validated_data):

        for item in validated_data:
            setattr(instance, item, validated_data[item])

        instance.save()
        return instance



