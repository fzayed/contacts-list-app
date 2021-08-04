from django.urls import path
from .views import ContactList, ContactDetail, ContactCreate, ContactUpdate, ContactDelete

urlpatterns = [
    path('', ContactList.as_view(), name='contacts'),
    path('contact/<int:pk>/', ContactDetail.as_view(), name='contact'),
    path('contact-create/', ContactCreate.as_view(), name='contact-create'),
    path('contact-update/<int:pk>/', ContactUpdate.as_view(), name='contact-update'),
    path('contact-delete/<int:pk>/', ContactDelete.as_view(), name='contact-delete'),
]