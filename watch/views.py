from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection, connections
import requests
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import activity,myuser
from django.db import connection
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from django.db import connection

conn = connections['default']
cursor = conn.cursor()


# Create your views here.
def home(request):

    logged = request.session.get('user', 'False')
    if logged != True:
        return redirect("login")

    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM `watch_myuser` WHERE email = %s AND password = %s", [email, password])
        user = cursor.fetchone()
        cursor.close()
        if user:
            # login successful, do something
            request.session['user'] = True
            return redirect('home')
        else:            
            # login failed, show error message
            messages.error(request, 'Invalid email or password')
    return render(request, 'login.html')


def rajapalayam(request):
    logged = request.session.get('user', 'False')
    if logged != True:
        return redirect("login")

    return render(request,'rajapalayam.html')


def chetpet(request):
    logged = request.session.get('user', 'False')
    if logged != True:
        return redirect("login")
    return render(request, 'chetpet.html')


def media(request):
    cursor.execute("SELECT * FROM `activity` WHERE dept='media'")
    media = cursor.fetchall()
    return render(request,'media.html',{'media': media})


def accounts(request):
    cursor.execute("SELECT * FROM `activity` WHERE dept='accounts'")
    account = cursor.fetchall()
    return render(request,'accounts.html',{'account':account})

def database_developer(request):
    cursor.execute("SELECT * FROM `activity` WHERE dept='database developer'")
    d_dev = cursor.fetchall()
    return render(request,'database_developer.html',{'developer':d_dev})

def database(request):
    cursor.execute("SELECT * FROM `activity` WHERE dept='database'")
    databases = cursor.fetchall()
    return render(request,'database.html',{'database':databases})

def backup(request):
    cursor.execute("SELECT * FROM `activity` WHERE dept='backup'")
    backup = cursor.fetchall()
    return render(request,'backup.html',{'backup':backup})

def instagram(request):
    cursor.execute("SELECT * FROM `activity` WHERE dept='instagram'")
    instagram = cursor.fetchall()
    return render(request,'instagram.html',{'insta':instagram})

def instagram_chetpet(request):
    cursor.execute("SELECT * FROM `activity` WHERE dept='instagram_chetpet'")
    instagram_chetpet = cursor.fetchall()
    return render(request,'instagram_chetpet.html',{'insta_chet':instagram_chetpet})

def database_chetpet(request):
    cursor.execute("SELECT * FROM `activity` WHERE dept='database_chetpet'")
    database_chet = cursor.fetchall()
    return render(request,'database_chetpet.html',{'database_chet':database_chet})

def overallchetpet(request):
    #cursor.execute("SELECT * FROM `activity` WHERE dept='media'")
    cursor.execute("SELECT * FROM `activity` WHERE dept IN ('instagram_chetpet','database_chetpet')")

    overallchetpet= cursor.fetchall()
    return render(request,'overallchetpet.html',{'overallchetpet': overallchetpet})

def overallrajapalayam(request):
    #cursor.execute("SELECT * FROM `activity` WHERE dept='media'")
    cursor.execute("SELECT * FROM `activity` WHERE dept IN ('media', 'backup', 'instagram','database','accounts','database developer')")

    overallrajapalayam = cursor.fetchall()
    return render(request,'overallrajapalayam.html',{'overallrajapalayam': overallrajapalayam})

def logout(request):
    del request.session['user']
    return redirect('/')

@api_view(['POST'])
def getdataapiold(request):

    name = (request.data['Name'])
    api_key = (request.data['API-KEY'])
    pc_id = (request.data['PC-ID'])
    total_time = (request.data['Total-Time'])
    public_url = (request.data['Public-Url'])
    created_at = (request.data['created_at'])
    dept = (request.data['Dept'])

    # DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'activity_watch',
#         'USER': 'watch_activity',
#         'PASSWORD': 'Activity@123',
#         'HOST': '166.62.27.182',
#         'PORT': '3306',
#         'CONN_MAX_AGE': 500000,
#     }
# }

    
    sql = "INSERT INTO `activity` (name, total_time, pc_id, created_at, dept, public_url) VALUES (%s, %s, %s,%s,%s, %s)"
    values = (name, total_time, pc_id, created_at,dept, public_url)

    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, values)
            db.commit()
        print('success first attempt')
    except pymysql.OperationalError as e:
        if e.args[0] == 2013:
            # lost connection, attempt to reconnect
            print("Lost connection to MySQL server during query, attempting to reconnect...")
            time.sleep(5)
            db = pymysql.connect(host="localhost", user="root", password="", database="activity_watch")
            cursor = db.cursor()
        else:
            # re-raise other OperationalError types
            raise e

    return rest_response({"status":"200","Message":"Success"})



@api_view(['POST'])
def getdataapi(request):
    name = request.data['Name']
    total_time = request.data['Total-Time']
    pc_id = request.data['PC-ID']
    created_at = request.data['created_at']
    dept = request.data['Dept']
    public_url = request.data['Public-Url']
    api_key = request.data['API-KEY']
    

    if api_key != "123456789":
        print("Error")
        return Response({"Status":"400","Message":"Invalid API Key"})


    with connection.cursor() as cursor:
        # Execute the SQL query to insert a new row into the activity table
        cursor.execute(
            "INSERT INTO `activity` (name, total_time, pc_id, created_at, dept, public_url) VALUES (%s, %s, %s, %s, %s, %s)",
            [name, total_time, pc_id, created_at, dept, public_url]
        )

    return Response({"status": "200", "Message": "Success"})