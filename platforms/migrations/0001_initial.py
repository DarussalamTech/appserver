# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Platform'
    
        db.create_table(u'platforms_platform', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'platforms', ['Platform'])

        # Adding model 'AppPlatform'
        db.create_table(u'platforms_appplatform', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('app_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['apps.App'])),
            ('plat_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['platforms.Platform'])),
        ))
        db.send_create_signal(u'platforms', ['AppPlatform'])

        # Adding model 'Push'
        db.create_table(u'platforms_push', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('app_platform_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['platforms.AppPlatform'])),
            ('notification', self.gf('django.db.models.fields.TextField')()),
            ('send_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'platforms', ['Push'])

        # Adding model 'Flurry'
        db.create_table(u'platforms_flurry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('app_platform_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['platforms.AppPlatform'])),
            ('store_id', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('apikey', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'platforms', ['Flurry'])

        # Adding model 'GoogleAnalytics'
        db.create_table(u'platforms_googleanalytics', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('app_platform_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['platforms.AppPlatform'])),
            ('tracking_id', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'platforms', ['GoogleAnalytics'])

        # Adding model 'Parse'
        db.create_table(u'platforms_parse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('app_platform_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['platforms.AppPlatform'])),
            ('application_id', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('client_key', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'platforms', ['Parse'])

        # Adding model 'Facebook'
        db.create_table(u'platforms_facebook', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('app_platform_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['platforms.AppPlatform'])),
            ('app_id', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('app_secret', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'platforms', ['Facebook'])

        # Adding model 'Twitter'
        db.create_table(u'platforms_twitter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('app_platform_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['platforms.AppPlatform'])),
            ('app_id', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('app_secret', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'platforms', ['Twitter'])

        # Adding model 'GooglePlus'
        db.create_table(u'platforms_googleplus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('app_platform_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['platforms.AppPlatform'])),
            ('app_id', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('app_secret', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'platforms', ['GooglePlus'])

        # Adding model 'Plugin'
        db.create_table(u'platforms_plugin', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'platforms', ['Plugin'])


    def backwards(self, orm):
        # Deleting model 'Platform'
        db.delete_table(u'platforms_platform')

        # Deleting model 'AppPlatform'
        db.delete_table(u'platforms_appplatform')

        # Deleting model 'Push'
        db.delete_table(u'platforms_push')

        # Deleting model 'Flurry'
        db.delete_table(u'platforms_flurry')

        # Deleting model 'GoogleAnalytics'
        db.delete_table(u'platforms_googleanalytics')

        # Deleting model 'Parse'
        db.delete_table(u'platforms_parse')

        # Deleting model 'Facebook'
        db.delete_table(u'platforms_facebook')

        # Deleting model 'Twitter'
        db.delete_table(u'platforms_twitter')

        # Deleting model 'GooglePlus'
        db.delete_table(u'platforms_googleplus')

        # Deleting model 'Plugin'
        db.delete_table(u'platforms_plugin')


    models = {
        u'apps.app': {
            'Meta': {'object_name': 'App'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['apps.Category']"}),
            'clients': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['apps.Clients']", 'symmetrical': 'False'}),
            'create_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'devices': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['apps.DeviceType']", 'symmetrical': 'False'}),
            'icon': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itunes_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'platforms': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['platforms.Platform']", 'symmetrical': 'False'}),
            'playstore_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'plugins': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['platforms.Plugin']", 'symmetrical': 'False'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'apps.category': {
            'Meta': {'object_name': 'Category'},
            'cat_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'apps.clients': {
            'Meta': {'object_name': 'Clients'},
            'device_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'apps.devicetype': {
            'Meta': {'object_name': 'DeviceType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'platforms.appplatform': {
            'Meta': {'object_name': 'AppPlatform'},
            'app_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['apps.App']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plat_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['platforms.Platform']"})
        },
        u'platforms.facebook': {
            'Meta': {'object_name': 'Facebook'},
            'app_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'app_platform_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['platforms.AppPlatform']"}),
            'app_secret': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'platforms.flurry': {
            'Meta': {'object_name': 'Flurry'},
            'apikey': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'app_platform_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['platforms.AppPlatform']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'store_id': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        },
        u'platforms.googleanalytics': {
            'Meta': {'object_name': 'GoogleAnalytics'},
            'app_platform_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['platforms.AppPlatform']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tracking_id': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'platforms.googleplus': {
            'Meta': {'object_name': 'GooglePlus'},
            'app_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'app_platform_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['platforms.AppPlatform']"}),
            'app_secret': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'platforms.parse': {
            'Meta': {'object_name': 'Parse'},
            'app_platform_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['platforms.AppPlatform']"}),
            'application_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'client_key': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'platforms.platform': {
            'Meta': {'object_name': 'Platform'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'platforms.plugin': {
            'Meta': {'object_name': 'Plugin'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'platforms.push': {
            'Meta': {'object_name': 'Push'},
            'app_platform_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['platforms.AppPlatform']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notification': ('django.db.models.fields.TextField', [], {}),
            'send_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'platforms.twitter': {
            'Meta': {'object_name': 'Twitter'},
            'app_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'app_platform_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['platforms.AppPlatform']"}),
            'app_secret': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['platforms']