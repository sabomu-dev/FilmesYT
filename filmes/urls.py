from django.urls import path
from .views import Index, Movie, Mix, About, Search

urlpatterns = [
    path("", Index , name = "index"),
    path("sobre", About , name="sobre"),
    path("lancamento/<int:pk>", Movie, name="lancamento"),
    path("misturado/<int:pk>", Mix, name="misturado"),
    path("procurar/", Search, name="procurar"), 

]