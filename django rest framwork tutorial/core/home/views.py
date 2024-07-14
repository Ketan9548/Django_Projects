from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import Response

# Create your views here.
@api_view
def home(request):
    return Response({'status':200,'message':'hello kapil'})
