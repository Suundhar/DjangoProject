# views.py
from django.shortcuts import render,redirect
from django.contrib import messages

from .models import users
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')


def appointment(request):
    return render(request, 'appointment.html')


def contact(request):
    return render(request, 'contact.html')

def error(request):
    return render(request, "404.html")
def feature(request):
    return render(request, "feature.html")

def service(request):
    return render(request, "service.html")

def team(request):
    return render(request, "team.html")
def testimonial(request):
    return render(request, "testimonial.html")
def appointment_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        date = request.POST.get('date')
        time = request.POST.get('time')
        doctor = request.POST.get('doctor')
        problem = request.POST.get('problem')

        if not all([name, email, mobile, date, time, doctor, problem]):
            messages.error(request, 'Please fill in all fields.')
            return redirect('appointment')

        count = users.count_documents({"mobile": mobile})
        if count == 0:
            record = {
                'name': name,
                'email': email,
                'mobile': mobile,
                'date': date,
                'time': time,
                'doctor': doctor,
                'problem': problem
            }
            users.insert_one(record)
            messages.success(request, 'Appointment booked successfully.')
        else:
            messages.error(request, 'You have already booked an appointment.')

    return redirect('appointment.html')

def login(request):
    return render(request, 'loginuser.html')
def updateuser(request):
    if "Update" in request.GET:
        name=request.GET['name']
        email=request.GET['email']
        mobile=request.GET['mobile']
        date=request.GET['date']
        time=request.GET['time']
        users.update_one({"uname":uname},{"$set":{"name":name,"email":email,"mobile":mobile,"date":date,"time":time}})
        current_user=users.find({"name":name})
        return render(request,"dashboard.html",{'user':current_user[0]})
    elif "delete" in request.GET:
        name=request.GET['name']
        users.delete_many({'name':name})
        del request.session['name']
        return render(request,'contact.html')
    elif "logout" in request.GET:
        del request.session['name']
        return render(request,'contact.html')
def loginuser(request):
    if request.method == 'POST':
        # your login logic here
        return render(request, 'home/loginuser.html')
    else:
        return render(request, 'home/loginuser.html')