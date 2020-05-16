from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Dish, Calls, Call
from django.shortcuts import render


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('code', 'name', 'rating', 'kkal', 'price',)
class CallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calls
        fields = ('name', 'phone')
class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = ('id', 'name', 'phone')

def client(request):
    return render(request, "index.html")
def menu(request):
    return render(request, "menu.html")
def list(request):
    return render(request, "list.html")
def registration(request):
    return render(request, "registration.html")
def login(request):
    return render(request, "login.html")




@api_view(['GET', 'POST'])
def list_dishes(request):
    if request.method == "GET":
        dishes = Dish.objects.all()
        serializer = DishSerializer(dishes, many=True)
        return Response(serializer.data)
    else:  # Post
        serializer = DishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # Successful post
        return Response(serializer.errors, status=400)  # Invalid data

@api_view(['GET', 'DELETE', 'PUT'])
def dish_details(request, code):
    try:
        dish = Dish.objects.get(code=code)
    except:
        return Response(status=404)

    if request.method == 'GET':
        serializer = DishSerializer(dish)
        return Response(serializer.data)
    elif request.method == 'PUT':  # Update
        serializer = DishSerializer(dish, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Update table in DB
            return Response(serializer.data)

        return Response(serializer.errors, status=400)  # Bad request
    elif request.method == 'DELETE':
        dish.delete()
        return Response(status=204)

@api_view(['GET', 'POST'])
def list_calls(request):
    if request.method == "GET":
        calls = Call.objects.all()
        serializer = CallSerializer(calls, many=True)
        return Response(serializer.data)
    else:  # Post
        serializer = CallSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # Successful post

        return Response(serializer.errors, status=400)  # Invalid data


@api_view(['GET', 'DELETE', 'PUT'])
def call_details(request, pk):
    try:
        call = Call.objects.get(pk=pk)
    except:
        return Response(status=404)

    if request.method == 'GET':
        serializer = CallSerializer(call)
        return Response(serializer.data)
    elif request.method == 'PUT':  # Update
        serializer = CallSerializer(call, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Update table in DB
            return Response(serializer.data)

        return Response(serializer.errors, status=400)  # Bad request
    elif request.method == 'DELETE':
        call.delete()
        return Response(status=204)



