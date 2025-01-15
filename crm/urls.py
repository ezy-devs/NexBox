from django.urls import path, include
from . import views

urlpatterns = [
    path('contacts-list', views.contacts_list, name='contacts_list'),
    path('create-contact', views.create_contact, name='create_contact'),
    path('edit-contact/<uuid:contact_id>/', views.edit_contact, name='edit_contact'),
    path('delete-contact/<uuid:contact_id>/', views.delete_contact, name='delete_contact'),
    path('creates', views.tags_list, name='tags_list'),
    path('create-tag', views.create_tag, name='create_tag'),
    path('edit-tag/<int:tag_id>/', views.edit_tag, name='edit_tag'),
    path('delete-tag/<int:tag_id>/', views.delete_tag, name='delete_tag'),
    path('onboarding', views.business_onboarding, name='business_onboarding'),

]