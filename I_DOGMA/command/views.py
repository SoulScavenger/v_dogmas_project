from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from rest_framework import authentication, generics
from rest_framework.permissions import IsAuthenticated

from command.constants import COMMANDS_PER_PAGE
from command.forms import CommandForm
from command.models import Command, Tag
from command.serializers import CommandCreateSerializer, CommandSerializer


# CBV
class SearchListView(ListView):
    model = Command
    paginate_by = 5

    def get_queryset(self):
        print(self.request.GET.get('query'))
        query = self.request.GET.get('query')
        object_list = Command.objects.prefetch_related(
            'tags'
        ).select_related('author')
        filtered_object_list = object_list.filter(
            Q(name__icontains=query)
            | Q(tags__name__icontains=query)
            | Q(author__username__icontains=query)
        ).distinct()
        print(filtered_object_list)
        return filtered_object_list


class CommandListView(ListView):
    model = Command
    paginate_by = COMMANDS_PER_PAGE
    queryset = Command.objects.prefetch_related(
        'tags'
    ).select_related('author')


class CommandDetailView(DetailView):
    model = Command
    form_class = CommandForm

    def get_object(self, *args, **kwargs):
        return get_object_or_404(Command.objects.prefetch_related(
            'tags'
        ).select_related('author'), id=self.kwargs['pk'])


class CommandCreateView(LoginRequiredMixin, CreateView):
    model = Command
    form_class = CommandForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('command:index')


class CommandUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Command
    form_class = CommandForm

    def test_func(self):
        object = get_object_or_404(Command.objects.prefetch_related(
            'tags'
        ).select_related('author'), id=self.kwargs['pk'])
        return object.author == self.request.user

    def get_success_url(self):
        return reverse_lazy('command:index')


class CommandDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Command
    template_name = 'command/command_form.html'

    def test_func(self):
        object = get_object_or_404(Command.objects.prefetch_related(
            'tags'
        ).select_related('author'), id=self.kwargs['pk'])
        return object.author == self.request.user

    def get_success_url(self):
        return reverse_lazy('command:index')


class TagDetailView(ListView):
    model = Command
    paginate_by = COMMANDS_PER_PAGE
    tag = None

    def get_tag(self):
        self.tag = get_object_or_404(
            Tag,
            slug=self.kwargs['tag_slug']
        )

    def get_queryset(self):
        self.get_tag()
        qs = Command.objects.prefetch_related('tags').select_related(
            'author'
        ).filter(tags=self.tag)
        return qs

    def get_context_data(self, **kwargs):
        self.get_tag()
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context


# API
class CommandAPIView(generics.ListAPIView):
    queryset = Command.optimal.all()
    serializer_class = CommandSerializer
    authentication_classes = (authentication.TokenAuthentication,
                              authentication.SessionAuthentication,
                              )
    permission_classes = (IsAuthenticated, )


class CommandAPIRetrieve(generics.RetrieveAPIView):
    queryset = Command.optimal.all()
    serializer_class = CommandSerializer
    authentication_classes = (authentication.TokenAuthentication,
                              authentication.SessionAuthentication,
                              )
    permission_classes = (IsAuthenticated, )


class CommandAPICreate(generics.ListCreateAPIView):
    queryset = Command.optimal.all()
    serializer_class = CommandCreateSerializer
    authentication_classes = (authentication.TokenAuthentication,
                              authentication.SessionAuthentication,)
    permission_classes = (IsAuthenticated, )


class CommandAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Command.optimal.all()
    serializer_class = CommandCreateSerializer
    authentication_classes = (authentication.TokenAuthentication,
                              authentication.SessionAuthentication,
                              )
    permission_classes = (IsAuthenticated, )


class CommandAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Command.optimal.all()
    serializer_class = CommandSerializer
    authentication_classes = (authentication.TokenAuthentication,
                              authentication.SessionAuthentication,
                              )
    permission_classes = (IsAuthenticated, )
