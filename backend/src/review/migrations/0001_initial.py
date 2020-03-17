# Generated by Django 3.0.4 on 2020-03-17 12:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mjlog_id', models.CharField(max_length=63, verbose_name='牌譜ID')),
                ('target_actor', models.PositiveSmallIntegerField(verbose_name='視点')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, '予約中'), (2, 'レビュー中'), (3, 'レビュー完了'), (4, 'エラー終了')], default=1, verbose_name='レビュー状況')),
                ('result_json', models.TextField(blank=True, verbose_name='結果JSON')),
                ('reserved_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='予約時刻')),
                ('started_at', models.DateTimeField(blank=True, null=True, verbose_name='レビュー開始時刻')),
                ('ended_at', models.DateTimeField(blank=True, null=True, verbose_name='レビュー完了時刻')),
            ],
            options={
                'verbose_name': 'レビュー',
                'verbose_name_plural': 'レビュー',
                'db_table': 'review',
            },
        ),
    ]
