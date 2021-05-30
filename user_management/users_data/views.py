from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import mixins,generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter


class Users_List(generics.ListAPIView, mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Users.objects.all()
    serializer_class = usersSerializer
    
    filter_backends = (DjangoFilterBackend, OrderingFilter,SearchFilter,)#'news__headline','tags__tag',
    filter_fields = ('id','first_name','last_name',)
    ordering_fields = ('id','first_name','last_name','email','phone_number','modified_by','modified_date_time')
    search_fields = ('first_name','last_name')


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Users.objects.all()

        return queryset

class Users_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = usersSerializer

    def get(self, request, *args, **kwargs):
        """GET the data based on the id
        """
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """PATCH the data based on the id
        """
        return self.partial_update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """PUT the data based on the id
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """DELETE the data based on the id
        """
        return self.destroy(request, *args, **kwargs)

