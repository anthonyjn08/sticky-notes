from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for displating a list of all notes
    path("",
         views.note_list,
         name="note_list"
         ),

    # URL pattern for displaying details of a specific note
    path("note/<int:pk>/",
         views.note_detail,
         name="note_detail"
         ),

    # URL pattern for creating a new note
    path("note/create/",
         views.note_create,
         name="note_create"
         ),

    # URL pattern for updating an existing note
    path("note/<int:pk>/edit/",
         views.note_update,
         name="note_update"
         ),

    # URL pattern for deleting an existing note
    path("note/<int:pk>/delete/",
         views.note_delete,
         name="note_delete"
         ),

    # URL pattern to pin/unpin an existing note
    path('note/<int:pk>/toggle_pin/',
         views.toggle_pin,
         name='toggle_pin'
         ),

    # URL pattern to archive/unarchive an existing note
    path('note/<int:pk>/toggle_archive/',
         views.toggle_archive,
         name='toggle_archive'
         ),
]
