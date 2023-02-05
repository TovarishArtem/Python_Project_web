import datetime

import requests
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from pyexpat.errors import messages
from .forms import RegisterUserForm1, Skills
from .forms import AddPostForm
from .models import *



def index(request):
    block1 = Main_to_Geo.objects.all()

    return render(request, 'main/Index.html', {'block1': block1})

dect = {}

class RegisterUser(CreateView):
    form_class = RegisterUserForm1
    template_name = 'main/register.html'
    success_url = reverse_lazy('home')
# def register(request):
#     block1 = Main_to_Geo.objects.all()
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)
#             new_user.set_password(user_form.cleaned_data['password1'])
#             new_user.save()
#             dect = new_user
#             print('fewfwef')
#             reverse_lazy('home')
#     else:
#         user_form = UserRegistrationForm()
#     return render(request, 'main/register.html', {'user_form': user_form})

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'
    def get_success_url(self):
        return reverse_lazy('home')

class LogoutUser(LogoutView):
    next_page = reverse_lazy('home')


# def login(request):
#     block1 = Main_to_Geo.objects.all()
#     if request.method == 'POST':
#         user_form = AuthenticationForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)
#             new_user.set_password(user_form.cleaned_data['password1'])
#             new_user.save()
#             dect = new_user
#             print('fewfwef')
#
#             return render(request, 'main/Index.html', {'block1': block1})
#     else:
#         user_form = AuthenticationForm()
#     return render(request, 'main/login.html', {'user_form': user_form})



def error(request):
    return render(request, 'main/form_erorr.html')

def skills(request):
    if request.method == 'POST' and 'form1' in request.POST:
        pect = Pictures(
            pic=request.FILES['picture'],
            user=request.user,

            name=request.POST['name']
        )

        pect.save()
    if request.method == 'POST' and 'form2' in request.POST:
        pictures = Pictures.objects.all()
        pictures_send = PicturesSend(
            pic=request.FILES['picture_send'],
            user_get=int(request.POST['code']),
            user_set=request.user.id,
            name=(request.POST['name_send'])
        )
        print(request.user)
        pictures_send.save()
        pictures_send = PicturesSend.objects.all()
        return render(request, 'main/skills.html', { 'pictures': pictures, 'pictures_s': pictures_send})
    else:

        pictures = Pictures.objects.all()
        pictures_send = PicturesSend.objects.all()
        return render(request, 'main/skills.html', {'pictures': pictures, 'pictures_s': pictures_send})


class FormCreate(View):

    def get(self, request):
        if request.method == 'POST':
            form = AddPostForm(request.POST)
            if form.is_valid():

                print(form)
        else:
            form = AddPostForm()
        return render(request, 'main/form.html', {'form' : form})

    my_list = list()

    def post(self, request):

        return request.POST['digit']

class FormCreate(View):
    def get(self, request):
        if request.method == 'POST':
            form = AddPostForm(request.POST)
            if form.is_valid():

                print(form)
        else:
            form = AddPostForm()
        return render(request, 'main/form.html', {'form' : form, 'title' : 'Выберите число декабря'})

    def post(self, request):
                day = []
                day.append(request.POST['digit'])
                print(day)
                day1 = day[0]
                block_error = Last_vacancies.objects.all()
                try:

                    vacancies = requests.get(
                        f'https://api.hh.ru/vacancies?specialization=1&date_from=2022-12-{day1}T00:00:00&date_to=2022-12-{day1}T23:59:59&text=NAME:(Андроид+разработчик+OR+android+OR+android+developer)&only_with_salary=true&order_by=publication_time&per_page=10').json()['items']
                except:
                    return render(request, 'main/form_erorr.html', {'block_error': block_error})

                if len(vacancies) > 0:
                    jobs_list = []
                    for vac in vacancies:
                        jobs_list.append(requests.get(f'https://api.hh.ru/vacancies/{vac["id"]}').json())

                    list_vacancies = []
                    for vac in jobs_list:
                        vacancies_info = {
                            'name': vac['name'],
                            'description': vac['description'],
                            'key_skills': ', '.join(skill['name'] for skill in vac['key_skills']),
                            'employer': vac['employer']['name'],
                            'salary': f"{int((int(vac['salary']['from'] or 0) + int(vac['salary']['to'] or 0)) /2):,} {vac['salary']['currency']}",
                            'area': vac['area']['name'],
                            'published_at': datetime.datetime.strptime(vac['published_at'].replace('T', ' ')[:18], '%Y-%m-%d %H:%M:%S'),
                            'alternate_url': vac['alternate_url'],

                        }

                        list_vacancies.append(vacancies_info)
                    context = {"data": list_vacancies}
                    return render(request, 'main/last_vacancies.html',  context=context)

                return render(request, 'main/form_erorr.html', {'block_error': block_error})


def admin(request):
    return render(request, 'admin')


def demand(request):
    grafic1 = Main_to_Geo.objects.all()
    return render(request, 'main/demand.html', {'grafic1': grafic1})


def geo(request):

    grafic2 = Main_to_Geo.objects.all()
    return render(request, 'main/geo.html', {'grafic2': grafic2})