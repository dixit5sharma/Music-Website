""" Generic View """

from django.views import generic
from .models import Album
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Import for UserForm

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

class IndexView(generic.ListView):
    template_name = "music/index.html"
    context_object_name = "all_albums"

    def get_queryset(self):
        return Album.objects.all

class DetailView(generic.DetailView):
    model = Album
    template_name = "music/detail.html"

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    # process form data
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned / normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username = username, password = password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})

''' OLD METHOD BELOW '''
# # from django.http import Http404
# # from django.template import loader    # No longer required
# # from django.http import HttpResponse  # No longer requied now
# from django.shortcuts import render, get_object_or_404     # Shortcut - loader not needed
# from .models import Album, Song
#
# def index(request):
#     all_albums = Album.objects.all()
#     # template = loader.get_template("music/index.html")  # Not needed if render is imported
#     context = { "all_albums" : all_albums }
#     # return HttpResponse(template.render(context,request)) # Not needed if render is imported
#     return render(request,"music/index.html",context)
#
#     """ Below code is not good since it involves mixed HTML and DJANGO code. Need to be separated """
#     # html = ""
#     # for album in all_albums:
#     #     html += "<a href = /music/" + str(album.id) + "/>" + album.album_title + "</a><br>"
#     # return HttpResponse(html)
#
# def detail(request, album_id):
#     # try:
#     #     album = Album.objects.get(id=album_id)
#     # except Album.DoesNotExist:
#     #     raise Http404("Album does not exist")
#
#     album = get_object_or_404(Album, pk=album_id)    # Better shortcut with get_object_or_404 module
#     # return HttpResponse("<h2>Details of album id : " + str(album_id) + "</h2>")   # No longer required now
#     return render(request,"music/detail.html",{"album":album})
#
# # def favourite(request, album_id):
# #     album = get_object_or_404(Album, pk=album_id)    # Better shortcut with get_object_or_404 module
# #     try:
# #         selected_song = album.song_set.get(pk=request.POST['song'])
# #     except (KeyError, Song.DoesNotExist):
# #         return render(request, "music/detail.html", {"album": album, 'error_message':'You did not select a valid song'})
# #     else:
# #         selected_song.is_favourite = True
# #         selected_song.save()
# #         return render(request,"music/detail.html",{"album":album})
#
""" Above is the old method. We are going to create Generic view now """