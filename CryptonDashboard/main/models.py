from django.db import models

# Create your models here.
class Node(models.Model):
    img = models.CharField('Фото', max_length=250)
    title = models.CharField('Название', max_length=250)
    raiting = models.CharField('Рейтинг', max_length=250)
    
    about = models.TextField('Описание', default='nothing')

    tech = models.BooleanField('Tech')
    Community = models.BooleanField('Community')

    status = models.CharField('Статус', max_length=250)
    dates = models.CharField('Дата', max_length=250)
    rewards = models.CharField('Награды', max_length=250)
    lock = models.CharField('Закрытие', max_length=250)
    
    hardware = models.IntegerField('Оборудование')
    Complexity = models.IntegerField('Сложность')

    cpu = models.CharField('Процессор', max_length=250)
    ram = models.CharField('Оперативная память', max_length=250)
    os = models.CharField('Операционная система', max_length=250)
    storage = models.CharField('Память', max_length=250)
    network = models.CharField('Скорость интернета', max_length=250)
    note = models.CharField('Примечание', max_length=250)

    template_name = models.CharField('Название шаблона гайда', max_length=250)
    start = models.IntegerField('Дата старта проекта', max_length=250)
    
    template_world = models.CharField('Имя инфографиков', default='nothing', max_length=250)
    urldef = models.CharField('Сылка на оф. гайд', default='nothing', max_length=250)

class World(models.Model):
    name = models.CharField('Название ноды', max_length=250)
    field1 = models.IntegerField('Korea Talecom')
    field2 = models.IntegerField('KORNET')
    field3 = models.IntegerField('(ju)haepimeoniaissi')
    field4 = models.IntegerField('Contabo')
    field5 = models.IntegerField('Kornet')
    field6 = models.IntegerField('Digital Ocean')
    field7 = models.IntegerField('Alibaba.com Singapore E-Co')
    field8 = models.IntegerField('Hetzner')

class VPS(models.Model):
    name = models.CharField('Название ноды', max_length=250)
    field1 = models.IntegerField('South Korea')
    field2 = models.IntegerField('Germany')
    field3 = models.IntegerField('United States')
    field4 = models.IntegerField('Hong Kong')
    field5 = models.IntegerField('Singapore')
    field6 = models.IntegerField('Russia')
    field7 = models.IntegerField('Netherlands')
    field8 = models.IntegerField('Finland')


class Country(models.Model):
    name = models.CharField('Название ноды', max_length=250)
    field1 = models.IntegerField('December')
    field2 = models.IntegerField('January')
    field3 = models.IntegerField('February')
    field4 = models.IntegerField('March')
    field5 = models.IntegerField('April')
    field6 = models.IntegerField('May')