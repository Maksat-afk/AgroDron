from django.http import JsonResponse
from django.views import View
from .models import Article

class ArticleListView(View):
    def get(self, request):
        articles = list(Article.objects.values())
        return JsonResponse(articles, safe=False)

class ArticleDetailView(View):
    def get(self, request, pk):
        article = Article.objects.get(pk=pk)
        return JsonResponse({
            "title": article.title,
            "text": article.text,
            "author": article.author
        })
