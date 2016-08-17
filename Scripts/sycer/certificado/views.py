from django.shortcuts import render
from django.views.generic import ListView
from certificado.models import Certificado
from usuario.models import Usuario
from empresaCliente.models import EmpresaCliente
# Create your views here.
class CertificadoListView(ListView):
	model = Certificado
	template_name = 'certificado/certificado-list.html'
	#ordering = 'nombre'
	paginate_by = 10

	def get_queryset(self):
		usuario= Usuario.objects.get(user=self.request.user)
		#queryset= self.model.objects.filter(id_empresa=usuario.id_empresa)	
		queryset = self.model.objects.filter(id_empresa_cliente__id_empresa=usuario.id_empresa)
		return queryset
