from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
#from gunicorn.config import User
import json
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.generic import ListView,View
# Create your views here.
import socketio
#import os

from .models import *
#basedir = os.path.dirname(os.realpath(__file__))
async_mode = 'eventlet'
from django.http import JsonResponse


#from django.forms import inlineformset_factory
sio = socketio.Server(async_mode='eventlet',always_connect=True)
app = socketio.WSGIApp(sio)



def room_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        return redirect('home')
    context = {}
    return render(request, 'room.html', context)


class home_view(View):
    template_name = 'homee.html'
    
    global roomname
    


    def post(self,request):
        if request.method == 'POST':
            global roomname
            roomname = request.POST.get('username')
            #roomname = username
            print(roomname)
            id = self.kwargs.get('id')
            f = self.request.user
            #print(f)
            # check if user is in a group then returns true
            if self.check_group(f,roomname) == True:
                context = { 'room1': roomname,'theuser':request.user}
                return render(request, self.template_name, context)
            else:
                return redirect('room')

    @sio.event
    def me(sid, data):
        #m = json.loads(data)
        #print(m)

        #data['type'] = 'answer'
        m = json.loads(data)
        print(type(m['sdp']))
        l = m['sdp']
        l['peer'] = m['peer'] # created a peer attribute in l dictionary
        print(m)

        sio.emit('message2', l, to='first')
        print(data)



    @sio.event
    def message(sid, data):
        #m = json.loads(data)
        print('tyy',data)
        sio.emit('message', data , to='first')
        '''
        else:
            print('No vidmassage')
            print(m['group'])
            chat_user = User.objects.get(username=m['chat_user'])
            group = Groupss.objects.get(name=m['group'])
            #Chatmessage.objects.create(chat_user=chat_user, chat=group, message=m['message'])
            # then emit queryset to room
           # h = League.objects.create(Leaguename=data)
            #l = chat.objects.last()
            #print(type(str(l)) )
            print('messagee',m['group'])

            sio.emit('welcome', data, to=m['group'])
            print(sid, data, 'message')
    '''
    @sio.event
    def connect(sid, environ):
        sio.emit('message', 'welcome')
        username = environ.get('HTTP_X_USERNAME')

        roomname = environ.get('HTTP_X_ROOMNAME')
        print('usernama',username,roomname)
        print('room', roomname)
        print(sid, 'connected')
        g = Groupss.objects.get(name=roomname)
        user = User.objects.get(username=username)
        print(g.users.all())
        # checks if the user is in the list of users in the room
        if user in g.users.all():
            sio.enter_room(sid, roomname) # if yes then add user to room
            message = ('welcome to room'+''+roomname)
            sio.emit('conninfo', message, to=roomname)
        else:
            print('kklrf') # Raise validation error



    def check_group(self,theuser,thegroup):
        g = Groupss.objects.get(name=thegroup)
        print(g.users.all())
        if theuser in g.users.all():
            return True
        else:
            print('kklrf')


    #clubs = Clubs.objects.filter





def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        print(username,password)
        if user is not None:  # not none    means the user name is there in database                login(request, username)

            login(request, user)

            return redirect('room')
        else:
            messages.info(request, "Username OR Password is incorrect")  # you dont need to pass through context
    context = {}
    return render(request, 'login.html', context)





