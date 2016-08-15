from django.conf.urls import patterns,url

from empresaCliente.views import EmpresaClienteListView,EmpresaClienteDetailView, EmpresaClienteUpdateView, EmpresaClienteCreateView

urlpatterns = [
   # url(r'^registro/$', views.registro_usuario_view, name='accounts.registro'),
    url(r'^clientes/$', EmpresaClienteListView.as_view(), name='empresaCliente.empresaCLiente-list'),
    url(r'^editarCliente/(?P<pk>[\w\-]+)/$', EmpresaClienteUpdateView.as_view(), name='empresaCliente.editarEmpresaCliente'),
    url(r'^crearCliente/$', EmpresaClienteCreateView.as_view(), name='empresaCliente.crearEmpresaCliente'),
]