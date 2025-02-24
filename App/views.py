from pydoc import pager
from .models import Song
# from django.contrib.admin.templatetags.admin_list import paginator_number
from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    paginator = Paginator(Song.object.all(),1)
    pager_number = request.GET.get('page')
    page_obj = paginator.get_page(pager_number)
    context = {"page_obj":page_obj}

    return render(request, "index.html", context)