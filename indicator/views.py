from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import status
from .models import Lighthouse
from .serializers import CmdSerializer
import datetime


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
   queryset = Lighthouse.objects.all()
   serializer_class = CmdSerializer

   def get(self, request, *args, **kwargs):
      return self.list(request, *args, **kwargs)

'''
class Cmd_detail(mixins.RetrieveModelMixin,
                 generics.GenericAPIView):
   queryset = Lighthouse.objects.all()
   serializer_class = CmdSerializer
   lookup_field = 'cmd'

   def get(self, request, *args, **kwargs):
#      res = Lighthouse.objects.get(cmd = kwargs['cmd'])
      res = Lighthouse.objects.order_by('-create_date_time').filter(cmd = kwargs['cmd'])[0]
      res.visit_ip = request.META['REMOTE_ADDR']
      res.save()
      print('**********************')
      return self.retrieve(request, *args, **kwargs)
'''

class Cmd_detail(APIView):

   permission_classes = (permissions.IsAuthenticated, )

   def get_object(self, cmd_id, request):
      try:
         res = Lighthouse.objects.order_by('-create_date_time').filter(cmd = cmd_id)[0]
#         res = Lighthouse.objects.order_by('-create_date_time')[0]
         res.visit_ip = request.META['REMOTE_ADDR']
         res.visit_date_time = datetime.datetime.utcnow()
         res.save()
         return res
      except:
         raise Http404

   def get(self, request, cmd, format=None):
      res = self.get_object(cmd, request)
      serializer = CmdSerializer(res)
      return Response(serializer.data)

   def put(self, request, cmd, format=None):
      print('Hi\n')
      print(request.data)
      res = self.get_object(cmd, request)
      serializer = CmdSerializer(res, request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
