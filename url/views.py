from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect, HttpResponse

from .models import UrlForm, Url

import uuid
from django.utils.translation import ugettext as _

# Create your views here.

@require_http_methods(["GET", "POST"])
def newuri(request):
    """
        Muestra el formulario para introducir la url
        y retorna la url acortada.
    """
    shorturl=None

    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            # Se guarda y se devuelve la Url
            obj=form.save()
            shorturl=obj.shorturl.hex
            
            # Se limpia el form por si se desea arcortar más urls
            form=UrlForm()

    else:
        form = UrlForm()

    return render(request, 'url.html', {'shorturl':shorturl, 'form':form} )


@require_http_methods(["GET",])
def geturi(request, urlpk):
    """
        Expande la url
    """
    uri=get_object_or_404(Url, shorturl=uuid.UUID(urlpk))
    return HttpResponseRedirect(uri.url)
