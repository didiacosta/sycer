# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Certificado.municipio'
        db.add_column(u'certificado_certificado', 'municipio',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['municipio.Municipio']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Certificado.municipio'
        db.delete_column(u'certificado_certificado', 'municipio_id')


    models = {
        u'certificado.certificado': {
            'Meta': {'object_name': 'Certificado'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_empresa_cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresaCliente.EmpresaCliente']"}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['municipio.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'observacion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pesoArchivo': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'ruta': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tipoCertificado.TipoCertificado']"})
        },
        u'cliente.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'estado': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nit': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'departamento.departamento': {
            'Meta': {'object_name': 'Departamento'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'empresa.empresa': {
            'Meta': {'object_name': 'Empresa'},
            'estado': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nit': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'empresaCliente.empresacliente': {
            'Meta': {'object_name': 'EmpresaCliente'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cliente.Cliente']"}),
            'id_empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresa.Empresa']"})
        },
        u'municipio.municipio': {
            'Meta': {'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['departamento.Departamento']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'tipoCertificado.tipocertificado': {
            'Meta': {'object_name': 'TipoCertificado'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['certificado']