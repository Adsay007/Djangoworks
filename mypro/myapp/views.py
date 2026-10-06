from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# def First(request):

#     if(request.method=="GET"):
#         return HttpResponse("First Page")

# def Second(request):

#     if(request.method=="GET"):
#         return HttpResponse("Second Page")

from django.views import View

class First(View):
    def get(self,request):
        return HttpResponse("First Page")

class Second(View):
    def get(self,request):
        return HttpResponse("Second Page")