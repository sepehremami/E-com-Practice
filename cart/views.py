from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import CacheResponseMixin
from rest_framework.decorators import api_view, cache_page


class MyAPIView(CacheResponseMixin, APIView):
    def get(self, request):
        # Your view logic here
        return Response(...)
