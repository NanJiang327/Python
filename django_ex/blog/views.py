from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.core.paginator import Paginator

from blog.models import Article


def hello_world(request):
    return HttpResponse("Hello World!")


def article(request):
    articles = Article.objects.all()

    return HttpResponse(articles[0].title)


def get_index_page(request):
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1

    articles = Article.objects.all()

    top5_article_list = Article.objects.order_by('-publish_date')[:5]

    paginator = Paginator(articles, 6)

    page_num = paginator.num_pages

    page_article_list = paginator.page(page)

    if page_article_list.has_next():
        next_page = page + 1
    else:
        next_page = page

    if page_article_list.has_previous():
        previous_page = page - 1
    else:
        previous_page = page

    return render(request, 'blog/index.html', {
        'article_list': page_article_list,
        'page_num': range(1, page_num + 1),
        'curr_page': page,
        'next_page': next_page,
        'previous_page': previous_page,
        'top5_article_list': top5_article_list
    })


def get_detail_page(request, article_id):
    all_article = Article.objects.all()
    previous_article_index = 0
    next_article_index = 0
    for index, article in enumerate(all_article):
        if index == 0:
            previous_article_index = 0
            next_article_index = index + 1
        elif index == len(all_article) - 1:
            next_article_index = index
            previous_article_index = index - 1
        else:
            previous_article_index = index - 1
            next_article_index = index + 1
        if article.article_id == article_id:
            curr_article = article
            previous_article = all_article[previous_article_index]
            next_article = all_article[next_article_index]
            break
    section_list = curr_article.content.split('\n')
    return render(request, 'blog/detail.html', {
        'curr_article': curr_article,
        'section_list': section_list,
        'previous_article': previous_article,
        'next_article': next_article
    })
