from ast import Not
from multiprocessing import context
import re
from django.shortcuts import redirect, render
from .models import Room, Topic
from .forms import RoomForm
from django.conf.urls.static import static
import os
import requests
# Create your views here.

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    rooms = Room.objects.filter(topic__name__contains=q)
    topics = Topic.objects.all()
    context = { 'rooms': rooms,'topics':topics }
    return render(request, 'dashboard/home.html',context=context)
def room(request,pk=None):
    if pk == None:
        return render(request, 'dashboard/room.html')
    rooms = Room.objects.all()
    for i in rooms:
        if i.pk == int(pk):
            room = i
    context = { 'room': room }   
    return render(request, 'dashboard/room.html',context=context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'dashboard/room_form.html',context=context)

def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form':form}
    return render(request, 'dashboard/room_form.html',context=context)      

def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    print(request)
    if request.method =='POST':
        print(request)
        room.delete()
        return redirect('/')
    context = {'obj':room}
    return render(request, 'dashboard/delete.html',context)
def login(request):
    if request.method == 'POST':
        link = request.POST.get('username')
        command = f'youtube-dl -e -f best "{link}" --get-url'
        res = os.popen(command).read().split('\n')
        print(res[0])
        context = {'title':res[0], 'link':res[1]}
        print(context)
        # return redirect('/login',context=context)
        return render(request, 'dashboard/download.html',context=context)
    return render(request, 'dashboard/login_register.html')

def download(request):
    return render(request, 'dashboard/download.html')

def getLink(studentID):
    url = f"https://usis.bracu.ac.bd/academia/docuJasper/index?studentId={studentID}&reportFormat=PDF&old_id_no={studentID}&strMessage=&scholarProgramMsg=&companyLogo=%2Fvar%2Facademia%2Fimage%2FuniversityLogo%2F1571986355.jpg&companyName=BRAC+University&headerTitle=GRADE+SHEET&companyAddress=66%2C+MOHAKHALI+C%2FA%2C+DHAKA+-+1212.&academicStanding=Satisfactory&gradeSheetBackground=%2Fbits%2Fusis%2Ftomcat%2Fwebapps%2Facademia%2Fimages%2FgradeSheetBackground.jpg&_format=PDF&_name={studentID}&_file=student%2FrptStudentGradeSheetForStudent.jasper"
    return url

def secretsheet(request):
    if request.method == 'POST':
        studentid = request.POST.get('studentid')
        passcode = request.POST.get('passcode')
        if passcode == "JoyBangla":
            link = getLink(studentid)
            print(link)
            context = {'result':link}
            return render(request, 'dashboard/secretsheetresult.html',context=context)
    return render(request, 'dashboard/secretsheet.html')