from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from towns import views

urlpatterns = [
    path('towns/', views.TownList.as_view()),
    path('agg/', views.TownAggregation.as_view()),
    path('query/', views.TownDsl.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
