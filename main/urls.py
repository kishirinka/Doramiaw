from django.urls import path
from main.views import show_main, create_object_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user
from main.views import logout_user
from main.views import edit_object, delete_object
from main.views import show_welcome, add_object_entry_ajax, create_item_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-object-entry', create_object_entry, name='create_object_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-item/<uuid:id>', edit_object, name='edit_object'),
    path('delete/<uuid:id>', delete_object, name='delete_object'),
    path('welcome/', show_welcome, name='welcome'),
    path('create-item-entry-ajax', add_object_entry_ajax, name='add_object_entry_ajax'),
    path('create-flutter/', create_item_flutter, name='create_item_flutter'),
]