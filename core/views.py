from time import asctime
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from core.database import DBMongoShow, DBMongoAdd, DBApiShow, DBApiAdd


# Create your views here.
def home(request):
    cursor = DBMongoShow()
    container = []
    context = {}
    for i in cursor:
        container.append(i)
        context = {
            "restic": container
        }
    return render(request, 'index.html', context)


def addpage(request):
    template = 'addrest.html'
    context = {

    }
    req = request.GET
    id = req.get('id')
    id = f'ObjectId("{id}")'
    name = req.get('name')
    breakfast = True if req.get('breakfast') == 'True' else False
    dinner = True if req.get('dinner') == 'True' else False
    lunch = True if req.get('lunch') == 'True' else False
    european = True if req.get('european') == 'True' else False
    authors = True if req.get('authors') == 'True' else False
    italian = True if req.get('italian') == 'True' else False
    asian = True if req.get('asian') == 'True' else False
    vegetarian = True if req.get('vegetarian') == 'True' else False
    japan = True if req.get('japan') == 'True' else False
    cafe = True if req.get('cafe') == 'True' else False
    restaurant = True if req.get('restaurant') == 'True' else False
    bar = True if req.get('bar') == 'True' else False
    shop = True if req.get('shop') == 'True' else False
    mean_prices = req.get('mean_prices')
    link = req.get('link')
    description = req.get('description')
    address = req.get('address')
    picture = req.get('picture')
    time = req.get('time')
    district = req.get('district')
    a = req.get('a')
    c = req.get('b')
    if name is not None and name != '':
        b = {
            'name': name,
            'type_of_meal': {'breakfast': breakfast, 'dinner': dinner, 'lunch': lunch},
            'type_of_food': {'italian': italian, 'european': european, 'vegetarian': vegetarian,
                             'authors': authors, 'japan': japan, 'asian': asian},
            'type_of_restaurant': {'cafe': cafe, 'restaurant': restaurant, 'bar': bar, 'shop': shop},
            'mean_prices': mean_prices,
            'links': link,
            'description': description,
            'address': address,
            'picture': picture,
            'time': time,
            'district': district,
            'location': {"type": "Point", 'coordinates': [float(a), float(c)]}
        }
        DBMongoAdd(name, b)
    return render(request, template, context)


def managebuttons(request):
    template = 'managebuttons.html'
    container = []
    r = DBApiShow()
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
    DBApiAdd(objects, id)
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
