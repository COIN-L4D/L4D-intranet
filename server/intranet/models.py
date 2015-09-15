from django.db import models

class Page(models.Model):

    name = models.CharField(max_length=64,
        blank=False,
        unique=True,
        verbose_name='An explicit name of the page')

    url_name = models.CharField(max_length=64,
        unique=True,
        blank=False,
        verbose_name='The name used in the url')

    template_file = models.CharField(max_length=256,
        blank=False,
        verbose_name='The template used for this page'
    )

    initially_visible = models.BooleanField(
        verbose_name='The page is it visible at the start of the game',
        default=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.__str__()

class PagePassword(models.Model):

    page = models.OneToOneField(Page,
        verbose_name='The target page of the link')

    password = models.CharField(max_length=128,
        unique=True,
        verbose_name='The secret code to type to reveal the page')

    def __str__(self):
        return self.page.name

    def __unicode__(self):
        return self.__str__()

class VisiblePage(models.Model):
    """ This table holds the pages that are visible,
    including the initials.
    """
    page = models.OneToOneField(Page)

    def __str__(self):
        return self.page.name

    def __unicode__(self):
        return self.__str__()

class CurrentGame(models.Model):

    RUN = 'R'
    PAUSE = 'P'
    STOP = 'S'
    STATE_CHOICES = (
        (RUN, 'Run'),
        (PAUSE, 'Pause'),
        (STOP, 'Stop'),
    )

    state = models.CharField(max_length=2,
        choices=STATE_CHOICES,
        default=STOP,
        verbose_name='The state of the current game')

    start_datetime = models.DateTimeField(
        verbose_name='The datetime when the last game has started')
