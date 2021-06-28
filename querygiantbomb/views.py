from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.shortcuts import redirect
from gamesquery import settings
from querygiantbomb.apps import GiantBombApi
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, AdminRenderer


def bad_request(request, exception=None):
    """
    Redirect bad request to home view
    """
    return redirect(reverse('home'))


@api_view(('GET',))
def home(request):
    """
    Search a Game: \n
        GET /v1/games/{game_query}
        GET /v1/games/{game_query}?limit={resultsPerPage}&page={pageIndex}&format=json
        GET /v1/games/{game_query}?fields=field1,field2,field3
    \nExamples: (curl, http) \n
        http://34.220.37.66:8000/v1/games/poke
        http://34.220.37.66:8000/v1/games/poke?limit=2&page=2
        http://34.220.37.66:8000/v1/games/poke?limit=2&page=2&fields=id,aliases,description
    \nNote: \n
        Default Filters: "limit=5, page=0, offset=0"
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
        GET /v1/games/{game_name}
        GET /v1/games/{game_name}?limit={resultsPerPage}&page={pageIndex}&format=json
        GET /v1/games/{game_name}?fields=field1,field2,field3
    \nExamples (curl, http): \n
        http://34.220.37.66:8000/v1/games/poke
        http://34.220.37.66:8000/v1/games/poke?limit=2&page=2
        http://34.220.37.66:8000/v1/games/poke?limit=2&page=2&fields=id,aliases,description
    \nNote: \n
        Default Filters: "limit=5, page=0, offset=0"
        Default Fields: "id, name, date_added, api_detail_url, number_of_user_reviews"
    """
    # Render in JSON, API and Admin formats
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer, AdminRenderer]

    def get(self, request, version, game_query):
        """
        GET v1/games/{game_name}/
        Returns a list of games from GiantBomb backend DB
        """
        # Get giantbomb api key from settings
        api_key = settings.GIANTBOMB_API_KEY

        # Get filters from request
        filters = request.GET.dict()

        # Get results from giantbomb search api
        giantbomb = GiantBombApi(api_key)
        response = giantbomb.search(game_query, filters)

        # Return the response
        return Response(response)
