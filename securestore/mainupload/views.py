from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from .serializers import FileSerializer


# Create your views here.


def index(request):
    return HttpResponse('hi')


def create_directory(request):
    pass


class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)