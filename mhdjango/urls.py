from django.conf.urls import url, include
from rest_framework import routers
from mh_api import views
from django.contrib import admin


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'album', views.AlbumViewSet)
router.register(r'artist', views.ArtistViewSet)
router.register(r'song', views.SongViewSet)
router.register(r'genre', views.GenreViewSet)






urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
