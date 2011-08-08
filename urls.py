from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
#import for custom registration with profile
from forms import CustomRegistrationForm
from registration.views import register

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cs.views.home', name='home'),
    # url(r'^cs/', include('cs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
		(r'^$','cs.views.home'),	
		(r'^videos/',include('videos.urls')),
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
		(r'^faq/$','cs.views.faq'),
	#custom registration form that creates profile
	url(r'^login/$',register,{'form_class' : CustomRegistrationForm},name='registration_register'),
		(r'^accounts/', include('registration.urls')),
		(r'^users/',include('users.urls')),
	# Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	
		(r'^streams/(?P<stream_url_friendly>[\w\-]+)/$','cs.views.stream_detail'),
)
