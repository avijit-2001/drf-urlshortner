from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .models import Link
from .serializer import LinkSerializer
import string, random
from django.http import HttpResponseRedirect

class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)

class URLShortner(APIView):
    """
    URLShortner Class includes functionality
    of creating short url and redirecting to original 
    url when entered.

    * Requires token authentication.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, short_url):
        short_url = "arg2e.dom/" + short_url
        url = Link.objects.get(short_url=short_url).url
        return HttpResponseRedirect(redirect_to=url)


    def post(self, request, format=None):
        url = request.data["url"]
        short_url = ''.join(random.choice(string.ascii_letters)
                           for x in range(10))
        short_url = 'app/arg2e.dom/' + short_url #adding discriminator

        link = Link(url=url, short_url=short_url)
        link.save()
        return Response(LinkSerializer(link).data)