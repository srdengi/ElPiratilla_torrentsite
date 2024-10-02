
from django.urls import path
from .views import TorrentList, TorrentDetail, download_torrent, UploadTorrentView
from . import views


urlpatterns = [
    path('', TorrentList.as_view(), name = "torrent_list"),
    path("search/", views.search, name= "search"),
    path('upload/', UploadTorrentView.as_view(), name="upload_torrent"),
    path('<int:pk>', TorrentDetail.as_view(), name = "torrent_detail"),
    path('download/<int:torrent_id>/', download_torrent, name='download_torrent'),  
]
    


