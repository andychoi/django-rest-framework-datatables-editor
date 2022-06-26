from django.urls import re_path, include
from django.contrib import admin
from rest_framework import routers

from albums import views

# router = DatatablesDefaultRouter()
router = routers.DefaultRouter()
router.register(r'albums', views.AlbumViewSet)
router.register(r'artists', views.ArtistViewSet)


urlpatterns = [
    re_path('^admin/', admin.site.urls),
    re_path('^api/', include(router.urls)),
    re_path('^$', views.index, name='albums')
]
