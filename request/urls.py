from django.urls import path
# from .import views
# from django.conf import settings
# from django.conf.urls.static import static
from .views import IndexPageView

app_name = 'request'

urlpatterns = [
    path('', IndexPageView.as_view(), name = 'index'),
]



# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL,  document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
