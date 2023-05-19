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