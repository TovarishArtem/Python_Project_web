from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include

from .views import FormCreate, LoginUser, RegisterUser, LogoutUser

urlpatterns = [
    path('', views.index, name='home'),
    path('last_vacancies', FormCreate.as_view(), name='last_vacancies'),
    path('admin', views.admin),
    path('error', views.error),
    path('demand', views.demand, name='demand'),
    path('geo', views.geo, name='geo'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', LogoutUser.as_view(), name='logout'),
    path('skills', views.skills, name='skills'),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)