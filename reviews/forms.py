# reviews/forms.py
from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'placeholder': 'fale sobre sua avaliação...', 'rows': 3}),
        }