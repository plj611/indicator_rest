from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from .models import LighthouseTest
from .serializers import CmdSerializer


# Create your views here.
'''
class ListCmdView(generics.ListAPIView):

   queryset = LighthouseTest.objects.all()
   serializer_class = CmdSerializer
'''

def cmd_list(request):
   if request.method == 'GET':
      queryset = LighthouseTest.objects.all()
      serializer = CmdSerializer(queryset, many=True)
      return JsonResponse(serializer.data, safe=False)

def cmd_detail(request, cmd_id):
   if request.method == 'GET':
      try:
         res = LighthouseTest.objects.get(cmd=cmd_id)
      except:
         return HttpResponse(status=404)

   if request.method == 'GET':
      serializer = CmdSerializer(res)
      return JsonResponse(serializer.data, safe=False)
