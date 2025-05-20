from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Quản lý cửa hàng điện thoại"
admin.site.site_title = "Quản trị hệ thống"
admin.site.index_title = "Chức năng quản trị"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)