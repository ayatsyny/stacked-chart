from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^chart/',  include('upload_data.urls')),
    url(r'^admin/', admin.site.urls),
]
