from rest_framework import serializers
from .models import LighthouseTest


class CmdSerializer(serializers.ModelSerializer):
#class CmdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LighthouseTest
        fields = ("cmd", "act")
