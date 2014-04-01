# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'apps_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cat_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'apps', ['Category'])

        # Adding model 'Clients'
        db.create_table(u'apps_clients', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('device_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'apps', ['Clients'])

        # Adding model 'DeviceType'
        db.create_table(u'apps_devicetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'apps', ['DeviceType'])

        # Adding model 'App'
        db.create_table(u'apps_app', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('icon', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['apps.Category'])),
            ('playstore_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('itunes_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('create_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'apps', ['App'])

        # Adding M2M table for field platforms on 'App'
        m2m_table_name = db.shorten_name(u'apps_app_platforms')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('app', models.ForeignKey(orm[u'apps.app'], null=False)),
            ('platform', models.ForeignKey(orm[u'platforms.platform'], null=False))
        ))
        db.create_unique(m2m_table_name, ['app_id', 'platform_id'])

        # Adding M2M table for field clients on 'App'
        m2m_table_name = db.shorten_name(u'apps_app_clients')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('app', models.ForeignKey(orm[u'apps.app'], null=False)),
            ('clients', models.ForeignKey(orm[u'apps.clients'], null=False))
        ))
        db.create_unique(m2m_table_name, ['app_id', 'clients_id'])

        # Adding M2M table for field devices on 'App'
        m2m_table_name = db.shorten_name(u'apps_app_devices')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('app', models.ForeignKey(orm[u'apps.app'], null=False)),
            ('devicetype', models.ForeignKey(orm[u'apps.devicetype'], null=False))
        ))
        db.create_unique(m2m_table_name, ['app_id', 'devicetype_id'])

        # Adding M2M table for field plugins on 'App'
        m2m_table_name = db.shorten_name(u'apps_app_plugins')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('app', models.ForeignKey(orm[u'apps.app'], null=False)),
            ('plugin', models.ForeignKey(orm[u'platforms.plugin'], null=False))
        ))
        db.create_unique(m2m_table_name, ['app_id', 'plugin_id'])

        # Adding model 'AppClients'
        db.create_table(u'apps_appclients', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('app_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['apps.App'])),
            ('client_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['apps.Clients'])),
        ))
        db.send_create_signal(u'apps', ['AppClients'])

        # Adding model 'Device'
        db.create_table(u'apps_device', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('deviceIdentifier', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'apps', ['Device'])

        # Adding M2M table for field client on 'Device'
        m2m_table_name = db.shorten_name(u'apps_device_client')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('device', models.ForeignKey(orm[u'apps.device'], null=False)),
            ('clients', models.ForeignKey(orm[u'apps.clients'], null=False))
        ))
        db.create_unique(m2m_table_name, ['device_id', 'clients_id'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'apps_category')

        # Deleting model 'Clients'
        db.delete_table(u'apps_clients')

        # Deleting model 'DeviceType'
        db.delete_table(u'apps_devicetype')

        # Deleting model 'App'
        db.delete_table(u'apps_app')

        # Removing M2M table for field platforms on 'App'
        db.delete_table(db.shorten_name(u'apps_app_platforms'))

        # Removing M2M table for field clients on 'App'
        db.delete_table(db.shorten_name(u'apps_app_clients'))

        # Removing M2M table for field devices on 'App'
        db.delete_table(db.shorten_name(u'apps_app_devices'))

        # Removing M2M table for field plugins on 'App'
        db.delete_table(db.shorten_name(u'apps_app_plugins'))

        # Deleting model 'AppClients'
        db.delete_table(u'apps_appclients')

        # Deleting model 'Device'
        db.delete_table(u'apps_device')

        # Removing M2M table for field client on 'Device'
        db.delete_table(db.shorten_name(u'apps_device_client'))


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
        u'apps.appclients': {
            'Meta': {'object_name': 'AppClients'},
            'app_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['apps.App']"}),
            'client_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['apps.Clients']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
        u'apps.device': {
            'Meta': {'object_name': 'Device'},
            'client': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['apps.Clients']", 'symmetrical': 'False'}),
            'deviceIdentifier': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
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
        u'platforms.platform': {
            'Meta': {'object_name': 'Platform'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'platforms.plugin': {
            'Meta': {'object_name': 'Plugin'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['apps']