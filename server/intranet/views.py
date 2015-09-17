from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import json

from .models import Page, CurrentGame, VisiblePage
from .game import Manager


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

class ClosedView(TemplateView):

    template_name = 'intranet/closed.html'

    def dispatch(self, *args, **kwargs):
        if Manager().is_started():
            return redirect('home')
        return super(ClosedView, self).dispatch(*args, **kwargs)

class IntranetBaseView(View):
    """ View accesible only if a game is running """

    def dispatch(self, *args, **kwargs):
        if not Manager().is_started():
            return redirect('closed')
        return super(IntranetBaseView, self).dispatch(*args, **kwargs)

class HomeView(IntranetBaseView, TemplateView):
    template_name = 'intranet/home.html'

class DeniedView(IntranetBaseView, TemplateView):
    template_name = 'intranet/denied.html'

class PageView(IntranetBaseView):
    """ Base view for intranet page (those used in iframe) """

    def fetch_url_name(self, **kwargs):
        self.url_name = kwargs['url_name']
        return self.url_name

    def fetch_page(self):
        self.page = get_object_or_404(Page, url_name=self.url_name)
        return self.page

    def page_is_visible(self):
        try:
            VisiblePage.objects.get(page=self.page)
            return True
        except VisiblePage.DoesNotExist:
            return False

    def get(self, request, *args, **kwargs):
        self.fetch_url_name(**kwargs)
        self.fetch_page()
        if self.page_is_visible():
            return render(request, self.page.template_file)
        else:
            return redirect('denied')

class AdminView(LoginRequiredMixin, TemplateView):
    template_name = 'intranet/admin.html'
