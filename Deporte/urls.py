from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from rest_framework import routers
admin.autodiscover()
from nomencladores.views import PersonaViewSet
router = routers.DefaultRouter()
router.register(r'links/listaPersonas',PersonaViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'hockey.views.index', name='index'),
    url(r'^sumarVotosArticulo/(\d+)$', 'hockey.views.sumarVotosArticulo', name='sumarVotosArticulo' ),
    url(r'^restarVotosArticulo/(\d+)$', 'hockey.views.restarVotosArticulo', name='restarVotosArticulo' ),
    url(r'^addArticulo/$', 'hockey.views.addArticulo', name='addArticulo'),
    url(r'articulo/(\d+)$','hockey.views.articulo',name='articulo'),
    url(r'consumoPersonas/$','hockey.views.consumoPersonas', name='consumoPersonas'),
)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
