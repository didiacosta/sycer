from django.conf.urls import patterns,url

from certificado.views import CertificadoListView

urlpatterns = [
   # url(r'^registro/$', views.registro_usuario_view, name='accounts.registro'),
    url(r'^certificados/$', CertificadoListView.as_view(), name='certificado.certificado-list'),
 
]