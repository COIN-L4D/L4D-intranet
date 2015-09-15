from django.shortcuts import redirect
from django.views.generic import View
from django.http import HttpResponse
import json

from .models import Page, CurrentGame, VisiblePage, PagePassword
from .game import Manager
from .views import IntranetBaseView

class MenuAPI(IntranetBaseView):

    @staticmethod
    def prepare_page(page):
        """ prepare the page to be serialized """
        return {
            'name': page.name,
            'path': '/page/' + page.url_name,
        }

    @staticmethod
    def prepare_visible_page_list(page_list):
        return [
            MenuAPI.prepare_page(visible_page.page)
            for visible_page in page_list
        ]

    def get(self, request):
        if Manager().is_started():
            initial_page_list = VisiblePage.objects.filter(
                page__initially_visible=True)
            reveal_page_list = VisiblePage.objects.filter(
                page__initially_visible=False)
        else:
            initial_page_list = []
            reveal_page_list = []

        response_object = {
            'initial': MenuAPI.prepare_visible_page_list(initial_page_list),
            'reveal': MenuAPI.prepare_visible_page_list(reveal_page_list),
        }

        response_json = json.dumps(response_object)
        return HttpResponse(response_json, content_type='application/json')

class TryPasswordAPI(IntranetBaseView):
    """ This api try to unlock any page by entering a password """

    def get(self, request, *args, **kwargs):
        """ Forward GET to POST (for testing purpose) """
        request.POST = request.GET
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.POST.has_key('password'):
            response_object = self.process_password(request.POST['password'])
        else:
            response_object = self.invalid_request(
                "missing 'password' parameter")
        response_json = json.dumps(response_object)
        return HttpResponse(response_json, content_type='application/json')

    def process_password(self, password):
        try:
            page_pwd = PagePassword.objects.get(password=password)
            page = page_pwd.page
            VisiblePage.objects.get_or_create(page=page)
            return {
                'error': False,
                'granted': True,
                'page': MenuAPI.prepare_page(page),
            }
        except PagePassword.DoesNotExist:
            return {
                'error': False,
                'granted': False,
            }

    def invalid_request(self, error_info):
        return {
            'error': True,
            'error_info': 'invalid request: ' + error_info,
        }


class BaseGameAPI(View):
    def get(self, request, *args, **kwargs):
        """ Forward GET to POST (for testing purpose) """
        request.POST = request.GET
        return self.post(request, *args, **args)

class StartAPI(BaseGameAPI):
    def post(self, request):
        Manager().start()
        return HttpResponse('')

class StopAPI(BaseGameAPI):
    def post(self, request):
        Manager().stop()
        return HttpResponse('')

class PauseAPI(BaseGameAPI):
    def post(self, request):
        Manager().pause()
        return HttpResponse('')

class RestartAPI(BaseGameAPI):
    def post(self, request):
        Manager().restart()
        return HttpResponse('')
