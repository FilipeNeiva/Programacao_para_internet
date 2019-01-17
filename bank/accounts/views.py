from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Account
from .serializers import AccountSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def account_list(request):

    if request.method == 'GET':
        accounts = Account.objects.all()
        account_serializer = AccountSerializer(accounts, many=True)
        return Response(account_serializer.data)

    elif request.method == 'POST':
        account_serializer = AccountSerializer(data=request.data)
        if account_serializer.is_valid():
            account_serializer.save()
            return Response(account_serializer.data, status=status.HTTP_201_CREATED)

        return Response(account_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def account_detail(request, id):
    try:
        account = Account.objects.get(pk=id)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        account_serializer = AccountSerializer(account)
        return Response(account_serializer.data)

    elif request.method == 'PUT':
        account_serializer = AccountSerializer(account, data=request.data)

        if account_serializer.is_valid():
            account_serializer.save()
            return Response(account_serializer.data, status=status.HTTP_201_CREATED)

        return Response(account_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PATCH':

        print(request.data['balance'])

        account_serializer = AccountSerializer(account, data=request.data, partial=True)

        if account_serializer.is_valid():
            account_serializer.save()
            return Response(account_serializer.data, status=status.HTTP_200_OK)

        return Response(account_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
