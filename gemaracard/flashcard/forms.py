from django import forms
from .models import Flashcard
from crispy_forms.helper import FormHelper

class FlashcardForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    LANGUAGE_CHOICES = (
        ('HEB', 'Hebrew',),
        ('ARAM', 'Aramaic',),
        ('LW', 'Loanword',)
    )
    language = forms.ChoiceField(widget=forms.Select, choices=LANGUAGE_CHOICES)
    class Meta:
        model = Flashcard
        fields = ('vocab_term','language', 'part_of_speech', 'root',
                  'page_number', 'translation', 'notes',)
    # http://stackoverflow.com/questions/24783275/django-form-with-choices-but-also-with-freetext-option
