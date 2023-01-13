from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include

from .views import FormCreate

urlpatterns = [
    path('', views.index, name='home'),
    path('demand', FormCreate.as_view(), name='demand'),
    path('admin', views.admin),
    path('error', views.error)

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)