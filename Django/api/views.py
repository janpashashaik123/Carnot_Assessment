from dataclasses import dataclass
import re
from django.shortcuts import render

# Create your views here.
import json
from django.conf import settings
import redis
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# Connect to our Redis instance
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT, db=0)
@api_view(['POST'])
def Fetch_Device_Info(request, *args, **kwargs):
    if request.method == 'POST':
        print(request.data.get('key'))
        if request.data.get('key'):
            value = redis_instance.get(request.data.get('key'))
            if value:
                response = {
                    'key': request.data.get('key'),
                    'value': json.loads(value)[0],
                    'msg': 'success'
                }
                return Response(response, status=200)
            else:
                response = {
                    'key': kwargs['key'],
                    'value': None,
                    'msg': 'Not found'
                }
                return Response(response, status=404)

@api_view(['POST'])
def Fetch_Location(request, *args, **kwargs):
    if request.method == 'POST':
        if request.data.get('key'):
            value = redis_instance.get(request.data.get('key'))
            # print(value)
            if value:
                loc=(json.loads(value)[0][0],json.loads(value)[0][1])
                
                response = {
                    'key': request.data.get('key'),
                    'value': loc,
                    'msg': 'success'
                }
                return Response(response, status=200)
            else:
                response = {
                    'key': kwargs['key'],
                    'value': None,
                    'msg': 'Not found'
                }
                return Response(response, status=404)


@api_view(['POST'])
def Fetch_List_of_Locations(request, *args, **kwargs):
    if request.method == 'POST':
        if request.data.get('key'):
            value = redis_instance.get(request.data.get('key'))
           
            print(value)
            if value:
                data=[]
                value=json.loads(value)
                for i in range(len(value)):
                    if value[i][2]>=request.data.get('start_time') and  value[i][2]<=request.data.get('end_time'):
                        data.append(value[i][0])
                        data.append(value[i][1])
                        data.append(value[i][2])
                response = {
                    'key': request.data.get('key'),
                    'value': data,
                    'msg': 'success'
                }
                return Response(response, status=200)
            else:
                response = {
                    'key': kwargs['key'],
                    'value': None,
                    'msg': 'Not found'
                }
                return Response(response, status=404)
    
    
