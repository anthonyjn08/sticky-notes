from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Note(models.Model):
    """
    Model for a sticky note.

    PRIORITY_CHOICES:
        - These set the priority level choices for note priority in the model.

    Fields:
        - user: ForeignKey representing the user who created the note.
        - title: Charfield for the title of the note, maximum length
          set at 100 characters.
        - content: CharField for the note content.
        - priority: IntergerField for the priority level of the note, default
          set to 1 - Low.
        - created_at: DateTimeField set to current date and time post was
          created.
        - modified_at: DateTimeField set to the date and time the post was
          modified.
        - pinned: BooleanField, as well as priority a user can pin the most
          important notes to have display priority.
        - archived: Booleanfield, one a note has been completed, a user can
          archive it to hide from main view, but can view on their archive
          page.
    """
    # Set priority levels for priority field in model.
    PRIORITY_CHOICES = [
        (1, "Low"),
        (2, "Medium"),
        (3, "High"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField()
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=1)
    pinned = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
