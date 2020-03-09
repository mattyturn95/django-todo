from django.conf.urls import url
from django.contrib import admin
from todo.views import say_hello

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', say_hello),    
]
