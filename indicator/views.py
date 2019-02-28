from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
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

'''
class Cmd_list(APIView):
   def get(self, request, format=None):
      queryset = LighthouseTest.objects.all()
      serializer = CmdSerializer(queryset, many=True)
      return Response(serializer.data)

class Cmd_detail(APIView):
   def get_object(self, cmd):
      try:
         return LighthouseTest.objects.get(cmd=cmd)
      except:
         raise Http404
   def get(self, request, cmd_id, format=None):
      res = self.get_object(cmd_id)
      serializer = CmdSerializer(res)
      return Response(serializer.data)

'''

class Cmd_list(mixins.ListModelMixin,
               generics.GenericAPIView):
   queryset = LighthouseTest.objects.all()
   serializer_class = CmdSerializer

   def get(self, request, *args, **kwargs):
      return self.list(request, *args, **kwargs)

class Cmd_detail(mixins.RetrieveModelMixin,
                 generics.GenericAPIView):
   queryset = LighthouseTest.objects.all()
   serializer_class = CmdSerializer
   lookup_field = 'cmd'

   def get(self, request, *args, **kwargs):
      return self.retrieve(request, *args, **kwargs)
