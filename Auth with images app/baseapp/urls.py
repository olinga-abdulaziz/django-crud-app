from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('upload/',views.UploadView.as_view(),name='upload'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)