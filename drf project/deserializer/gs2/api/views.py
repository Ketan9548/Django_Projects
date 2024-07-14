from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import Studentserializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
# Create your views here.
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = Studentserializer(data=pythondata)  # Use 'data' argument when creating a serializer
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data inserted'}
            print(res[0])
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')  # Correct 'applicateion' typo
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json') 
    else:
        return HttpResponse(json_data, content_type='application/json')