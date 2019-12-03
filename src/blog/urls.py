from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from posts.views import index, blog, post


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="home_page"),
    path('blog/', blog, name="blog_list"),
    path('post/', post, name="single_post"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)