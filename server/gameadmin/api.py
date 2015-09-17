from django.shortcuts import redirect
from django.views.generic import View
from django.http import HttpResponse
import json

from intranet.game import Manager

# Create your views here.
class BaseAdminAPI(View):
    """ Ensure that the user is authenticated,
    otherwise return an error """
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
             return super(BaseAdminAPI, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponse(json.dumps({
                'error': True,
                'error_info': 'you are not authenticated'
            }), content_type='application/json')

class StatusAPI(BaseAdminAPI):
    """ This api returns the status of the current game """

    def get(self, request, *args, **kwargs):
        current_game = Manager().current_game
        response_object = {
            'error': False,
            'state': current_game.get_state_display(),
            'start_datetime': current_game.start_datetime.strftime('%x %X'),
        }
        response_json = json.dumps(response_object)
        return HttpResponse(response_json, content_type='application/json')

class BaseAdminPostAPI(BaseAdminAPI):
    def get(self, request, *args, **kwargs):
        """ Forward GET to POST (for testing purpose) """
        request.POST = request.GET
        return self.post(request, *args, **kwargs)

class StartAPI(BaseAdminPostAPI):
    def post(self, request):
        Manager().start()
        return HttpResponse(json.dumps({
            'error': False,
        }), content_type='application/json')

class StopAPI(BaseAdminPostAPI):
    def post(self, request):
        Manager().stop()
        return HttpResponse(json.dumps({
            'error': False,
        }), content_type='application/json')

class PauseAPI(BaseAdminPostAPI):
    def post(self, request):
        Manager().pause()
        return HttpResponse(json.dumps({
            'error': False,
        }), content_type='application/json')

class RestartAPI(BaseAdminPostAPI):
    def post(self, request):
        Manager().restart()
        return HttpResponse(json.dumps({
            'error': False,
        }), content_type='application/json')
