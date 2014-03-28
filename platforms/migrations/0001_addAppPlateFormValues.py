# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        db.create_table('platforms_values', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('app_id', self.gf('django.db.models.fields.CharField')(max_length=250,null=True, blank=True)),
            ('app_secret', self.gf('django.db.models.fields.CharField')(max_length=250,null=True, blank=True)),
            ('app_platform', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='appPlatform', null=True,to=orm['apps.AppPlatform'])),
        ))

    def backwards(self, orm):
        "Write your backwards methods here."
        db.delete_table('platforms_values')

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
    symmetrical = True
