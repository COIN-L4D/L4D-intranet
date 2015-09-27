from django.http import HttpResponse

from intranet.api import BaseInGameAPI
from gameadmin.views import LoginRequiredMixin
from .models import MapSettings, MapEvent
import json
import datetime

class GetMapEventsAPI(BaseInGameAPI):
    """ Get the list of recent map events """

    def prepare_event(self, event):
        return {
            'position': {
                'lat': event.lat,
                'lng': event.lng,
            },
            'datetime': event.datetime.isoformat(),
            'text': event.text,
        }

    def get(self, request):
        self.map_settings = MapSettings.get_settings()
        filter_datetime = datetime.datetime.now() - \
            datetime.timedelta(seconds=self.map_settings.event_life_time)
        queryset = MapEvent.objects.filter(datetime__gt=filter_datetime)
        response_obj = [ self.prepare_event(e) for e in queryset ]
        response_json = json.dumps(response_obj)
        return HttpResponse(response_json, content_type='application/json')

class PushMapEventAPI(LoginRequiredMixin, BaseInGameAPI):
    """ push an event on the server, must be authenticated """

    def get(self, request, *args, **kwargs):
        """ Forward GET to POST (for testing purpose) """
        request.POST = request.GET
        return self.post(request, *args, **kwargs)

    def post(self, request):
        response_obj = self.parse_post(request.POST)
        response_json = json.dumps(response_obj)
        return HttpResponse(response_json, content_type='application/json')

    def invalid_request(self, error_info):
        return {
            'error': True,
            'error_info': 'invalid request: ' + error_info,
        }

    def parse_post(self, POST):
        if POST.has_key('lat'):
            try:
                lat = float(POST['lat'])
            except ValueError:
                return invalid_request("variable 'lat' is not a float")
        else:
            return invalid_request("missing variable 'lat'")

        if POST.has_key('lng'):
            try:
                lng = float(POST['lng'])
            except ValueError:
                return invalid_request("variable 'lng' is not a float")
        else:
            return invalid_request("missing variable 'lng'")

        if POST.has_key('text'):
            text = POST['text']
        else:
            return invalid_request("missing variable 'text'")

        return self.process_event(lat=lat, lng=lng, text=text)

    def process_event(self, **kwargs):
        event = MapEvent(
            lat=kwargs['lat'],
            lng=kwargs['lng'],
            text=kwargs['text'],
        )
        event.save()
        return { 'error': False, }
