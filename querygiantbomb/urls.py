from django.urls import path, re_path
from querygiantbomb import views

# Maps all routes to home view except /v1/games/{game_name}
urlpatterns = [
    path("", views.home, name='home'),
    re_path(r'^(?P<version>(v1))/games/(?P<game_query>[a-zA-Z0-9 ]+)',
            views.GameSearch.as_view(),
            name='game-search-list'
            ),
    re_path(r'.*', views.bad_request, name='bad-request'),
]
