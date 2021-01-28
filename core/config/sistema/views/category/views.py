from django.urls import reverse_lazy
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView


from sistema.forms import CategoryForm
from sistema.models import Category

class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Category.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Categorías'
        context['create_url'] = reverse_lazy('sistema:add')
        context['list_url'] = reverse_lazy('sistema:list')
        context['entity'] = 'Categorias'
        return  context

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "category/create.html"
    success_url = reverse_lazy('sistema:list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion.'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear nueva categoría'
        context['entity'] = 'Categorias'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return  context

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "category/create.html"
    success_url = reverse_lazy('sistema:list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'update':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion.'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar una categoría'
        context['entity'] = 'Categorias'
        context['list_url'] = self.success_url
        context['action'] = 'update'
        return context

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category/delete.html'
    success_url = reverse_lazy('sistema:list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar una categoría'
        context['entity'] = 'Categorias'
        context['list_url'] = self.success_url
        return context