# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Certificado'
        db.create_table(u'certificado_certificado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_empresa_cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresaCliente.EmpresaCliente'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ruta', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('observacion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tipoCertificado.TipoCertificado'])),
            ('pesoArchivo', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'certificado', ['Certificado'])


    def backwards(self, orm):
        # Deleting model 'Certificado'
        db.delete_table(u'certificado_certificado')


    models = {
        u'certificado.certificado': {
            'Meta': {'object_name': 'Certificado'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_empresa_cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresaCliente.EmpresaCliente']"}),
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
        u'tipoCertificado.tipocertificado': {
            'Meta': {'object_name': 'TipoCertificado'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['certificado']