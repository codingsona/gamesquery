from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseNotFound
from gamesquery import settings
from querygiantbomb.apps import GiantBombApi
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, AdminRenderer


def bad_request(request, exception=None):
    """
    Handle bad requests
    """
    return HttpResponseNotFound("404: Bad Request, resource not found")
    #return redirect(reverse('home'))


@api_view(('GET',))
def home(request):
    """
    Search a Game: \n
        GET /v1/games?query={game_query}
        GET /v1/games?query={game_query}&limit={resultsPerPage}&page={pageIndex}&format=json
        GET /v1/games?query={game_query}&fields=field1,field2,field3
        GET /v1/games?query={game_query}&format-=json&fields=field1,field2,field3
    \nExamples: (curl, http) \n
        http://34.220.37.66:8000/v1/games?query=poke
        http://34.220.37.66:8000/v1/games?query=poke&limit=2&page=2
        http://34.220.37.66:8000/v1/games?query=poke&limit=2&page=2&fields=id,name,api_detail_url
        http://34.220.37.66:8000/v1/games?query=poke&format=json&limit=2&page=2&fields=id,name,api_detail_url
    \nNote: \n
        Default Filters: "limit=5, page=1, offset=0"
        Default Fields: "id, name, date_added, api_detail_url, number_of_user_reviews"
    """
    return Response({
        "Search a Game": "GET /v1/games/{game_query}",
        "Example1": "http://34.220.37.66:8000/v1/games/poke",
        'Apply Filters': ' GET /v1/games/{game_query}?limit={resultsPerPage}&page={pageIndex}&format=json',
        'Example2': 'http://34.220.37.66:8000/v1/games/poke?limit=10&page=1',
        'Apply Fields': ' GET /v1/games/{game_query}?fields=field1,field2',
        'Example3': 'http://34.220.37.66:8000/v1/games/poke?fields=id,name&limit=10&page=1',
        "Default Fields are": "id,name,date_added,api_detail_url,number_of_user_reviews"
    })


class GameSearch(APIView):
    """
    Search a Game: \n
        GET /v1/games?query={game_query}
        GET /v1/games?query={game_query}&limit={resultsPerPage}&page={pageIndex}&format=json
        GET /v1/games?query={game_query}&fields=field1,field2,field3
        GET /v1/games?query={game_query}&format-=json&fields=field1,field2,field3
    \nExamples: (curl, http) \n
        http://34.220.37.66:8000/v1/games?query=poke
        http://34.220.37.66:8000/v1/games?query=poke&limit=2&page=2
        http://34.220.37.66:8000/v1/games?query=poke&limit=2&page=2&fields=id,aliases,description
        http://34.220.37.66:8000/v1/games?query=poke&format=json&limit=2&page=2&fields=id,aliases,description
    \nNote: \n
        Default Filters: "limit=5, page=1, offset=0"
        Default Fields: "id, name, date_added, api_detail_url, number_of_user_reviews"
    """
    # Render in JSON, API and Admin formats
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer, AdminRenderer]

    def get(self, request, version):
        """
        GET v1/games/{game_name}/
        Returns a list of games from GiantBomb backend DB
        """
        # Get giantbomb api key from settings
        api_key = settings.GIANTBOMB_API_KEY

        # Get filters from request
        filters = request.GET.dict()

        # Find out if game query string is present in filters
        game_query_present = False
        if len(filters.get("query",[])) > 0:
            game_query_present = True

        # Get results from giantbomb search api
        if game_query_present:
            giantbomb = GiantBombApi(api_key)
            response = giantbomb.search(filters)
        else:
            return HttpResponseNotFound("404: No query string sent for search")

        # Return the response
        return Response(response)
