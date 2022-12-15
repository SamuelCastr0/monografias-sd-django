from django.urls import path, include

from django.views.generic import TemplateView

from . import views
from .api import author, advisor, monography

urlpatterns = [
    path('', views.SearchMonographyView.as_view(), name='index'),
    path('create-advisor/', TemplateView.as_view(template_name='monografias/create-advisor.html'), name='create-advisor'),
    path('create-co-advisor/', views.CoAdvisorView.as_view(), name='create-co-advisor'),
    path('create-author/', views.AuthorView.as_view(), name='create-author'),
    path('create-monography/', TemplateView.as_view(template_name='monografias/create-monography.html'), name='create-monography'),

    path('view-authors/', TemplateView.as_view(template_name='monografias/author_list.html'), name='view-authors'),
    path('edit-author/', TemplateView.as_view(template_name='monografias/author_form.html'), name='edit-author'),
    path('edit-author/<int:pk>/', TemplateView.as_view(template_name='monografias/author_form.html'), name='edit-author'),
    path('delete-author/', TemplateView.as_view(template_name='monografias/author_confirm_delete.html'), name='delete-author'),
    path('delete-author/<int:pk>/', TemplateView.as_view(template_name='monografias/author_confirm_delete.html'), name='delete-author'),

    path('view-advisors/', TemplateView.as_view(template_name='monografias/advisor_list.html'), name='view-advisors'),
    path('edit-advisor/', TemplateView.as_view(template_name='monografias/advisor_form.html'), name='edit-advisor'),
    path('edit-advisor/<int:pk>/', views.AdvisorEdit.as_view(), name='edit-advisor'),
    path('delete-advisor/', views.AdvisorDelete.as_view(), name='delete-advisor'),
    path('delete-advisor/<int:pk>/', views.AdvisorDelete.as_view(), name='delete-advisor'),

    path('view-coadvisor/', views.CoAdvisorList.as_view(), name='view-coadvisor'),
    path('edit-coadvisor/<int:pk>/', views.CoAdvisorEdit.as_view(), name='edit-coadvisor'),
    path('delete-coadvisor/<int:pk>/', views.CoAdvisoDelete.as_view(), name='delete-coadvisor'),

    path('view-monography/', views.MonographysList.as_view(), name='view-monography'),
    path('edit-monography/<int:pk>/', views.MonographyEdit.as_view(), name='edit-monography'),
    path('delete-monography/<int:pk>/', views.MonographyDelete.as_view(), name='delete-monography'),

    path('api/', include([
        path('authors/', author.AuthorAPI.as_view(), name='api-authors'),
        path('authors/<int:id>', author.AuthorAPI.as_view(), name='api-authors'),

        path('advisors/', advisor.AdvisorAPI.as_view(), name='api-advisors'),
        path('advisors/<int:id>', advisor.AdvisorAPI.as_view(), name='api-advisors'),

        path('monography/', advisor.AdvisorAPI.as_view(), name='api-monography'),
        path('monography/<int:id>', advisor.AdvisorAPI.as_view(), name='api-monography'),
    ]))
]