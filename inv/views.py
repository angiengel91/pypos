from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from .models import Categoria, Subcategoria, Marca
from .forms import CategoriaForm, SubcategoriaForm, MarcaForm

# --------------------------------------------------------------- #
# --------------------- CATEGORIAS ------------------------------ #
# --------------------------------------------------------------- #

#Listar
class CategoriaView(LoginRequiredMixin, generic.ListView):
    model = Categoria
    template_name = 'inv/categoria_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

#Nueva
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

#Editar 
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

#Borrar
class CategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model = Categoria
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:categoria_list')

# ------------------------------------------------------------------ #
# --------------------- SUBCATEGORIAS ------------------------------ #
# ------------------------------------------------------------------ #

#Listar
class SubcategoriaView(LoginRequiredMixin, generic.ListView):
    model = Subcategoria
    template_name = 'inv/subcategoria_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

#Nueva
class SubcategoriaNew(LoginRequiredMixin, generic.CreateView):
    model = Subcategoria
    template_name = 'inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubcategoriaForm
    success_url = reverse_lazy('inv:subcategoria_list')
    login_url = 'bases:login'

    #Se sobreescribe este método para poder tener el usuario que crea
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

#Editar
class SubcategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Subcategoria
    template_name = 'inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubcategoriaForm
    success_url = reverse_lazy('inv:subcategoria_list')
    login_url = 'bases:login'

    #Se sobreescribe este método para poder tener el usuario que modifica
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

#Borrar
class SubcategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model = Subcategoria
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:subcategoria_list')

# ---------------------------------------------------------- #
# --------------------- MARCA ------------------------------ #
# ---------------------------------------------------------- #

#Listar
class MarcaView(LoginRequiredMixin, generic.ListView):
    model = Marca
    template_name = 'inv/marca_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

#Nueva
class MarcaNew(LoginRequiredMixin, generic.CreateView):
    model = Marca
    template_name = 'inv/marca_form.html'
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url = reverse_lazy('inv:marca_list')
    login_url = 'bases:login'

    #Se sobreescribe este método para poder tener el usuario que crea
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

#Editar
class MarcaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Marca
    template_name = 'inv/marca_form.html'
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url = reverse_lazy('inv:marca_list')
    login_url = 'bases:login'

    #Se sobreescribe este método para poder tener el usuario que modifica
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

#Función Para desactivar 
def marca_inactivar(request, id):
    marca = Marca.objects.filter(pk=id).first()
    contexto={}
    template_name='inv/catalogos_del.html'

    if not marca:
        return redirect("inv:marca_list")

    if request.method=='GET':
        contexto={'obj':marca}

    if request.method=='POST':
        marca.estado=False
        marca.Save()
        return redirect("inv:marca_list")

    return render(request, template_name, contexto)