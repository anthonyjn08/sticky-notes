from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


# Create your views here.
def note_list(request):
    """
    Display for all notes.
    
    - param request: HTTP request object.
    - return: Rendered template with all notes.
    """
    notes = Note.objects.all().order_by("pinned", "-priority", "created_at")

    # Context dictionary to pass data.
    context = {
        "notes": notes,
        "page_title": "List of Notes",
    }

    return render(request, "notes/notes_list.html", context)


def note_detail(request, pk):
    """
    View to display a specific notes detail.

    - param request: HTTP request object.
    - param pk: The primary key of the note.
    - return: Rendered template with details of the specific note.
    """
    note = get_object_or_404(Note, pk=pk)
    return render(request, "notes/note_detail.html", {"note": note})


def note_create(request):
    """
    View to create a new note.
    
    - param request: HTTP request object.
    - return: Rendered new note template with form to fill in.
    """
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect("note_list")
    else:
        form = NoteForm()
    return render(request, "notes/note_form.html", {"form": form})


def note_update(request, pk):
    """
    View to update an existing note.
    
    - param request: HTTP request object.
    - param pk: Primary key of the note to be updated.
    - return: Rendered template of the specified note to update.
    """
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect("note_list")
    else:
        form = NoteForm()
    return render(request, "notes/note_form.html", {"form": form})


def note_delete(request, pk):
    """
    View to delete an existing note.

    - param request: HTTP request object.
    - param pk: Primary key of the note to be deleted.
    - return: Redirect to the note list after deletion.
    """
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect("note_list")
