from django import forms
from movie_app.models import Movie_Review


class ReviewForm(forms.ModelForm):

    class Meta():
        model = Movie_Review
        fields = {'reviewrating','reviewcategory'}
