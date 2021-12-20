from time import asctime

from django.shortcuts import render
from pymongo import MongoClient

from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
import json
import requests
from requests.auth import HTTPBasicAuth

BOT_HOST = 'https://79d6-89-110-15-93.ngrok.io'
MAIN_URL = f'{BOT_HOST}/api/'


# Create your views here.
def home(request):
    url = 'mongodb+srv://places_spb:E34SBxaaz4qJ2PQ@places.cekmy.mongodb.net/test?authSource=admin&replicaSet=atlas-gv7ek5-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true'
    client = MongoClient(url)
    db = client["spb-bot"]
    cursor = db["restaurants"].find({})
    container = []
    a = {}
    for i in cursor:
        container.append(i)
        a = {
            "restic": container
        }
    return render(request, 'index.html', a)


def addpage(request):
    template = 'addrest.html'
    context = {

    }
    breakfast = False
    dinner = False
    lunch = False
    european = False
    authors = False
    italian = False
    asian = False
    vegetarian = False
    japan = False
    cafe = False
    restaurant = False
    bar = False
    shop = False
    req = request.GET
    id = req.get('id')
    name = req.get('name')
    breakfast = req.get('breakfast')
    dinner = req.get('dinner')
    lunch = req.get('lunch')
    european = req.get('european')
    authors = req.get('authors')
    italian = req.get('italian')
    asian = req.get('asian')
    vegetarian = req.get('vegetarian')
    japan = req.get('japan')
    cafe = req.get('cafe')
    restaurant = req.get('restaurant')
    bar = req.get('bar')
    shop = req.get('shop')
    mean_prices = req.get('mean_prices')
    links = req.get('links')
    description = req.get('description')
    address = req.get('address')
    picture = req.get('picture')
    time = req.get('time')
    district = req.get('district')
    a = req.get('a')
    c = req.get('b')
    b = {
        '_id': f'ObjectId{id}',
        'name': name,
        'type_of_meal': {'breakfast': breakfast, 'dinner': dinner, 'lunch': lunch},
        'type_of_food': {'italian': italian, 'european': european, 'vegetarian': vegetarian,
                         'authors': authors, 'japan': japan, 'asian': asian},
        'type_of_restaurant': {'cafe': cafe, 'restaurant': restaurant, 'bar': bar, 'shop': shop},
        'mean_prices': mean_prices,
        'links': links,
        'description': description,
        'address': address,
        'picture': picture,
        'time': time,
        'district': district,
        'location': {"type": "Point", 'coordinates': [float(a), float(c)]}
    }
    url = 'mongodb+srv://places_spb:E34SBxaaz4qJ2PQ@places.cekmy.mongodb.net/test?authSource=admin&replicaSet=atlas-gv7ek5-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true'
    client = MongoClient(url)
    db = client["spb-bot"]
    if name is not None:
        db["restaurants"].insert_one(b)
    print(b)
    return render(request, template, context)


def managebuttons(request):
    template = 'managebuttons.html'
    data = {"login": "admin", "password": "admin123"}
    session = requests.session()
    r = session.post(url="https://79d6-89-110-15-93.ngrok.io/api/auth/login", json=data)
    r = session.get(url="https://79d6-89-110-15-93.ngrok.io/api/interface_objects")
    container = []
    for i in r.json():
        if i["type"] == "keyboard":
            for k in i["buttons"]:
                container.append(k)
                buttons = {
                    "objects": container
                }
    for i in r.json():
        if i["type"] == "reply":
            container.append(i)
            replies = {
                "messages": container
            }
    print(buttons["objects"])
    context = {'buttons': buttons, 'replies': replies}
    req = request.GET
    id = req.get('id')
    object = req.get('object')
    type = req.get('type')
    text = req.get('text')
    title = req.get('title')
    platform = req.get('platform')
    created_at = req.get('created_at')
    updated_at = asctime()
    objects = {
        'object': object,
        'type': type,
        'text': text,
        'title': title,
        'platform': platform,
        'created_at': created_at,
        'updated_at': updated_at,
        'id': id}

    r = session.post(url=f'https://79d6-89-110-15-93.ngrok.io/api/interface_objects/{id}', json=objects)

    return render(request, template, context)


def addadmin(request):
    template = 'addadmin.html'
    context = {

    }
    req = request.GET
    login = req.get('login')
    password = req.get('password')
    if login != None:
        user = User.objects.create_superuser(username=login, password=password)

    return render(request, template, context)


def login(request):
    template = 'login.html'
    context = {

    }
    req = request.GET
    login = req.get('login')
    password = req.get('password')
    if login != None:
        user = auth.authenticate(username=login, password=password)
        if user is not None:
            auth.login(request, user=user)
            return redirect('home')
    return render(request, template, context)


def logout(request):
    auth.logout(request)
    return redirect('home')
