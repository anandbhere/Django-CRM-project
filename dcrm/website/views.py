from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages  
from .forms import SignupForm,AddRecordForm
from .models import Record

def home(request):
    records = Record.objects.all()
    #check to c if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        #Authenticate
        user = authenticate(request, username=username , password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.success(request,"There is error in logging in")
            return redirect('home')

    else: 
        return render(request,'home.html', {'records' : records})
    

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)    #Taking the form created in forms.py and posting trough it
        if form.is_valid():            #validating the form 
            form.save()                    #if valid form then saving it

    #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,f"{user.first_name} You have been Successfully registered ")
            return redirect('home')
    
    else:
        form = SignupForm()
        return render(request,'register.html',{'form':form})

    return render(request,'register.html',{'form':form})


# def login_user(request):        #need this if u hv seperate login page In this project we r creating login form in home page
#     pass

def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id = pk)
        return render(request,'record.html',{'customer_record':customer_record})
    else:
        messages.success(request,"You must be Logged in first")
        return redirect('home')
    


def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_record = Record.objects.get(id=pk)
        delete_record.delete()
        messages.success(request,"Record has been deleted successfully")
        return redirect('home')
    

    else:
        messages.success(request,"You must be Logged in first")
        return redirect('home')
    


def add_record(request):
        form = AddRecordForm(request.POST or None)
        if request.user.is_authenticated:
            if request.method == "POST":
                if form.is_valid():
                    add_record = form.save()
                    messages.success(request,f"Record of {add_record.first_name} is added Successfully")
                    return redirect('home')
                
            return render(request,'add_record.html',{'form':form})
        else:
            messages.success(request,"You must Logged in first")
            return redirect('home')
                 
def update_record(request,pk):
    if request.user.is_authenticated:
        update_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None,instance=update_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record Has been updated")
            return redirect('home')
        return render(request,'update_record.html',{'form':form})    
    else:
        messages.success(request,"You must Logged in first")
        return redirect('home')


