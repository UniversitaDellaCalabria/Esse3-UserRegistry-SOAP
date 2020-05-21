from django.urls import include, path, re_path
from soapfish.django_ import django_dispatcher
from . soaps import UserRegistrySoapService
#  from . user_registry_service import UserRegistrySoapPort_SERVICE
#  from . UserRegistryService import UserRegistrySoapPort_SERVICE


dispatcher = django_dispatcher(UserRegistrySoapService)
app_name = "esse3_unireg"

urlpatterns = path(r'user_registry', dispatcher, name='user_registry'),
