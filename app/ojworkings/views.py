from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
import requests
from ojworkings.uriWorkings import uriLogin, getProblist as getUriProblist
from ojworkings.uvaWorkings import uvaLogin, getProblist as getUvaProblist


class Problist(viewsets.ViewSet):
    """problist viewset"""

    def list(self, request):
        cliente = requests.session()
        problist = getUriProblist(cliente,5)
        return Response(problist)


def problist2(request, oj):
    """lists problems judgewise"""
    cliente = requests.session()
    problist = []
    if oj == "URI":
        problist.extend(getUriProblist(cliente,5))
        problist.extend(getUriProblist(cliente,8))
        problist.extend(getUriProblist(cliente,18))
        problist.extend(getUriProblist(cliente,12))
    elif oj == "UVA":
        problist.extend(getUvaProblist(cliente,3))
        problist.extend(getUvaProblist(cliente,6))
        problist.extend(getUvaProblist(cliente,5))
    elif oj == "CF":
        url = "https://codeforces.com/api/problemset.problems"
    else:
        pass
    return JsonResponse(problist, safe=False)
