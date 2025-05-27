from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Communitie
from . import forms 


def comms_list(request):
    comms = Communitie.objects.all().order_by('-date')
    return render(request, 'comms/comms_list.html', {'comms': comms})

def comm_page(request, slug):
    comm = Communitie.objects.get(slug=slug)
    return render(request, 'comms/comm_page.html', {'comm': comm})

@login_required(login_url="/users/login/")
def comm_new(request):
    if request.method == 'POST': 
        form = forms.CreateComm(request.POST, request.FILES) 
        if form.is_valid():
            newcomm = form.save(commit=False) 
            newcomm.author = request.user 
            newcomm.save()
            return redirect('comms:list')
    else:
        form = forms.CreateComm()
    return render(request, 'comms/comm_new.html', { 'form': form })