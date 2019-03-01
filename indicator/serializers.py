from rest_framework import serializers
from .models import Lighthouse


class CmdSerializer(serializers.ModelSerializer):
#class CmdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lighthouse
        fields = ("cmd", "act", "date_time", "visit_ip")
