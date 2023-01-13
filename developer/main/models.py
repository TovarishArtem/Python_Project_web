from django.db import models

# Create your models here.
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

class Grafics(models.Model):
    title = models.CharField('Название', max_length=50)
    grafic = models.ImageField('График', blank=True,  upload_to='images/')
    bd = models.Field

    def __str__(self):
        return self.title