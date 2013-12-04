# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'faq_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=75)),
            ('display_order', self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True)),
        ))
        db.send_create_signal(u'faq', ['Category'])

        # Adding model 'Question'
        db.create_table(u'faq_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.TextField')()),
            ('answer', self.gf('django.db.models.fields.TextField')()),
            ('display_order', self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='questions', null=True, on_delete=models.SET_NULL, to=orm['faq.Category'])),
        ))
        db.send_create_signal(u'faq', ['Question'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'faq_category')

        # Deleting model 'Question'
        db.delete_table(u'faq_question')


    models = {
        u'faq.category': {
            'Meta': {'ordering': "('display_order',)", 'object_name': 'Category'},
            'display_order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '75'})
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