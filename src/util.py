import urllib3
import json
import os

from datetime import datetime
import boto3
from boto3.dynamodb.conditions import Attr


def slack_call(payload:dict, webhook:str):
    try:
        header = {
            'Content-Type' : 'application/json'
        }
        http = urllib3.PoolManager()
        response = http.request( 
            method="POST", 
            url=webhook, 
            body=json.dumps(payload ), 
            headers=header
        )
        return response
    except Exception as ex: 
        print(ex)

def get_today():
    try:
        now = datetime.now()
        bisiesto = True if now.year%4 == 0 else False
        return now.day, now.month, now.year, bisiesto
    except Exception as ex:
        print(ex)

def get_tabla(name:str):
    try:
        session = boto3.session.Session(
            region_name = os.getenv('REGION')
        )
        resource = session.resource('dynamodb')
        tabla = resource.Table(name)
        return tabla
    except Exception as ex: 
        print(ex)

def get_specific(nombre_tabla:str, id:str):
    try:
        tabla = get_tabla(nombre_tabla)
        data = tabla.get_item(
            Key={
                'id':id
            }
        )
        if 'Item' in data: return [ data['Item'] ]
        else: 
            print(f'ID: "{id}" Not Found')
            exit()
    except Exception as ex:
        print(ex)

def get_all(nombre_tabla:str, day:int, month:int):
    try:
        tabla = get_tabla(nombre_tabla)
        data = tabla.scan(
            FilterExpression=Attr('day').eq(day) & Attr('month').eq(month)
        )['Items']
        return data
    except Exception as ex:
        print(ex)


