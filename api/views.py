from rest_framework.views import APIView
from rest_framework import generics
from .serializers import *
from .models import *

class GetRichtungeItems(generics.ListAPIView):
    serializer_class = RichtungenSerializer
    queryset = Richtungen.objects.all()


class GetRichtungeItem(generics.RetrieveAPIView):
    serializer_class = RichtungenItemSerializer

    def get_object(self):
        return Richtungen.objects.get(name_slug=self.request.query_params.get('slug'))

class GetTableItems(generics.ListAPIView):
    serializer_class = TableSerializer
    queryset = HilfreicheTabellen.objects.all()


class GetTableItem(generics.RetrieveAPIView):
    serializer_class = TableItemSerializer

    def get_object(self):
        return HilfreicheTabellen.objects.get(name_slug=self.request.query_params.get('slug'))

