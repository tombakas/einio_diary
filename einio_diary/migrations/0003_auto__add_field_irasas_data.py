# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Irasas.data'
        db.add_column(u'einio_diary_irasas', 'data',
                      self.gf('django.db.models.fields.DateField')(auto_now=True, default=datetime.datetime(2014, 3, 1, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Irasas.data'
        db.delete_column(u'einio_diary_irasas', 'data')


    models = {
        u'einio_diary.irasas': {
            'Meta': {'object_name': 'Irasas'},
            'data': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pavadinimas': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'tekstas': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['einio_diary']