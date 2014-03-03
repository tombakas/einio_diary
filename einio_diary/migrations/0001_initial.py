# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Irasas'
        db.create_table(u'einio_diary_irasas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pavadinimas', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
        ))
        db.send_create_signal(u'einio_diary', ['Irasas'])


    def backwards(self, orm):
        # Deleting model 'Irasas'
        db.delete_table(u'einio_diary_irasas')


    models = {
        u'einio_diary.irasas': {
            'Meta': {'object_name': 'Irasas'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pavadinimas': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'})
        }
    }

    complete_apps = ['einio_diary']