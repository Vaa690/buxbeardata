from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class NokeWebhookView(APIView):

    def post(self, request):
        authentication_classes = (TokenAuthentication,)
        permission_classes = (IsAuthenticated,)

        print('Got webhook from Noke')
        print(request)
        print(request.data)
        return Response(None, status=200)



class DialpadWebhookView(APIView):

    def post(self, request):
        authentication_classes = (TokenAuthentication,)
        permission_classes = (IsAuthenticated,)

        print('Got webhook from dialpad')
        print(request)
        print(request.data)
        return Response(None, status=200)
