# Generated by Django 3.1.4 on 2020-12-02 19:00

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import emanagement.utils
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[(None, 'Select Language'), ('Action and adventure', 'Action and adventure'), ('Art', 'Art'), ('Alternate history', 'Alternate history'), ('Autobiography', 'Autobiography'), ('Anthology', 'Anthology'), ('Biography', 'Biography'), ('Chick lit', 'Chick lit'), ('Book review', 'Book review'), ("Children's", "Children's"), ('Cookbook', 'Cookbook'), ('Comic book', 'Comic book'), ('Diary', 'Diary'), ('Coming-of-age', 'Coming-of-age'), ('Dictionary', 'Dictionary'), ('Crime', 'Crime'), ('Encyclopedia', 'Encyclopedia'), ('Drama', 'Drama'), ('Guide', 'Guide'), ('Fairytale', 'Fairytale'), ('Health', 'Health'), ('Fantasy', 'Fantasy'), ('History', 'History'), ('Graphic novel', 'Graphic novel'), ('Journal', 'Journal'), ('Historical fiction', 'Historical fiction'), ('Math', 'Math'), ('Horror', 'Horror'), ('Memoir', 'Memoir'), ('Mystery Prayer', 'Mystery Prayer'), ('Paranormal romance', 'Paranormal romance'), ('Religion, spirituality and new age', 'Religion, spirituality and new age'), ('Picture book', 'Picture book'), ('Textbook', 'Textbook'), ('Poetry', 'Poetry'), ('Review', 'Review'), ('Political thriller', 'Political thriller'), ('Science', 'Science'), ('Romance', 'Romance'), ('Self help', 'Self help'), ('Satire', 'Satire'), ('Travel', 'Travel'), ('Science fiction', 'Science fiction'), ('True crime', 'True crime'), ('Short story', 'Short story'), ('Suspense', 'Suspense'), ('Thriller', 'Thriller'), ('Young adult', 'Young adult')], editable=False, max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='BookPublish',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('company_name', models.CharField(error_messages={'unique': 'This name is already exists.'}, max_length=100, unique=True)),
                ('website', models.TextField(unique=True)),
                ('genre', models.ManyToManyField(help_text='Hold down “Control”, or “Command” on a Mac, to select more than one.', to='emanagement.Genre', verbose_name='Genre')),
            ],
            options={
                'ordering': ['company_name'],
            },
        ),
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('middle_name', models.CharField(max_length=100, verbose_name='Middle Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('date_of_birth', models.DateField(null=True)),
                ('died', models.DateField(blank=True, null=True, verbose_name='Died')),
                ('aboutAuthor', models.TextField(max_length=250)),
                ('genre', models.ManyToManyField(help_text='Hold down “Control”, or “Command” on a Mac, to select more than one.', to='emanagement.Genre', verbose_name='Genre')),
            ],
            options={
                'ordering': ['date_of_birth'],
                'unique_together': {('first_name', 'last_name')},
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Book ID')),
                ('name', models.CharField(max_length=120, unique=True, verbose_name='Name')),
                ('publish_date', models.DateField(verbose_name='Publish Date')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Date')),
                ('language', models.CharField(choices=[(None, 'Select Language'), ('af', 'Afrikaans'), ('ar', 'Arabic'), ('ar-dz', 'Algerian Arabic'), ('ast', 'Asturian'), ('az', 'Azerbaijani'), ('bg', 'Bulgarian'), ('be', 'Belarusian'), ('bn', 'Bengali'), ('br', 'Breton'), ('bs', 'Bosnian'), ('ca', 'Catalan'), ('cs', 'Czech'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('dsb', 'Lower Sorbian'), ('el', 'Greek'), ('en', 'English'), ('en-au', 'Australian English'), ('en-gb', 'British English'), ('eo', 'Esperanto'), ('es', 'Spanish'), ('es-ar', 'Argentinian Spanish'), ('es-co', 'Colombian Spanish'), ('es-mx', 'Mexican Spanish'), ('es-ni', 'Nicaraguan Spanish'), ('es-ve', 'Venezuelan Spanish'), ('et', 'Estonian'), ('eu', 'Basque'), ('fa', 'Persian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'), ('ga', 'Irish'), ('gd', 'Scottish Gaelic'), ('gl', 'Galician'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hr', 'Croatian'), ('hsb', 'Upper Sorbian'), ('hu', 'Hungarian'), ('hy', 'Armenian'), ('ia', 'Interlingua'), ('id', 'Indonesian'), ('ig', 'Igbo'), ('io', 'Ido'), ('is', 'Icelandic'), ('it', 'Italian'), ('ja', 'Japanese'), ('ka', 'Georgian'), ('kab', 'Kabyle'), ('kk', 'Kazakh'), ('km', 'Khmer'), ('kn', 'Kannada'), ('ko', 'Korean'), ('ky', 'Kyrgyz'), ('lb', 'Luxembourgish'), ('lt', 'Lithuanian'), ('lv', 'Latvian'), ('mk', 'Macedonian'), ('ml', 'Malayalam'), ('mn', 'Mongolian'), ('mr', 'Marathi'), ('my', 'Burmese'), ('nb', 'Norwegian Bokmål'), ('ne', 'Nepali'), ('nl', 'Dutch'), ('nn', 'Norwegian Nynorsk'), ('os', 'Ossetic'), ('pa', 'Punjabi'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pt-br', 'Brazilian Portuguese'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sq', 'Albanian'), ('sr', 'Serbian'), ('sr-latn', 'Serbian Latin'), ('sv', 'Swedish'), ('sw', 'Swahili'), ('ta', 'Tamil'), ('te', 'Telugu'), ('tg', 'Tajik'), ('th', 'Thai'), ('tk', 'Turkmen'), ('tr', 'Turkish'), ('tt', 'Tatar'), ('udm', 'Udmurt'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('uz', 'Uzbek'), ('vi', 'Vietnamese'), ('zh-hans', 'Simplified Chinese'), ('zh-hant', 'Traditional Chinese')], max_length=12, verbose_name='Language')),
                ('edition', models.IntegerField(choices=[(None, 'Select Edition'), (1, '1st'), (2, '2nd'), (3, '3rd'), (4, '4th'), (5, '5th'), (6, '6th'), (7, '7th'), (8, '8th'), (9, '9th'), (10, '10th')], verbose_name='Edition')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Book Cost(per unit)')),
                ('page', models.PositiveIntegerField(verbose_name='Total Page')),
                ('description', models.TextField(verbose_name='Book Description')),
                ('stock', models.PositiveIntegerField(verbose_name='Stock')),
                ('today_stock', models.PositiveIntegerField(blank=True, null=True, verbose_name='Current stock')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Rating')),
                ('profile', models.FileField(blank=True, default='default.jpg', upload_to=emanagement.utils.pic_upload, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=[], message='Select valid Cover Image.')], verbose_name='Book cover')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emanagement.bookauthor', verbose_name='Author Name')),
                ('genre', models.ManyToManyField(help_text='Hold down “Control”, or “Command” on a Mac, to select more than one.', to='emanagement.Genre', verbose_name='Genre')),
                ('publish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emanagement.bookpublish', verbose_name='Publisher Name')),
            ],
            options={
                'ordering': ['name'],
                'permissions': [('is_defaulter', 'User in defaulter list')],
                'unique_together': {('name', 'author')},
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField(default=datetime.datetime(2020, 12, 9, 19, 0, 43, 279394, tzinfo=utc), help_text='By defualt date is now + 7')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emanagement.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'book')},
            },
        ),
    ]