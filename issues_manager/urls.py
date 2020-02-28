from django.urls import path, include

# from rest_framework import routers

from . import views

# router = routers.DefaultRouter()
# router.register(r'', views.IssuesViewSet)

urlpatterns = [
    path('', views.pagina_inicial, name='home'),
    path('issue_register/', views.issue_create_view, name='issue_create_view'),
    path('search/', views.search_view, name='search_view'),
    # path('api/issues/', include(router.urls)),
]
