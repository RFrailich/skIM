from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from skIM import settings
admin.autodiscover()

urlpatterns = [
    url(r'^messaging/', include('registration.backends.default.urls')),
    url(r'^messaging/', include('messaging.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()