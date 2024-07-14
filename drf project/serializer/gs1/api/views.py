from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer 
from rest_framework.renderers import JSONRenderer
from django.http  import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Model object - single Student Data

def studen_detail(request,pk):
    std = Student.objects.get(id=pk)
    print(std)
    serializer = StudentSerializer(std)
    print(serializer)
    # json_data = JSONRenderer().render(serializer.data) 
    # print(json_data)
    # return HttpResponse(json_data,content_type = 'application/json')
    return JsonResponse(serializer.data)


def studen_list(request):
    std = Student.objects.all()
    print(std)
    serializer = StudentSerializer(std,many = True)
    print(serializer)
    json_data = JSONRenderer().render(serializer.data) 
    print(json_data)
    return HttpResponse(json_data,content_type = 'application/json')


@csrf_exempt
def Student_created(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Inserted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type = 'application/json')

 