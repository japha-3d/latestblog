from django.urls import path
from home import views
from .views import Detail
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.AllPost,name='home',),
    path('all/',views.PostAll,name='all',),
    path('trending/',views.Trending,name='trending',),
    path('search/',views.Search,name='search',),
    path('<int:pk>',Detail.as_view(),name='home',),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                        document_root=settings.MEDIA_ROOT)