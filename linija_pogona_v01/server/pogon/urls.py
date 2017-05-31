from django.conf.urls import url
from . import views

app_name = 'pogon'

urlpatterns = [
    # /linija/
    url(r'^$', views.gosti, name='gosti'),
    url(r'^ploca/$', views.ploca, name='ploca'),
    url(r'^dokumentacija/$', views.dokumentacija, name='dokumentacija'),
    url(r'^formular/$', views.formular, name='formular'),
    url(r'^detaljno/$', views.detaljno, name='detaljno'),
    url(r'^prijava/$', views.prijava, name='prijava'),
    url(r'^odjava/$', views.odjava, name='odjava'),

    # formular za unos parametara procesa
    # url(r'^(?P<operater_id>[0-9]+)/i-parametara/$', views.novi_parametri, name='novi_parametri'),
]
