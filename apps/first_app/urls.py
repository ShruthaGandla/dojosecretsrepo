from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [ url(r'^$', views.index),
url(r'^registration$', views.registrationLogic),
url(r'^login$', views.loginLogic),
url(r'^secrets$', views.secretLogic),
url(r'^createSecret/(?P<id>\d+)$', views.createSecret),
url(r'^delete/(?P<id>\d+)$', views.deleteSecret),
url(r'^like/(?P<id>\d+)$', views.createLikeFromLogin),
url(r'^mostpopular$', views.mostPopular),
url(r'^like2/(?P<id>\d+)$', views.createLikeFromPopular)
]
