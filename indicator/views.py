from django.shortcuts import render
#from django.http import HttpResponse, JsonResponse
from django.http import HttpResponse
#from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import LighthouseTest
from .serializers import CmdSerializer


# Create your views here.
'''
class ListCmdView(generics.ListAPIView):

   queryset = LighthouseTest.objects.all()
   serializer_class = CmdSerializer
'''

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
'''

@api_view(['GET'])
def cmd_list(request, format=None):
   if request.method == 'GET':
      queryset = LighthouseTest.objects.all()
      serializer = CmdSerializer(queryset, many=True)
      return Response(serializer.data)

@api_view(['GET'])
def cmd_detail(request, cmd_id, format=None):
   if request.method == 'GET':
      try:
         res = LighthouseTest.objects.get(cmd=cmd_id)
      except:
         return Response(status=status.HTTP_404_NOT_FOUND)

      serializer = CmdSerializer(res)
      return Response(serializer.data)
