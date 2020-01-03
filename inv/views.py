from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.urls import reverse_lazy
from .models import Categoria, Subcategoria, Marca, UM, Producto
from .forms import CategoriaForm, SubcategoriaForm, MarcaForm, UMForm, ProductoForm
from django.contrib import messages

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
class CategoriaNew(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    login_url = 'bases:login'
    success_message = 'Categoría creada con éxito!'

    #Se sobreescribe este método para poder tener el usuario que crea
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

#Editar 
class CategoriaEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    login_url = 'bases:login'
    success_message = 'Categoría actualizada con éxito!'

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

# ------------------------------------------------------------------ #
# --------------------- UNIDADES DE MEDIDA ------------------------- #
# ------------------------------------------------------------------ #

#Listar
class UMView(LoginRequiredMixin, generic.ListView):
    model = UM
    template_name = 'inv/um_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

#Nueva
class UMNew(LoginRequiredMixin, generic.CreateView):
    model = UM
    template_name = 'inv/um_form.html'
    context_object_name = 'obj'
    form_class = UMForm
    success_url = reverse_lazy('inv:um_list')
    login_url = 'bases:login'

    #Se sobreescribe este método para poder tener el usuario que crea
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

#Editar
class UMEdit(LoginRequiredMixin, generic.UpdateView):
    model = UM
    template_name = 'inv/um_form.html'
    context_object_name = 'obj'
    form_class = UMForm
    success_url = reverse_lazy('inv:um_list')
    login_url = 'bases:login'

    #Se sobreescribe este método para poder tener el usuario que modifica
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

# --------------------------------------------------------- #
# --------------------- PRODUCTOS ------------------------- #
# --------------------------------------------------------- #

#Listar
class ProductoView(LoginRequiredMixin, generic.ListView):
    model = Producto
    template_name = 'inv/producto_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

#Nueva
class ProductoNew(LoginRequiredMixin, generic.CreateView):
    model = Producto
    template_name = 'inv/producto_form.html'
    context_object_name = 'obj'
    form_class = ProductoForm
    success_url = reverse_lazy('inv:producto_list')
    login_url = 'bases:login'

    #Se sobreescribe este método para poder tener el usuario que crea
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

#Editar
class ProductoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Producto
    template_name = 'inv/producto_form.html'
    context_object_name = 'obj'
    form_class = ProductoForm
    success_url = reverse_lazy('inv:producto_list')
    login_url = 'bases:login'

    #Se sobreescribe este método para poder tener el usuario que modifica
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


# ---------------------------------------------------------- #
# --------------------- FUNCIONES -------------------------- #
# ---------------------------------------------------------- #

#Desactivar MARCAS
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
        marca.save()
        messages.success(request, 'Marca desactivada con éxito!')
        return redirect("inv:marca_list")

    return render(request, template_name, contexto)

#Desactivar UNIDADES DE MEDIDA
def um_inactivar(request, id):
    um = UM.objects.filter(pk=id).first()
    contexto={}
    template_name='inv/catalogos_del.html'

    if not um:
        return redirect("inv:um_list")

    if request.method=='GET':
        contexto={'obj':um}

    if request.method=='POST':
        um.estado=False
        um.save()
        return redirect("inv:um_list")

    return render(request, template_name, contexto)

#Desactivar PRODUCTOS
def producto_inactivar(request, id):
    prod = Producto.objects.filter(pk=id).first()
    contexto={}
    template_name='inv/catalogos_del.html'

    if not prod:
        return redirect("inv:producto_list")

    if request.method=='GET':
        contexto={'obj':prod}

    if request.method=='POST':
        prod.estado=False
        prod.save()
        return redirect("inv:producto_list")

    return render(request, template_name, contexto)