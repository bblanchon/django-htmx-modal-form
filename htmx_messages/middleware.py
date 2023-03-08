import json
from django.utils.deprecation import MiddlewareMixin
from django.contrib.messages import get_messages


class HtmxMessagesMiddleware(MiddlewareMixin):

    def process_response(self, request, response):

        if 'HX-Request' in request.headers:

            hx_trigger = response.headers.get('HX-Trigger')

            if hx_trigger is None:
                hx_trigger = {}
            elif hx_trigger.startswith('{'):
                hx_trigger = json.loads(hx_trigger)
            else:
                hx_trigger = {hx_trigger: True}

            hx_trigger['messages'] = [
                {
                    "message": message.message,
                    "tags": message.tags,
                }
                for message in get_messages(request)
            ]

            response.headers['HX-Trigger'] = json.dumps(hx_trigger)

        return response