from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from base.models import Tarea


class Logueo(LoginView):
    template_name = "base/login.html"
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('pendientes')



class PaginaRegistro (FormView):
    template_name = 'base/registro.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('pendientes')

    def form_valid(self, form):
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)

        return super().form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('pendientes')
        else:
            return super().get(*args, **kwargs)



class ListaPendientes(LoginRequiredMixin, ListView):
    model = Tarea
    context_object_name = 'Tareas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Tareas'] = context['Tareas'].filter(usuario=self.request.user)
        context['count'] = context['Tareas'].filter(completo = False).count()

        valor_buscado = self.request.GET.get('area-buscar') or ''

        if valor_buscado:

            context['Tareas'] = context['Tareas'].filter(titulo__icontains=valor_buscado)
        context['valor_buscado'] = valor_buscado

        return context



class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea
    context_object_name = 'tarea'
    template_name = 'base/tarea.html'


class CreaTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'completo']
    success_url = reverse_lazy('pendientes')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(CreaTarea, self).form_valid(form)


class EditarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'completo']
    success_url = reverse_lazy('pendientes')


class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    context_object_name = 'tarea'
    success_url = reverse_lazy('pendientes')





