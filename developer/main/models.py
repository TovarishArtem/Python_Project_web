from django.conf import settings
from django.contrib.auth.models import User

from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

from django.db import models
from django.conf import settings
from django.db import models



def image_thumbnail(self):
    return '<div class="panel-heading post-heading1"><img src="%s"/></div>' % (self.grafic)


image_thumbnail.allow_tags = True
image_thumbnail.short_description = 'Image Breif'
@property
def photo_url(self):
    if self.photo and hasattr(self.photo, 'url'):
        return self.photo.url

def user_directory_path(instance, filename):
    # путь, куда будет осуществлена загрузка MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Main_to_Geo(models.Model):
    text_definition = models.TextField('Определение', max_length=1000)
    text_what_doing = models.TextField('Что делает Android-разработчик?', max_length=1000)
    text_tools = models.TextField('Иструменты Android-разработчика ', max_length=1000)
    android_plus = models.TextField('Плюсы Android-разработчика ', blank=True, )
    android_minus = models.TextField('Минусы Android-разработчика ', blank=True,)
    text_skills = models.TextField('Навыки', blank=True, max_length=500)
    learn_uni = models.TextField('Обучение в ВУЗе', blank=True, max_length=500)
    learn_web_site = models.TextField('Обучение на Онлайн-курсах', blank=True, max_length=500)
    learn_self = models.TextField('Самообучение', blank=True, max_length=500)
    text_what_know_for_work =  models.TextField('Что должен знать Android-разработчика', blank=True)

    grafic_demand = models.ImageField('График Востребованности', blank=True,  upload_to='images/')
    grafic_geo = models.ImageField('График География', blank=True, upload_to='images/')
    bd = models.Field

    def __str__(self):
        return self.text_definition

class Last_vacancies(models.Model):
    title_form_error = models.TextField('Вывод ошибки', max_length=50)
    text_form_error = models.TextField('Действие устранение ошибки', max_length=50)
    bd = models.Field

    def __str__(self):
        return self.title_form_error


class Pictures(models.Model):
    name = models.CharField('Название', null=True, max_length=100)
    pic = models.ImageField( blank=True,  upload_to='images/')
    user = models.ForeignKey(User,
                             on_delete= models.PROTECT,
                             null=True,
                             )

class PicturesSend(models.Model):
    name = models.CharField('Название', null=True, max_length=100)
    pic = models.ImageField( blank=True,  upload_to='images/')
    user_set = models.IntegerField(
                             null=True,
                             )
    user_get = models.IntegerField(
        null=True,
    )

class Profile(models.Model):
    name = models.CharField('Имя', null=True, max_length=100)
    surname = models.CharField('Фамилия', null=True, max_length=100)
    user = models.OneToOneField(User,
                             unique=True,
                             on_delete= models.PROTECT,
                             null=True,
                             )
class Friend(models.Model):
    user_to = models.IntegerField(null=True,)
    user_from = models.IntegerField(null=True,)
