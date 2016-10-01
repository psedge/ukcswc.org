import markdown
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from content.models import Page


class PageView(DetailView):
    template_name = 'pages/page.html'

    def get(self, context, **response_kwargs):
        title = str(self.kwargs['p']).replace('-', ' ')
        page = Page.objects.filter(title=title).all()

        if not page.first():
            messages.error(self.request, 'Can\'t find that page!')
            return redirect('/')

        page = page.first()

        page.html = markdown.markdown(page.content)

        return render(self.request, self.template_name, {
            'page': page
        })

