from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Students
from .serializers import serializerstudent
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
# for class
from django.utils.decorators import method_decorator
from django .views import View

#class base
@method_decorator(csrf_exempt,name='dispatch')
class StudentApi(View):
    def get(self,request,*args,**kwargs):
        json_data = request.body
        #converting string 
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            stu = Students.objects.get(id=id)
            serializer = serializerstudent(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        stu = Students.objects.all()
        serializer = serializerstudent(stu,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self,request,*args,**kwargs):
        json_data = request.body
        #converting string
        strem = io.BytesIO(json_data)
        # provideing jsonparser dictionar
        pythondata = JSONParser().parse(strem)
        serializer = serializerstudent(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Inserted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')
        

    def put(self,request,*args,**kwargs):
        json_data = request.body
        #converting string
        strem = io.BytesIO(json_data)
        # provideing jsonparser dictionar
        pythondata = JSONParser().parse(strem)
        id = pythondata.get('id')
        stu = Students.objects.get(id = id)
        # this use for whole row data update
        # serializer = serializerstudent(stu,data=pythondata)
        # this is use for parserl update
        serializer = serializerstudent(stu,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data updated!!!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')
        


    def delete(self,request,*args,**kwargs):
        json_data = request.body
        #converting string
        strem = io.BytesIO(json_data)
        # provideing jsonparser dictionar
        pythondata = JSONParser().parse(strem)
        id = pythondata.get('id')
        stu = Students.objects.get(id = id)
        stu.delete()
        res = {'msg':'delete data success!!'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(res,safe=False)


# function base
# @csrf_exempt
# def Studen_api(request):
#     # this is for fetch data
#     if request.method == 'GET':
#         json_data = request.body
#         #converting string 
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id', None)
#         if id is not None:
#             stu = Students.objects.get(id=id)
#             serializer = serializerstudent(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type='application/json')
#         stu = Students.objects.all()
#         serializer = serializerstudent(stu,many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type='application/json')

#     # this is for insert data
#     if request.method == 'POST':
#         #save the data
#         json_data = request.body
#         #converting string
#         strem = io.BytesIO(json_data)
#         # provideing jsonparser dictionar
#         pythondata = JSONParser().parse(strem)
#         serializer = serializerstudent(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Data Inserted'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         else:
#             json_data = JSONRenderer().render(serializer.errors)
#             return HttpResponse(json_data, content_type='application/json')
    
#     # this is for update data
#     if request.method == 'PUT':
#         #save the data
#         json_data = request.body
#         #converting string
#         strem = io.BytesIO(json_data)
#         # provideing jsonparser dictionar
#         pythondata = JSONParser().parse(strem)
#         id = pythondata.get('id')
#         stu = Students.objects.get(id = id)
#         # this use for whole row data update
#         # serializer = serializerstudent(stu,data=pythondata)
#         # this is use for parserl update
#         serializer = serializerstudent(stu,data=pythondata,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'data updated!!!'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         else:
#             json_data = JSONRenderer().render(serializer.errors)
#             return HttpResponse(json_data, content_type='application/json')
        
#     # this is for delete data
#     if request.method == 'DELETE':
#         #save the data
#         json_data = request.body
#         #converting string
#         strem = io.BytesIO(json_data)
#         # provideing jsonparser dictionar
#         pythondata = JSONParser().parse(strem)
#         id = pythondata.get('id')
#         stu = Students.objects.get(id = id)
#         stu.delete()
#         res = {'msg':'delete data success!!'}
#         # json_data = JSONRenderer().render(res)
#         # return HttpResponse(json_data, content_type='application/json')
#         return JsonResponse(res,safe=False)
