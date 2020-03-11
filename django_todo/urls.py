from django.conf.urls import url
from django.contrib import admin
from todo.views import get_todo_list, create_an_item

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_todo_list),
    url(r'^add$', create_an_item)

]
