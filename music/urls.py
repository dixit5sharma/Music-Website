from django.conf.urls import url
from . import views

app_name = "music"  # This restricts the scope of defined names within the app by writing music:index / music:detail
urlpatterns = [
# /music/
    url(r'^$', views.IndexView.as_view(), name="index"),
# /music/
    url(r'^register/$', views.UserFormView.as_view(), name="register"),
# # /music/712/
    url(r"^(?P<pk>[0-9]+)/$", views.DetailView.as_view(), name="detail"),
# # /music/712/favourite
#     url(r"^(?P<album_id>[0-9]+)/favourite/$", views.favourite, name="favourite"),
    # /music/album/add/
    url(r"^album/add/$", views.AlbumCreate.as_view(), name="album-add"),

    # /music/album/4/
    url(r"^album/(?P<pk>[0-9]+)/$", views.AlbumUpdate.as_view(), name="album-update"),
    # /music/album/4/delete/
    url(r"^album/(?P<pk>[0-9]+)/delete/$", views.AlbumDelete.as_view(), name="album-delete"),
]