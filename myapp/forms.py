from django import forms
from .models import Recipe, Comment


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions', 'prep_time', 'cook_time', 'cuisine',
                  'image_url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'prep_time': forms.NumberInput(attrs={'class': 'form-control'}),
            'cook_time': forms.NumberInput(attrs={'class': 'form-control'}),
            'cuisine': forms.Select(attrs={'class': 'form-control'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']


class CuisineSearchForm(forms.Form):
    query = forms.CharField(label='Search for recipes by cuisine', required=False)

