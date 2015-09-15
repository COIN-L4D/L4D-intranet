from django.utils.timezone import now

from .models import CurrentGame, VisiblePage, Page

class Manager:

    def __init__(self):
        self._current_game = None

    @property
    def current_game(self):
        def get_current_game():
            tuple_ = CurrentGame.objects.get_or_create(defaults={
                'state': CurrentGame.STOP,
                'start_datetime': now(),
            })
            return tuple_[0]

        if self._current_game is None:
            self._current_game = get_current_game()
        return self._current_game

    def start(self):
        def reset_current_visible_pages():
            VisiblePage.objects.all().delete()
            for page in Page.objects.filter(initially_visible=True):
                VisiblePage(page=page).save()

        if self.current_game.state != CurrentGame.RUN:
            if self.current_game.state != CurrentGame.PAUSE:
                self.current_game.start_datetime = now()
                reset_current_visible_pages()
            self.current_game.state = CurrentGame.RUN
            self.current_game.save()

    def stop(self):
        self.current_game.state = CurrentGame.STOP
        self.current_game.save()

    def pause(self):
        if self.current_game.state != CurrentGame.STOP:
            self.current_game.state = CurrentGame.PAUSE
            self.current_game.save()

    def restart(self):
        self.stop()
        self.start()

    def is_started(self):
        return self.current_game.state != CurrentGame.STOP
