from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from persons.views import PersonsView, PersonDetails, Compare

app_name = 'persons'

urlpatterns = [
    path('persons/', PersonsView.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('persons/compare/<str:id1>/<str:id2>/', Compare.as_view()),
    path('persons/<str:id>/', PersonDetails.as_view())
]