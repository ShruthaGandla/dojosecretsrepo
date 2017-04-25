from django.shortcuts import render,redirect
from .models import User,Secret
from django.contrib import messages
from django.db.models import Count

def index(request):
    return render(request,"first_app/index.html")
def registrationLogic(request):
    if request.method == 'POST':
        list = User.objects.registration(request.POST['first_name'],request.POST['last_name'],request.POST['email'],request.POST['password'],request.POST['confirm_password'])
        if list:
            print list[0]
            userInstance=User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'],email=request.POST['email'],password=list[0])
            request.session['id'] = userInstance.id
            # messages.success(request, 'Succesfully registered or(logged in)')
            return redirect('/secrets')
        else:
            messages.error(request, 'Invalid Data')
            return redirect('/')
def loginLogic(request):
    if request.method == 'POST':
        try:
            userList = User.objects.filter(email=request.POST['email'])
            if(User.objects.login(userList[0].password,request.POST['password'])):
                # messages.success(request, 'Succesfully registered or(logged in)')
                request.session['id'] = userList[0].id
                return redirect('/secrets')
            else:
                messages.error(request, 'Incorrect Password')
                return redirect('/')
        except:
            messages.error(request, 'Incorrect Email ID')
            return redirect('/')




def secretLogic(request):
    userInstance = User.objects.get(id=request.session['id'])
    secretsList = Secret.objects.all().order_by('-id')[:10]
    # Secret.objects.all().order_by('-id')[:10].filter()

    context ={'userInstance':userInstance,
                'secretsList':secretsList}
    return render(request,"first_app/secrets.html",context)

def createSecret(request,id):
    userInstance = User.objects.get(id=id)
    Secret.objects.create(secret_message=request.POST['secret_message'],user=userInstance)
    return redirect('/secrets')

def deleteSecret(request,id):
    Secret.objects.get(id=id).delete()
    return redirect('/secrets')

# url(r'^like/(?P<id>\d+)$', views.createLike)
def createLikeFromLogin(request,id):
    likeHelper(request,id)
    # secretInstance = Secret.objects.get(id=id)
    # userInstance = User.objects.get(id=request.session['id'])
    # secretInstance.list_of_users_liked.add(userInstance)
    return redirect('/secrets')

def likeHelper(request,id):
    secretInstance = Secret.objects.get(id=id)
    userInstance = User.objects.get(id=request.session['id'])
    secretInstance.list_of_users_liked.add(userInstance)
    return None

def createLikeFromPopular(request,id):
    likeHelper(request,id)
    # secretInstance = Secret.objects.get(id=id)
    # userInstance = User.objects.get(id=request.session['id'])
    # secretInstance.list_of_users_liked.add(userInstance)
    return redirect('/mostpopular')

def mostPopular(request):
    userInstance = User.objects.get(id=request.session['id'])
    secretList = Secret.objects.annotate(num_likes=Count('list_of_users_liked')).order_by('-num_likes')
    context = {'secretList':secretList,
                "userInstance":userInstance}
    return render(request,"first_app/popular.html",context)
