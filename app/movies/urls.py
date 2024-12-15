from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MoviesViewSet


router = DefaultRouter()
router.register(r'movies', MoviesViewSet)


urlpatterns = [
    # path("api/movies/", MovieList.as_view()),
    # path("api/movies/<int:pk>/", MovieDetail.as_view())
    path('api/', include(router.urls))
]
