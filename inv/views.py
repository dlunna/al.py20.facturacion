#from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CategoriaModelo, SubCategoriaModel
from .forms import CategoriaForm, SubCategoriaForm
from django.urls import reverse_lazy
# Create your views here.

class CategoriaView(LoginRequiredMixin, generic.ListView):
    model = CategoriaModelo
    template_name = 'inv/categoria_list.html'
    context_object_name = 'obj'
    login_url = 'bases-space:login'

class CategoriaNew(LoginRequiredMixin, generic.CreateView):
    model = CategoriaModelo
    template_name = 'inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv-space:categoria_list')
    login_url = 'bases-space:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class CategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = CategoriaModelo
    template_name = 'inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv-space:categoria_list')
    login_url = 'bases-space:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class CategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model = CategoriaModelo
    template_name = 'inv/categoria_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv-space:categoria_list')
    login_url = 'bases-space:login'

class SubCategoriaView(LoginRequiredMixin, generic.ListView):
    model = SubCategoriaModel
    template_name = 'inv/subcategoria_list.html'
    context_object_name = 'obj'
    login_url = 'bases-space:login'

class SubCategoriaNew(LoginRequiredMixin, generic.CreateView):
    model = SubCategoriaModel
    template_name = 'inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv-space:subcategoria_list')
    login_url = 'bases-space:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class SubCategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = SubCategoriaModel
    template_name = 'inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv-space:subcategoria_list')
    login_url = 'bases-space:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class SubCategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model = SubCategoriaModel
    template_name = 'inv/categoria_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv-space:subcategoria_list')
    login_url = 'bases-space:login'
