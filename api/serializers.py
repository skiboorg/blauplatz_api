from rest_framework import serializers
from .models import *
from user.models import User



class RichtungenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Richtungen
        fields = [
            'id',
            'name',
            'name_slug',
            'icon',
        ]

class RichtungenItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Richtungen
        fields = [
            'name',
            'image',
            'text',
        ]

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = HilfreicheTabellen
        fields = [
            'id',
            'name',
            'name_slug',
        ]

class TableItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HilfreicheTabellen
        fields = [
            'name',
            'table',
        ]