from catalyst.views import PoemViewSet
from django.urls import path
from catalyst import views

urlpatterns = [
    path('api/poem/generate', views.PoemViewSet.as_view(), name='poem-generate'),
    # path('v1/chat/completions', generate_view),
]
# https://api.openai.com/v1/chat/completions