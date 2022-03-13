from datetime import datetime
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView
from .models import Notes
from  .forms import NotesForm


def get_note(request):
    current_user = request.user.id
    notes = Notes.objects.filter(user_id=current_user)
    return render(request, 'notes/notes_list.html', {'notes': notes})


def get_time():
    time = datetime.now()
    return time.strftime('%H:%M - %d.%m.%Y')


def add_note(request):
    error = ''
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            note = Notes.objects.create(title=form.cleaned_data.get('title'),
                                        date=get_time(),
                                        user_id=request.user.id)
            note.save()
            return redirect('list_note')
        else:
            error = 'Форма заполнена неверно'

    form = NotesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'notes/add_note.html', data)

class NoteUpdateView(UpdateView):
    model = Notes
    template_name = 'notes/add_note.html'
    form_class = NotesForm

class NoteDeleteView(DeleteView):
    model = Notes
    success_url = '/notes'
    template_name = 'notes/delete_note.html'


# Create your views here.
