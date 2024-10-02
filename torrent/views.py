from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from torrent.forms import TorrentForm
from .models import torrent
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView





#class TorrentList(ListView):
 #   model = torrent
    #context_object_name = ""
    #template_name = ""



class UploadTorrentView(FormView):
    template_name = 'torrent/upload_torrent.html'  # Asegúrate de tener una plantilla llamada upload_torrent.html
    form_class = TorrentForm
    success_url = reverse_lazy('torrent_list')  # Cambia 'nombre_de_tu_url_de_exito' por la URL a la que quieres redirigir después de enviar el formulario

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class TorrentDetail(DetailView):
    model =  torrent

    #template_name = ""


class TorrentList(ListView):
    model = torrent
    template_name = 'torrent/torrent_list.html'
    context_object_name = 'torrents'


def download_torrent(request, torrent_id):
    torrent_obj = get_object_or_404(torrent, pk=torrent_id)
    torrent_file = torrent_obj.torrent_file
    response = FileResponse(torrent_file.open(), content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{torrent_file.name}"'
    return response

class HomeView(ListView):
    model = torrent
    template_name = "torrent/index.html"

#funcion de busqueda
def search(request):
    query = request.GET.get("q")

    if query:
        results = torrent.objects.filter(title__icontains = query)
    else:
        results = []
    
    return render(request, "torrent/search_results.html", {"results" : results, "query" : query})

