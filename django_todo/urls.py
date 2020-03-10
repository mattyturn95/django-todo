from django.conf.urls import url
from django.contrib import admin
from todo.views import get_todo_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_todo_list),

]
