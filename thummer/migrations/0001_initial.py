# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'WebpageSnapshot'
        db.create_table('thummer_webpagesnapshot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, db_index=True)),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('capture_width', self.gf('django.db.models.fields.IntegerField')(default=1680)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('thummer', ['WebpageSnapshot'])


    def backwards(self, orm):
        
        # Deleting model 'WebpageSnapshot'
        db.delete_table('thummer_webpagesnapshot')


    models = {
        'thummer.webpagesnapshot': {
            'Meta': {'ordering': "[u'-created_at']", 'object_name': 'WebpageSnapshot'},
            'capture_width': ('django.db.models.fields.IntegerField', [], {'default': '1680'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'db_index': 'True'})
        }
    }

    complete_apps = ['thummer']
