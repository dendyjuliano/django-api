from django.shortcuts import render
from django.http import JsonResponse

# third party imports
from rest_framework.response import Response
from rest_framework.views import APIView

class TestView(APIView):
    def get(self,request,*args,**kwargs):
        data = {
            'name':'jhon',
            'age':17,
        }
        return Response(data)

# def test_view(request):
    # data = {
    #     'name':'jhon',
    #     'age':17,
    # }
#     return JsonResponse(data)
