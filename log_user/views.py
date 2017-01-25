from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.views.generic import View
from .forms import UserForm
from django.core.urlresolvers import reverse



def logout1(request):
    user = request.user.username
    logout(request)
    context = {'user':user}
    return render (request, 'log_user/logout.html', context)

def register_sussess(request):
    return render (request, 'log_user/successful_registration.html')

def login1(request):
    form = UserForm ()
    context = {'form':form}
    
    if request.method == 'POST':
        form = UserForm(request.POST)

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate (username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('paragony:lista_paragonow')
        else:
            context['flag'] = True
    
    return render(request, 'log_user/login.html', context)


def register1(request):
    form = UserForm ()
    context =  {'form': form}
    
    if request.method == 'POST':
        form = UserForm (request.POST)

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate (username=username, password=password)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(password)
            user.save()
            return HttpResponseRedirect('/regsuccess/')
        else:
            context['flag'] = True
    return render(request, 'log_user/register.html', context)

@login_required
def user_loged(request):
    user=request.user.username
    quaryset = Pytania.objects.filter(user=user).values('carddeck').distinct()
    context = {'pytania':quaryset,}
    return render (request, 'user_loged.html', context)
