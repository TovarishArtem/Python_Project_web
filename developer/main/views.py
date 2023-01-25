import datetime

import requests
from django.shortcuts import render, redirect
from django.views import View
from pyexpat.errors import messages

from .forms import AddPostForm
from .models import *


def index(request):
    block1 = Main_to_Geo.objects.all()

    return render(request, 'main/Index.html', {'block1': block1})


def error(request):
    return render(request, 'main/form_erorr.html')


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