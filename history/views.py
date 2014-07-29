from django.http import Http404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from sparkle.models import Channel
from base.models import macdown


class AllHistoryView(ListView):
    def get_queryset(self):
        return macdown.active_versions()


class ChannelHistoryView(ListView):

    def get_queryset(self):
        try:
            self.channel = Channel.objects.get(slug=self.kwargs.get('slug'))
        except Channel.DoesNotExist:
            raise Http404
        return macdown.active_versions(channel=self.channel)

    def get_context_data(self):
        data = super().get_context_data()
        data.update({'channel': self.channel})
        return data


all_ = AllHistoryView.as_view()
channel = ChannelHistoryView.as_view()
