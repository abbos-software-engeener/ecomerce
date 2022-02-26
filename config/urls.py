from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
from rest_framework import permissions

# schema_view = get_schema_view(
#     openapi.Info(
#         title='School',
#         default_version='1.0.0',
#         description="School platformasi",
#         terms_of_service='http://www.google.com/policies/terms',
#         contact=openapi.Contact(email='abboscik990@gmail.com'),
#         license=openapi.License(name='School uchun license')
#
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [

]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
    # path('api/', include('api.urls', namespace='api')),

    # path('swagger', schema_view.with_ui(
    #     'swagger', cache_timeout=0), name='schema-swagger-ui'
    #      ),
    # path('redoc/', schema_view.with_ui(
    #     'redoc', cache_timeout=0), name='schema-redoc-ui'
    #      ),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)