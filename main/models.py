from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
class WelcomeText(models.Model):
    name=models.CharField('Title', max_length=200)
    txt=RichTextField('Text',default='')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Welcome Text'
        verbose_name_plural = 'Welcome Texts'
class Aboutme(models.Model):
    name=models.CharField('Title',max_length=200)
    txt=RichTextField('Text',default='')
    date=models.DateTimeField('Date',default=timezone.now)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Part of about me'
        verbose_name_plural = 'About me'
class Projects(models.Model):
    name=models.CharField('Project name', max_length=200,unique=True)
    img=models.URLField('Image',default='')
    url=models.URLField('URL',default='')
    date=models.DateTimeField('Date',default=timezone.now)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
class Whatsapp(models.Model):
    name=models.CharField('Title',max_length=200)
    number=models.CharField('Number',max_length=200,default='+994556449164')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Whatsapp'
        verbose_name_plural = 'Whatsapp'
class Telegram(models.Model):
    name=models.CharField('Title',max_length=200)
    number=models.CharField('Number',max_length=200,default='+994556449164')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Telegram'
        verbose_name_plural = 'Telegram'
class Phone(models.Model):
    name=models.CharField('Title',max_length=200)
    number=models.CharField('Number',max_length=200,default='+994556449164')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Phone'
        verbose_name_plural = 'Phone'
class Location(models.Model):
    name=models.CharField('Location',max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Location'