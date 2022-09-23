from django.shortcuts import render
from . converter import converter
from .data import data_set


def home(request):
    if request.method == "POST":
        source_text = request.POST["source_text"]
        result_text = converter(source_text, data_set)
        source_text = source_text.strip()
        result_text = result_text.strip()
        result = {'source_text': source_text, 'result_text': result_text}
        return render(request, 'converter/home.html', {'result': result})
    else:
        return render(request, 'converter/home.html')
