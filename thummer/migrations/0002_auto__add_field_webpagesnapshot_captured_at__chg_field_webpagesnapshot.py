# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'WebpageSnapshot.captured_at'
        db.add_column('thummer_webpagesnapshot', 'captured_at', self.gf('django.db.models.fields.DateTimeField')(null=True), keep_default=False)

        # Changing field 'WebpageSnapshot.created_at'
        db.alter_column('thummer_webpagesnapshot', 'created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        for obj in orm['thummer.WebpageSnapshot'].objects.all():
            obj.captured_at = obj.created_at
            obj.save()


    def backwards(self, orm):
        
        # Deleting field 'WebpageSnapshot.captured_at'
        db.delete_column('thummer_webpagesnapshot', 'captured_at')

        # Changing field 'WebpageSnapshot.created_at'
        db.alter_column('thummer_webpagesnapshot', 'created_at', self.gf('django.db.models.fields.DateTimeField')())


    models = {
        'thummer.webpagesnapshot': {
            'Meta': {'ordering': "[u'-captured_at']", 'object_name': 'WebpageSnapshot'},
            'capture_width': ('django.db.models.fields.IntegerField', [], {'default': '1680'}),
            'captured_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'default': "u''", 'max_length': '200', 'db_index': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['thummer']
