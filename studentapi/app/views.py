from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views import View

class Studentdetails(View):
    def get(self,request):
        data={"studentname":"Amal","age":23,"course":"Bsc Cs","mark" : 76}

        return JsonResponse(data)

class StudentList(View):
    def get(self,request):
        data=[{"studentname":"Amal","age":23,"course":"Bsc Cs", "mark" : 76},
              {"studentname":"Alan","age":20,"course":"Python", "mark" : 96},
              {"studentname":"Laya","age":32,"course":"Dotnet", "mark" : 50}
              ]

        return JsonResponse(data,safe=False)