from django.urls import path, include

from . import views
from .api import advisor, author, coAdvisor, monography

urlpatterns = [
    path('', views.SearchMonographyView.as_view(), name='index'),
    path('create-advisor/', views.AdvisorView.as_view(), name='create-advisor'),
    path('create-co-advisor/', views.CoAdvisorView.as_view(), name='create-co-advisor'),
    path('create-author/', views.AuthorView.as_view(), name='create-author'),
    path('create-monography/', views.MonographyView.as_view(), name='create-monography'),

    path('view-authors/', views.AuthorsList.as_view(), name='view-authors'),
    path('edit-author/<int:pk>/', views.AuthorEdit.as_view(), name='edit-author'),
    path('delete-author/<int:pk>/', views.AuthorDelete.as_view(), name='delete-author'),

    path('view-advisor/', views.AdvisorList.as_view(), name='view-advisor'),
    path('edit-advisor/<int:pk>/', views.AdvisorEdit.as_view(), name='edit-advisor'),
    path('delete-advisor/<int:pk>/', views.AdvisorDelete.as_view(), name='delete-advisor'),

    path('view-coadvisor/', views.CoAdvisorList.as_view(), name='view-coadvisor'),
    path('edit-coadvisor/<int:pk>/', views.CoAdvisorEdit.as_view(), name='edit-coadvisor'),
    path('delete-coadvisor/<int:pk>/', views.CoAdvisoDelete.as_view(), name='delete-coadvisor'),

    path('view-monography/', views.MonographysList.as_view(), name='view-monography'),
    path('edit-monography/<int:pk>/', views.MonographyEdit.as_view(), name='edit-monography'),
    path('delete-monography/<int:pk>/', views.MonographyDelete.as_view(), name='delete-monography'),

    path('api/', include([
        path('author/', author.AuthorAPI.as_view(), name='authors-api'),
        path('author/<int:id>/', author.AuthorAPI.as_view(), name='authors-api'),

        path('advisor/', advisor.AdvisorAPI.as_view(), name='advisors-api'),
        path('advisor/<int:id>/', advisor.AdvisorAPI.as_view(), name='advisors-api'),

        path('co-advisor/', coAdvisor.CoAdvisorAPI.as_view(), name='co-advisor-api'),
        path('co-advisor/<int:id>/', coAdvisor.CoAdvisorAPI.as_view(), name='co-advisor-api'),

        path('monography/', monography.MonographyAPI.as_view(), name='monography-api'),
        path('monography/<int:id>/', monography.MonographyAPI.as_view(), name='monography-api'),
    ]))
]