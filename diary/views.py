
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from diary.forms import DiaryForm
from diary.models import DiaryEntry
from diary.services import get_from_cache


class DiaryListView(ListView):
    model = DiaryEntry
    paginate_by = 3

    def get_queryset(self):
        return get_from_cache()


class DiaryDetailView(DetailView):
    model = DiaryEntry


class DiaryCreateView(CreateView, LoginRequiredMixin):
    model = DiaryEntry
    form_class = DiaryForm
    success_url = reverse_lazy('diary:diaryentry_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        form.instance.user = self.request.user
        return super().form_valid(form)


class DiaryUpdateView(UpdateView):
    model = DiaryEntry
    form_class = DiaryForm
    success_url = reverse_lazy('diary:diaryentry_list')


class DiaryDeleteView(DeleteView):
    model = DiaryEntry
    success_url = reverse_lazy('diary:diaryentry_list')


class HomePageView(TemplateView):
    template_name = 'diary/home.html'


class SearchPageView(ListView):
    model = DiaryEntry
    template_name = 'diary/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = DiaryEntry.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        return object_list


