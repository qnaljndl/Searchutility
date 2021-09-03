# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from rest_framework import status, generics, filters, permissions
from snippets.serializers import SnippetSerializer, UserSerializer, MapSearchSerializer
from snippets.models import Snippet, Maps_Search_autocomplete
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView


class Search(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        value = request.query_params.get('query')
        if value is not None:
            payload = {'key': 'AIzaSyAcRq3Sd8Fq-ZKFxWW8AQxiiF_v0xm679s', 'input': value}
            try:
                response = requests.get('https://maps.googleapis.com/maps/api/place/autocomplete/json', params=payload)
                search_place = {'search_place': value}
                serializer = MapSearchSerializer(data=search_place)
                if serializer.is_valid():
                    serializer.save()
                    return Response(response.json(), status=status.HTTP_302_FOUND)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


class UserSearch(APIView):

    def get(self, request, format=None):
        value = request.query_params.get('query')
        userid = request.query_params.get('userid')
        print(request)
        if value is not None:
            payload = {'key': 'AIzaSyAcRq3Sd8Fq-ZKFxWW8AQxiiF_v0xm679s', 'input': value}
            response = requests.get('https://maps.googleapis.com/maps/api/place/autocomplete/json', params=payload)
            search_place = {'search_place': value, 'user_id': userid}
            serializer = MapSearchSerializer(data=search_place)
            if serializer.is_valid():
                serializer.save()
                return Response(response.json(), status=status.HTTP_302_FOUND)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        value = request.data.get('search_place')
        if value is not None:
            payload = {'key': 'AIzaSyAcRq3Sd8Fq-ZKFxWW8AQxiiF_v0xm679s', 'input': value}
            response = requests.get('https://maps.googleapis.com/maps/api/place/autocomplete/json', params=payload)
            serializer = MapSearchSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(response.json(), status=status.HTTP_302_FOUND)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class SnippetList(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_302_FOUND)

    def post(self, request, format=None):
        print(request)
        print(request.data)
        print(type(request.data))
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class SnippetDetail(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data, status=status.HTTP_302_FOUND)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Userlist(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format=None):
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_202_ACCEPTED)



