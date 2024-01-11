from django.urls import path
from . import views
from django.conf import settings	
from django.conf.urls.static import static

urlpatterns = [
	path('', views.index),
	path('card/<int:id>/', views.card_id),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
