from django.urls import path
from cakes.views import myroom_own , cake_custom
app_name = 'cakes'

urlpatterns = [
    path('ownroom/<int:user_id>/',myroom_own,name='ownroom'),
    path('cakecustom/',cake_custom,name='cakemaker'),
]