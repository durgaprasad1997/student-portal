
from django.views import View
from django.shortcuts import render,get_object_or_404,redirect

from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import *
from django.contrib.auth.mixins import LoginRequiredMixin


from django.shortcuts import render
import requests
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render


def viewStudents(request):

    response = requests.get('http://www.bhageerathreddy.com/mrnd-hackathon/2018/api/students/')
    data = response.json()


    return render(request, 'portal/students.html', {
        'student_list':data['message'],

    })



def viewStudentsPage(request,id):

    import ipdb
    response = requests.get('http://www.bhageerathreddy.com/mrnd-hackathon/2018/api/students?page='+str(id))
    data = response.json()

    data=data['message']


    paginator = Paginator(data, 10)


    page = request.GET.get('page')
    student = paginator.get_page(page)

    return render(request, 'portal/studentPage.html', {'contacts': student})

