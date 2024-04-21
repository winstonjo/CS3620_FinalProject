from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Recipe, Comment
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import RecipeForm, CommentForm, CuisineSearchForm


def base(request):
    return render(request, 'myapp/base.html')


class RecipeListView(ListView):
    model = Recipe
    template_name = 'myapp/recipe_list.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(cuisine__name__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = CuisineSearchForm(self.request.GET or None)
        return context


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'myapp/recipe_detail.html'


class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'myapp/recipe_form.html'
    success_url = reverse_lazy('recipe_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        print("Form is valid, redirected to:", self.get_success_url())
        return response

    def form_invalid(self, form):
        print("Form is invalid", form.errors)
        return super().form_invalid(form)


class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'myapp/recipe_delete.html'
    success_url = reverse_lazy('recipe_list')


class RecipeUpdateView(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'myapp/recipe_form.html'
    success_url = reverse_lazy('recipe_list')


def comment_view(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comments')
    else:
        form = CommentForm()
    comments = Comment.objects.all()
    return render(request, 'myapp/comments.html', {'comments': comments, 'form': form})




