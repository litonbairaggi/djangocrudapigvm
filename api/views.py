from django.shortcuts import render

# Create your views here.

from api.models import Team
from .serializers import TeamSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

class GenericTeamView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = 'id'

    def get(self, requrst, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def post(self, requrst):
        return self.create(request) 

    def put(self, requrst, id=None):
        return self.update(request, id) 

    def delete(self, requrst, id=None):
        return self.destroy(request, id)    
