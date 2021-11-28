# views for manage screen
from django.http import Http404, HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator

import json
import logging

from ..consts.ItemIds import ITEM_ID_LOGIN_ID, ITEM_ID_PASSWORD
from ..messages.ErrorMessages import ERROR_MESSAGE_VALIDATION_00001

logger = logging.getLogger("melchiorapp")


class Manager():
    def login(self, request, *args, **kwargs):

        _login_id = ""
        _password = ""
        messeges = []

        # check params
        if request.POST.get("login_id", None):
            _login_id = request.POST.get("login_id", None)
        else:
            messeges.append("{" + ERROR_MESSAGE_VALIDATION_00001 %
                            ITEM_ID_LOGIN_ID + "}")

        if request.POST.get(ITEM_ID_PASSWORD, None):
            _password = request.POST.get(ITEM_ID_PASSWORD, None)
        else:
            messeges.append("{" + ERROR_MESSAGE_VALIDATION_00001 %
                            ITEM_ID_PASSWORD + "}")

        if len(messeges) > 0:
            raise Http404(json.dumps(messeges))

        logger.info(_login_id + " and " + _password)

        _response = HttpResponse("{done}")
        # _response["Access-Control-Allow-Credentials"] = "true"
        _response["Access-Control-Allow-Origin"] = "*"
        # _response["Access-Control-Allow-Origin"] = "http://localhost:8080"
        _response["Access-Control-Allow-Methods"] = "POST,GET,PUT,DELETE"

        return _response

    # @csrf_exempt
    def check_csrf(request):

        _response = HttpResponse("done")
        _response["Access-Control-Allow-Methods"] = "POST,GET,PUT,DELETE"

        return _response
