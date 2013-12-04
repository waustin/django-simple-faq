# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Category', fields ['slug']
        db.create_unique(u'faq_category', ['slug'])


    def backwards(self, orm):
        # Removing unique constraint on 'Category', fields ['slug']
        db.delete_unique(u'faq_category', ['slug'])


    models = {
        u'faq.category': {
            'Meta': {'ordering': "('display_order',)", 'object_name': 'Category'},
            'display_order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '75'})
        },
        u'faq.question': {
            'Meta': {'ordering': "('display_order',)", 'object_name': 'Question'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'questions'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['faq.Category']"}),
            'display_order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['faq']