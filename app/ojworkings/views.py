from rest_framework import viewsets
from rest_framework.response import Response
import requests
from ojworkings.uriWorkings import uriLogin, getProblist


class Problist(viewsets.ViewSet):
    """problist viewset"""

    def list(self, request):
        cliente = requests.session()
        problist = getProblist(cliente,5)
        return Response(problist)
