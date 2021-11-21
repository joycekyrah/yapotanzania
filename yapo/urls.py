from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from core.views import index, about, events, blog, contact, blog_details, event_details, gallery, project, project_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('events/', events, name='events'),
    path('gallery/', gallery, name='gallery'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('blog-details/<int:blog_id>', blog_details, name='blog-details'),
    path('event-details/<int:event_id>', event_details, name='event-details'),
    path('project/', project, name='project'),
    path('project-details/<int:project_id>', project_details, name='project-details'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)