# from django.shortcuts import render

# # Create your views here.

# from django.http import JsonResponse

# def ping(request):
#     return JsonResponse({"message": "pong"})

from django.http import JsonResponse

def ping(request):
    return JsonResponse({"message": "Hello from Django backend!"})
