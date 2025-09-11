from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm
from django.contrib.auth.decorators import login_required


@login_required
def note_list(request):
    """
    Display for all notes.
    
    - param request: HTTP request object.
    - return: Rendered template with all notes.
    """
    # Toggle to show or hide archived notes.
    show_archived = request.GET.get("archived") == "1"

    notes = Note.objects.filter(
        user=request.user,
        archived=show_archived
        ).order_by("-pinned", "-priority", "-created_at")

    # Context dictionary to pass data.
    context = {
        "notes": notes,
        "show_archived": show_archived,
        "page_title": "List of Notes",
    }

    # Set shadow and title classes for template
    for note in notes:
        if note.priority == 3:
            note.shadow_class = "shadow-high"
            note.title_class = "high"
        elif note.priority == 2:
            note.shadow_class = "shadow-medium"
            note.title_class = "medium"
        else:
            note.shadow_class = "shadow-low"
            note.title_class = "low"

    return render(request, "notes/note_list.html", context)


@login_required
def note_detail(request, pk):
    """
    View to display a specific notes detail.

    - param request: HTTP request object.
    - param pk: The primary key of the note.
    - return: Rendered template with details of the specific note.
    """
    note = get_object_or_404(Note, pk=pk, user=request.user)

    return render(request, "notes/note_detail.html", {"note": note})


@login_required
def note_create(request):
    """
    View to create a new note.

    - param request: HTTP request object.
    - return: Rendered new note template with form to fill in.
    """
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect("note_list")
    else:
        form = NoteForm()

    return render(request, "notes/note_form.html", {"form": form})


@login_required
def note_update(request, pk):
    """
    View to update an existing note.

    - param request: HTTP request object.
    - param pk: Primary key of the note to be updated.
    - return: Rendered template of the specified note to update.
    """
    note = get_object_or_404(Note, pk=pk, user=request.user)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect("note_list")
    else:
        form = NoteForm(instance=note)

    return render(request, "notes/note_form.html", {"form": form})


@login_required
def note_delete(request, pk):
    """
    View to delete an existing note.

    - param request: HTTP request object.
    - param pk: Primary key of the note to be deleted.
    - return: Redirect to the note list after deletion.
    """
    note = get_object_or_404(Note, pk=pk, user=request.user)

    if request.method == "POST":
        note.delete()
        return redirect("note_list")
    
    return render(request, "notes/notes_confirm_delete.html", {"notes": note})


@login_required
def toggle_pin(request, pk):
    """
    View to toggle the pinned status of a note.

    - param request: HTTP request object.
    - param pk: Primary key of the note to be pinned.
    - return: Redirect to the note list after pinning note.
    """
    note = get_object_or_404(Note, pk=pk, user=request.user, archived=False)
    note.pinned = not note.pinned
    note.save()

    return redirect("note_list")


@login_required
def toggle_archive(request, pk):
    """
    View to toggle the archived status of a note.

    - param request: HTTP request object.
    - param pk: Primary key of the note to be archived.
    - return: Redirect to the note list after archiving note.
    """
    note = get_object_or_404(Note, pk=pk, user=request.user)
    note.archived = not note.archived
    if note.archived:
        note.pinned = False
    note.save()
    
    return redirect("note_list")
