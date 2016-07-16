from django.conf.urls import url

from . import views

urlpatterns = [
   # url(r'^registro/$', views.registro_usuario_view, name='accounts.registro'),
       url(r'^$', views.index_view, name='usuario.index'),
    url(r'^login/$', views.login_view, name='usuario.login'),
    url(r'^logout/$', views.logout_view, name='usuario.logout'),
    url(r'^perfil/$', views.profile_view, name='usuario.perfil'),
    url(r'^editar_email/$', views.editar_email_view, name='usuario.editar_email'),

]