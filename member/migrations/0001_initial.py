# Generated by Django 3.1.5 on 2021-01-09 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(blank=True, max_length=100, null=True)),
                ('resume_link', models.URLField(blank=True, max_length=100, null=True)),
                ('file', models.ImageField(blank=True, default='create.jpg', upload_to='users/%Y/%m/%d/')),
                ('status', models.CharField(choices=[('Open to work', 'Open to work'), ('Working', 'Working')], default='Working', max_length=30)),
                ('bio', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Social_Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_platform', models.CharField(max_length=40)),
                ('username', models.CharField(max_length=50)),
                ('url_for_link', models.URLField(max_length=400)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_link', to='member.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(blank=True, max_length=200, null=True)),
                ('experience_skill', models.IntegerField(blank=True, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='member.profile')),
            ],
            options={
                'ordering': ('experience_skill',),
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(blank=True, max_length=80, null=True)),
                ('company', models.CharField(blank=True, max_length=200, null=True)),
                ('started', models.DateTimeField(blank=True, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='member.profile')),
            ],
            options={
                'ordering': ('started',),
            },
        ),
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_hobby', models.CharField(max_length=200)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hobbies', to='member.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(blank=True, max_length=80, null=True)),
                ('school', models.CharField(blank=True, max_length=200, null=True)),
                ('cgpa', models.CharField(blank=True, max_length=2, null=True)),
                ('completed', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='member.profile')),
            ],
            options={
                'ordering': ('completed',),
            },
        ),
        migrations.CreateModel(
            name='Certificates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_name', models.CharField(blank=True, max_length=200, null=True)),
                ('completed', models.DateTimeField(blank=True, null=True)),
                ('url_for_certificate', models.URLField(blank=True, null=True)),
                ('company', models.CharField(blank=True, max_length=200)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificates', to='member.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_award', models.CharField(max_length=200)),
                ('url_for_awards', models.URLField(blank=True, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='awards', to='member.profile')),
            ],
        ),
    ]
