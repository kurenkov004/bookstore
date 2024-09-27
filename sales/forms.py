from django import forms

#display choices defined as a tuple
CHART_CHOICES = (
  ('#1', 'Bar chart'),
  ('#2', 'Pie chart'),
  ('#3', 'Line chart')
)

#class-cased Form imported from Django
class SalesSearchForm(forms.Form):
  book_title = forms.CharField(max_length=120)
  chart_type = forms.ChoiceField(choices=CHART_CHOICES)