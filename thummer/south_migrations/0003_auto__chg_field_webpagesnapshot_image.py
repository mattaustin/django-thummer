# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'WebpageSnapshot.image'
        db.alter_column('thummer_webpagesnapshot', 'image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True))


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'WebpageSnapshot.image'
        raise RuntimeError("Cannot reverse this migration. 'WebpageSnapshot.image' and its values cannot be restored.")


    models = {
        'thummer.webpagesnapshot': {
            'Meta': {'ordering': "[u'-captured_at']", 'object_name': 'WebpageSnapshot'},
            'capture_width': ('django.db.models.fields.IntegerField', [], {'default': '1680'}),
            'captured_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'db_index': 'True'})
        }
    }

    complete_apps = ['thummer']
