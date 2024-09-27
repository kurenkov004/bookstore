from django.shortcuts import render # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
import pandas as pd
from .utils import get_bookname_from_id, get_chart
from .forms import SalesSearchForm 
from .models import Sale

# Create your views here
def home(request):
  #returns the template file available & the request itself
  return render(request, 'sales/home.html')

@login_required
def records(request):
  #creates an instance of SalesSearchForm imported earlier
  form = SalesSearchForm(request.POST or None)
  #initialize dataframe to None
  sales_df = None
  chart = None

  #check if button is clicked
  if request.method == 'POST':
    #read book_title and chart_type
    book_title = request.POST.get('book_title')
    chart_type = request.POST.get('chart_type')
    #display in terminal - needed for debugging during development only
    print (book_title, chart_type)

    #apply filter to extract data
    qs = Sale.objects.filter(book__name=book_title)
    if qs:
      #convert the queryset values to pandas dataframe
      sales_df = pd.DataFrame(qs.values())
      #convert the ID to Name of book
      sales_df['book_id'] = sales_df['book_id'].apply(get_bookname_from_id)

      #call get_chart()
      chart=get_chart(chart_type, sales_df, labels=sales_df['date_created'].values)
      #convert dataframe to HTML
      sales_df = sales_df.to_html()

  #pack up data to be sent to template
  context = {
    'form': form,
    'sales_df': sales_df,
    'chart': chart
  }
  #load sales/records.html page
  return render(request, 'sales/records.html', context)