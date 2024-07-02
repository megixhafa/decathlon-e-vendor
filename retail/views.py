# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render

# def index(request):
#     return render(request, 'C:/Users/Megi/myproject/retail/templates/retail/index.html')

from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd

# Load the CSV file
df = pd.read_csv('static/all_data_with_summary_v4.csv')


def index(request):
    random_products = df.sample(n=12).to_dict(orient='records')
    return render(request, 'retail/index.html', {'random_products': random_products})

def search(request):
    query = request.GET.get('query', '')
    if not query:
        return JsonResponse([], safe=False)

    # Perform the search
    results = df[df['dsm'].str.lower() == query.lower()]
    results_list = results.to_dict(orient='records')
    return JsonResponse(results_list, safe=False)