# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Irasas.tekstas'
        db.add_column(u'einio_diary_irasas', 'tekstas',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Irasas.tekstas'
        db.delete_column(u'einio_diary_irasas', 'tekstas')


    models = {
        u'einio_diary.irasas': {
            'Meta': {'object_name': 'Irasas'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pavadinimas': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'tekstas': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['einio_diary']