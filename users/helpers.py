
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .constants import PERPAGE

def pagination(request,x):
    page = request.GET.get('page', 1)

    paginator = Paginator(x, PERPAGE)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return data