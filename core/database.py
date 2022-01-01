from pymongo import MongoClient
import requests
from core.config import url, data, MAIN_URL


def DBMongoShow():
    client = MongoClient(url)
    db = client["spb-bot"]
    cursor = db["restaurants"].find({})
    return cursor


def DBMongoAdd(name, b):
    client = MongoClient(url)
    db = client["spb-bot"]
    if name is not None:
        db["restaurants"].insert_one(b)


def DBApiShow():
    session = requests.session()
    r = session.post(url=f'{MAIN_URL}auth/login', json=data)
    r = session.get(url=f'{MAIN_URL}interface_objects')
    return r


def DBApiAdd(objects, id):
    session = requests.session()
    r = session.post(url=f'{MAIN_URL}auth/login', json=data)
    r = session.post(url=f'{MAIN_URL}interface_objects/{id}', json=objects)
