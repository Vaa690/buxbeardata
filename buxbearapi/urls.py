from django.contrib import admin
from django.urls import path
from buxbear import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webhook/noke', views.NokeWebhookView.as_view(), name='webhook_noke'),
    path('webhook/dialpad', views.NokeWebhookView.as_view(), name='webhook_dialpad'),
]