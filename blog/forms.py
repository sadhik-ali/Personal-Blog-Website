from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
                'style': 'width: 100%; height: 45px; padding: 10px;'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email',
                'style': 'width: 100%; height: 45px; padding: 10px;'
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your Comment',
                'rows': 5,
                'style': 'width: 100%; padding: 10px; resize: vertical;'
            }),
        }
