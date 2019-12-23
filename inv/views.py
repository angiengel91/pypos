from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from .models import Categoria
from .forms import CategoriaForm

#Vista Categorías
class CategoriaView(LoginRequiredMixin, generic.ListView):
    model = Categoria
    template_name = 'inv/categoria_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

#Vista Nueva Categoria
class CategoriaNew(LoginRequiredMixin, generic.CreateView):
    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    login_url = 'bases:login'

    #Se sobreescribe este método para poder tener el usuario que crea
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

#Vista Editar Categoria
class CategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    login_url = 'bases:login'

    #Se sobreescribe este método para poder tener el usuario que modifica
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

#Vista Borrar Categoria
class CategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model = Categoria
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:categoria_list')