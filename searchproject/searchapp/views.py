from django.shortcuts import render
from .models import Country
from .forms import SearchForm
from django.http import JsonResponse

def searchs(request):
    form = SearchForm()
    query = request.GET.get('query', '')
    countries = Country.objects.filter(name__icontains=query) | Country.objects.filter(capital__icontains=query)

    # For autocomplete suggestions
    if request.is_ajax():
        results = list(countries.values('name', 'capital'))
        return JsonResponse(results, safe=False)

    return render(request, 'search.html', {'form': form, 'countries': countries})