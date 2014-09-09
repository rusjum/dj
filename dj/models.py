import os
from django.db import models


# Model for menu item in header
import time
import hashlib

def generate_filename(instance, old_filename):

    m = hashlib.md5()
    splitted = os.path.splitext(old_filename)
    filename = str(splitted[0]).encode('utf-8')
    m.update(filename)
    extension = splitted[1]
    filename = str(m.hexdigest()) + extension
    return filename


class MenuItem(models.Model):
    label = models.CharField("Значение", max_length=100)
    url = models.CharField("Заголовок", max_length=255, null=True)
    visible = models.BooleanField("Видимость", default=True)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"


# Model for tagline in the middle
class Tagline(models.Model):
    text = models.CharField("Содержание", max_length=255)
    visible = models.BooleanField("Видимость", default=True)

    class Meta:
        verbose_name = "Слоган"
        verbose_name_plural = "Слоганы"

    def __str__(self):
        return self.text

# Model for Team members
class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    image = models.ImageField("Изображение", upload_to=generate_filename)
    visible = models.BooleanField("Видимость", default=True)

    class Meta:
        verbose_name = "Член команды"
        verbose_name_plural = "Члены команды"

    def __str__(self):
        return self.name

class SocialNetworkType(models.Model):
    # FACEBOOK = 'F'
    # GOOGLE_PLUS = 'G'
    # LINKED_IN = 'L'
    # TWITTER = 'T'
    # NETWORK_CHOICES = (
    #     (FACEBOOK, 'Facebook'),
    #     (GOOGLE_PLUS, 'Google+'),
    #     (TWITTER, 'Twitter'),
    #     (LINKED_IN, 'LinkedIn'),
    # )
    # network_type = models.CharField(max_length=1,
    #                                   choices=NETWORK_CHOICES,
    #                                   unique=True)
    network_name = models.CharField("Название социальной сети", max_length=255)
    image = models.ImageField("Изображение", upload_to=generate_filename)

    def __str__(self):
        return self.network_name

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"

#     social network link for a member
class SocialNetworkLink(models.Model):
    network_type = models.ForeignKey(SocialNetworkType, verbose_name="Социальная сеть")
    member = models.ForeignKey(TeamMember, verbose_name="Член команды")
    url = models.CharField("Ссылка", max_length=255)
    visible = models.BooleanField("Видимость", default=True)

    def __str__(self):
        return self.member.name + '_' + self.network_type

    class Meta:
        verbose_name = "Ссылка на социальную сеть"
        verbose_name_plural = "Ссылки на социальную сеть"


class OurService(models.Model):
    title = models.CharField("Наименование", max_length=255)
    description = models.TextField("Описание", name='description')
    image = models.ImageField("Изображение", upload_to=generate_filename)
    visible = models.BooleanField("Видимость", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class OurClient(models.Model):
    title = models.CharField("Наименование", max_length=255)
    description = models.TextField("Описание", name='description')
    image = models.ImageField("Изображение", upload_to=generate_filename)
    url = models.CharField("Ссылка", max_length=255)
    visible = models.BooleanField("Видимость", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

