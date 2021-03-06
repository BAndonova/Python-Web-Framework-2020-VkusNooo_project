from django import forms

from vkusnooo_app.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        # fields = '__all__'
        exclude = ('created_by', 'User', 'user', 'liked')


class CommentForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control rounded-2',
            }
        )
    )

