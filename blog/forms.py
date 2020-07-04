from django import forms
from .models import Post
from .models import Event

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('title', 'year', 'month', 'month_to_display', 'description')
