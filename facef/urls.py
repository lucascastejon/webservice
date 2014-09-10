from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='home'),
    url(r'^cliente/formulario/(?P<id_cliente>\d+)$', 'core.views.formulario', name='formulario'),
    url(r'^cliente/cep/(?P<cep>\d+)/(?P<id_cliente>\d+)', 'core.views.cep', name='cep'),
    url(r'^cliente/formulario/salvar/', 'core.views.salvar_enviar', name='salvar_enviar'),

    url(r'^admin/', include(admin.site.urls)),
)
