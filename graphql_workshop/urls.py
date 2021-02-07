from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from .views import graphql_websocket_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', GraphQLView.as_view(graphiql=True)),
    path('graphqlws/', graphql_websocket_view)
]
