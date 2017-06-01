from django.conf.urls import url
from . import views

app_name = 'pogon'

urlpatterns = [
    # /linija/
    url(r'^$', views.gosti, name='gosti'),
    url(r'^ploca/$', views.ploca, name='ploca'),
    url(r'^dokumentacija/$', views.dokumentacija, name='dokumentacija'),
    url(r'^parametri/$', views.parametri, name='parametri'),
    url(r'^prijava/$', views.prijava, name='prijava'),
    url(r'^odjava/$', views.odjava, name='odjava'),

    # /dokumentacija/392/
    #url(r'^(?P<kreirao_id>[0-9]+)/$', views.detail, name='detail'),
    #url(r'^(?P<kreirao_id>[0-9]+)/dokumentacija/$', views.novi_ulaz, name='novi_ulaz'),
]
