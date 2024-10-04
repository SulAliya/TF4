from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from rest_framework import filters

from diary.forms import DiaryForm, DiaryModeratorForm
from diary.models import DiaryEntry


class DiaryListView(LoginRequiredMixin, ListView):
    model = DiaryEntry
    paginate_by = 3

    def get_queryset(self):
        # return get_from_cache()
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset


class DiaryDetailView(DetailView):
    model = DiaryEntry


class DiaryCreateView(LoginRequiredMixin, CreateView):
    model = DiaryEntry
    form_class = DiaryForm
    success_url = reverse_lazy('diary:diaryentry_list')

    def __init__(self):
        self.object = None

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

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return DiaryForm
        if (user.has_perm('diary.can_edit_name') and user.has_perm('diary.can_edit_description')
                and user.has_perm('diary.can_edit_date_of_view') and user.has_perm('diary.can_edit_image')):
            return DiaryModeratorForm
        raise PermissionDenied


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


class IsOwnerFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """

    def filter_queryset(self, request, queryset, view):
        return queryset.filter(owner=request.user)
