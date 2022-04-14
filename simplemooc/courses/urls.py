from django.urls import path, include
from . import views


urlpatterns = [

    path('cursos/', views.courses, name='courses'),
    path('cursos/<slug:slug>/', views.details, name='details')

]




'''urlpatterns = [

    path('cursos/', views.PostListView.as_view(), name='courses'),
    path('cursos/<slug:slug>/', views.PostDetailView.as_view(), name='details'),

]
'''