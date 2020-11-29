from django import forms

from vkusnooo_app.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        # widgets = {
        #     'type': forms.ModelChoiceField(attrs={'class': 'form-control'}),
        #     'title': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
        #     'ingredients': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        #     'photo': forms.FileInput(attrs={'class': 'custom-file-input'}),
        #     'video': forms.FileInput(attrs={'class': 'custom-file-input'}),
        #     'time': forms.IntegerField(attrs={'class': 'custom-file-input'}),
        # }
        fields = '__all__'


class CommentForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control rounded-2',
            }
        )
    )

