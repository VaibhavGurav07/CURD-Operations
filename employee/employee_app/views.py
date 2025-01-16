from django.shortcuts import render,redirect
from .models import  Employee

# Create your views here.

def create(request):
    if (request.method == 'POST'):
        username=request.POST['uname']
        email=request.POST['email']
        msg = request.POST['msg']
        contact=request.POST['phone']

        m = Employee.objects.create(name=username,email=email,message=msg,number=contact)
        m.save()
        return render(request,'add.html')
    
def index(request):
    context = {}
    m=Employee.objects.all()
    context['data'] = m

    return render (request,'index.html',context)

def edit(request,sid):
    if request.method=='GET':
        m = Employee.objects.filter(id=sid)
        text={}
        text['data']=m
        return render (request,'edit.html',text)
    else:
        uesrname=request.POST['uname']
        email=request.POST['email']
        msg=request.POST['msg']
        contact=request.POST['phone']

        m=Employee.objects.filter(id=sid).update(name=uesrname,email=email, message=msg,number=contact)
        return redirect('main_file')
    
def delete(request,did):
    m=Employee.objects.filter(id=did).delete()
    return redirect('main_file')