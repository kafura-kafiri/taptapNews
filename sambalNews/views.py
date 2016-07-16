from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt

from mongoengine.django.auth import User
from mongoengine import *

from django.contrib.auth import login as auth_login
from django.core.mail import send_mail

from django.contrib.auth import login
from mongoengine.django.auth import User
from mongoengine.queryset import DoesNotExist
from django.contrib import messages

import json
import re
import hashlib
import re

from .models import *
# Create your views here.

def resign(dic):
    new_dic = {}
    for key in dic:
        if 'data' in key:
            if 'data' not in new_dic:
                new_dic['data'] = {}
            new_dic['data'][key[5:-1]] = dic[key]
        else:
            new_dic[key] = dic[key]
    return new_dic

@login_required
@csrf_exempt
def index(request):
    return render(request, 'sambalNews/index.html', {})


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        """if 'data' in request.POST:
            data = request.POST['data']
            data = json.loads(data)
            """
        post = resign(request.POST)
        #  return JsonResponse({"error": post})
        if 'data' in post:
            data = post['data']
            if 'email' in data and 'username' in data and 'password' in data:
                email = data['email']
                username = data['username']
                password = data['password']
                try:
                    connect('test_1')
                    user = User.objects.get(username=username)
                    return JsonResponse({'error': 'کاربر با این نام کاربری وجود دارد'})
                except DoesNotExist:
                    #  return JsonResponse({'d':'ds'})
                    error = ''
                    if not re.match(r'^\w+$', username):
                        error += 'نام کاربری محرز نمی باشد'
                    if not re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email):
                        error += 'ایمل معتبر نمیباشد'

                    if not error:
                        connect('test_1')  # todo
                        User.create_user(username, password, email)
                        user = User.objects.get(username=username)  # request.POST['username'])
                        custom = CustomUser(user=user)
                        custom.validation_number = 1
                        custom.save()
                        user.backend = 'mongoengine.django.auth.MongoEngineBackend'
                        auth_login(request, user)
                        request.session.set_expiry(60 * 60 * 1)
                        return HttpResponseRedirect(reverse('index'))
                        return JsonResponse({'error': 'کاربر اضافه شد'})

                    return JsonResponse({'error': error})

            return JsonResponse({'error': 'اطلاعات کافی نمیباشد'})
        return JsonResponse({'error': 'اطلاعات کافی نمیباشد'})
    return render(request, 'sambalNews/login.html')
    return JsonResponse({'error': 'به صورت post ارسال نشده'})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        """if 'data' in request.POST:
            data = request.POST['data']
            data = json.loads(data)
        #  return HttpResponse(request.POST)
            """
        post = resign(request.POST)
        #  return JsonResponse({"error": post})
        if 'data' in post:
            data = post['data']
            is_user = False
            if 'password' in data:
                password = data['password']
                if 'username' in data:
                    # Todo test
                    #  return JsonResponse({'test': 'username'})
                    username = data['username']
                    if re.match(r'^\w+$', username):
                        try:
                            connect('test_1')
                            user = User.objects.get(username=username)
                            is_user = True
                        except: pass
                if 'email' in data and is_user:
                    email = data['email']
                    # Todo test
                    #  return JsonResponse({'test': 'email'})
                    if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email):
                        try:
                            connect('test_1')
                            user = User.objects.get(email=email)
                            is_user = True
                        except: pass
                if is_user and CustomUser.objects.get(user=user).validation_number != 0:
                    #  return JsonResponse({'d': user.username})
                    user.backend = 'mongoengine.django.auth.MongoEngineBackend'
                    auth_login(request, user)
                    request.session.set_expiry(60 * 60 * 1)
                    return HttpResponseRedirect(reverse('index'))
                    return JsonResponse({'error': 'کاربر وارد شد' + user.email})
                return JsonResponse({'error': 'نام کاربری و ایمیل اشتباه است'})
            return JsonResponse({'error': 'رمز عبور خالی میباشد'})
        return JsonResponse({'error': 'صفت داده وجود ندارد'})
    return render(request, 'sambalNews/login.html')
    return JsonResponse({'error': 'به صورت post ارسال نشده'})


@login_required
@csrf_exempt
def logout(request): #  NOT TESTED
    #  return JsonResponse({'kire khar': 'kirr'})
    from django.contrib.auth import logout
    logout(request)
    return JsonResponse({'data': 'کاربر خارج شد'})


@login_required
@csrf_exempt
def create_news(request):
    if request.method == 'POST':

        post = resign(request.POST)
        #  return JsonResponse({"error": post})
        if 'data' in post:
            data = post['data']
            """
        if 'data' in request.POST:
            data = request.POST['data']
            data = json.loads(data)"""
            if 'title' in data and 'source' in data and 'category' in data and 'tags' in data and 'summary' in data and 'text' in data:
                title = data['title']
                source = data['source']
                category = data['category']
                tags = data['tags']
                tags = [tag.strip() for tag in tags[1:-1].split(',')]
                #  return JsonResponse({'tags': tags})
                summary = data['summary']
                text = data['text']
                #  title = data['title']

                summary = Summary(title=title, source=source, category=category, tags=tags, summary=summary)
                news = News(summary=summary, text=text)

                if 'img' in request.FILES and 'img' in data:
                    img = request.FILES['img']
                    summary.image_index.put(img, content_type='image/' + data['img'])
                summary.save()
                news.save()
                #  return JsonResponse({'error': str(news.id)})
                return JsonResponse({'error': 'خبر افزوده شد'})
        return JsonResponse({'error': 'اطلاعات کافی نیست'})
    return render(request, 'sambalNews/admin.html', {})
    return JsonResponse({'error': 'به صورت post ارسال نشده'})

@login_required
@csrf_exempt
def add_comment(request, news_id):
    try:
        news = News.objects.get(id=news_id)
        # return JsonResponse({'news_info': news.summary.title})
        if request.method == 'POST':
            post = resign(request.POST)
            #  return JsonResponse({"error": post})
            if 'data' in post:
                data = post['data']
                """
            if 'data' in request.POST:
                data = request.POST['data']
                data = json.loads(data)"""
                comment = Comment()
                if 'like' in data:
                    comment.like = 1
                    #  return JsonResponse({'int': news.summary.like})
                    news.summary.like += 1
                if 'dislike' in data:
                    comment.like = -1
                    news.summary.dislike += 1
                if 'text' in data:
                    comment.content = data['text']
                username = request.user.username
                user = User.objects.get(username=username)
                user = CustomUser.objects.get(user=user)
                comment.author = user
                # set today to date
                comment.date = datetime.datetime.now()
                #  comment.save()
                news.comments.append(comment)
                news.save()
                return JsonResponse({'comm_info': comment.to_json()}, safe=False)

            return JsonResponse({'error': 'اطلاعات کافی نمیباشد'})
        return JsonResponse({'error': 'به صورت post ارسال نشده'})
    except DoesNotExist: return JsonResponse({'error':'چنین خبری یافت نشد'})


def query_search(query, date, cnt=10):
    return Summary.objects(is_valid=True).search_text(query).filter(publish_date__lte=date).order_by('-date')[:cnt]

#  \ Job.objects(skills__in=user_skills)
def hash_search(tags, date, cnt=10):
    return Summary.objects(tags__in=tags).filter(is_valid=True).filter(publish_date__lte=date).order_by('-date')[:cnt]

def hot_search(date, cnt=10):
    return Summary.objects(is_hot=True).filter(is_valid=True).filter(publish_date__lte=date).order_by('-date')[:cnt]

def condid_search(date, cnt=10):
    return Summary.objects(is_condid=True).filter(is_valid=True).filter(publish_date__lte=date).order_by('-date')[:cnt]

def unofficials(date, cnt=10):
    return Summary.objects(is_valid=False).filter(publish_date__lte=date).order_by('-date')[:cnt]

@login_required
@csrf_exempt
def next(request):
    if request.method == 'POST':
        post = resign(request.POST)
        #  return JsonResponse({"error": post})
        if 'data' in post:
            data = post['data']
            """
        if 'data' in request.POST:
            data = request.POST['data']
            data = json.loads(data)"""
            if 'query' in data:
                query = data['query']
                date = datetime.datetime.now()
                if 'date' in data:
                    date_str = data['date']
                    date = datetime.datetime.strptime("2016-07-14 15:56:40.601691", "%Y-%m-%d %H:%M:%S.%f")
                list = []
                #  return HttpResponse(query[1:])
                if query[0] == '/': list = query_search(query[1:], date)
                if query[0] == '#': list = hash_search([tag.strip()[1:] for tag in query.split(',')], date)
                if query[0] == '$': list = hot_search(date)
                if query[0] == '^': list = condid_search(date)
                if query[0] == '!': list = unofficials(date)

                return JsonResponse({'summaries': [obj.to_json() for obj in list]}, safe=False)

            return JsonResponse({'error': 'اطلاعات کافی نمیباشد'})
        return JsonResponse({'error': 'اطلاعات کافی نمیباشد'})
    return JsonResponse({'error': 'به صورت post ارسال نشده'})

@login_required
@csrf_exempt
def add_hashtag(request):
    username = request.user.username
    user = User.objects.get(username=username)
    user = CustomUser.objects.get(user=user)
    #  return JsonResponse({'info': user.tags})
    if request.method == 'POST':
        post = resign(request.POST)
        #  return JsonResponse({"error": post})
        if 'data' in post:
            data = post['data']
            """
        if 'data' in request.POST:
            data = request.POST['data']
            data = json.loads(data)"""
            if 'tag' in data:
                tag = data['tag']
                if tag in user.tags:
                    return JsonResponse({'error': 'این تگ موجود است'})

                #  return JsonResponse({'ino': list})
                user.tags.append(tag)
                user.save()
                #  return JsonResponse({'ino': user.tags})
                return JsonResponse({'error': 'تگ اضافه شد'})
            return JsonResponse({'error': 'اطلاعات کافی نمیباشد'})
        return JsonResponse({'error': 'اطلاعات کافی نمیباشد'})
    return JsonResponse({'error': 'به صورت post ارسال نشده'})

"""@login_required
def create_hashtag(request):
    if request.method == 'POST':
        if 'data' in request.POST:
            data = request.POST['data']
            data = json.load(data)
            if 'tag' in data:
                tag = data['tag']
                if tag in .tags:
                    return JsonResponse({'error': 'این تگ موجود است'})
                user.tags.append(data['tag'])
            return JsonResponse({'error': 'اطلاعات کافی نمیباشد'})
        return JsonResponse({'error': 'اطلاعات کافی نمیباشد'})
    return JsonResponse({'error': 'به صورت post ارسال نشده'})
    pass"""


@login_required
@csrf_exempt
def comments(request, news_id):
    try:
        news = News.objects.get(id=news_id)
        json_dict = {'comments':[comment.to_json() for comment in news.comments]}
        return JsonResponse(json.dumps(json_dict), safe=False)
    except DoesNotExist: return JsonResponse({'error':'چنین خبری یافت نشد'})




@login_required
@csrf_exempt
def block(request, blocked_username):
    username = request.user.username
    user = User.objects.get(username=username)
    user = CustomUser.objects.get(user=user)

    if user.validation_number >= 2:
        try:
            user = User.objects.get(username=blocked_username)
            user = CustomUser.objects.get(user=user)
            user.modify(upsert=True, inc__validation_number=-1)
            user.save()
            return JsonResponse({'error': 'کاربر بلاک شد'})
        except DoesNotExist:
            return JsonResponse({'error': 'کاربر مورد نظر وجود ندارد'})
    return JsonResponse({'error': 'دسترسی داده نشد'})

@login_required
@csrf_exempt
def update_hots(request):
    username = request.user.username
    manager = CustomUser.objects.get(username=username)
    if manager.validation == 2:
        likes = {}
        for news in News.objects:
            likes[str(news.id)] = news.summary.like
            news.summary.like = 0
            news.summary.dislike = 0
            author_set = set()
            for comment in news.comments:
                author = comment.author
                author_id = str(author.id)
                if author_id not in author_set:
                    if comment.like == 1:
                        news.summary.like += 1
                        author_set.add(author_id)
                    if comment.like == -1:
                        news.summary.dislike += 1
                        author_set.add(author_id)
            likes[str(news.id)] = news.summary.like - likes[str(news.id)]
        values = sorted(likes.values())
        fifth_biggest = values[-5]
        for summary in Summary.objects:
            if summary.like >= fifth_biggest:
                summary.is_hot = True
        return HttpResponse('حلله')
    return JsonResponse({'error': 'دسترسی داده نشد'})

@login_required
@csrf_exempt
def update_condids(request):
    username = request.user.username
    manager = CustomUser.objects.get(username=username)
    if manager.validation == 2:
        date = datetime.datetime.now() - datetime.timedelta(days=14)
        comments = {}
        for news in News.objects:
            comments[str(news.id)] = 0
            for comment in news.comments:
                if comment.date > date:
                    comments[str(news.id)] += 1
        values = sorted(comments.values())
        fifth_biggest = values[-5]
        for news in News.objects:
            news.summary.is_condid = False
            if comments[str(news.id)] > fifth_biggest:
                news.summary.is_condid = True
            news.summary.save()
        return JsonResponse({'error': 'حللته'})
    return JsonResponse({'error': 'دسترسی داده نشد'})

@login_required
@csrf_exempt
def delete_news(request, news_id):
    try:
        news = News.objects.get(id=news_id)
        username = request.user.username
        user = User.objects.get(username=username)
        user = CustomUser.objects.get(user=user)

        #  return HttpResponse(user.validation_number)
        if user.validation_number >= 2:
            #  return HttpResponse('ds')
            news.summary.delete()
            news.delete()
            return JsonResponse({"error": "خبر حذف شد"})
        else:
            return JsonResponse({"error": "دسترسی داده نشد"})

    except DoesNotExist:
        return JsonResponse({'error': 'چنین خبری یافت نشد'})

@login_required
@csrf_exempt
def get_news(reqest, news_id):
    news = News.objects.get(id=news_id)
    summary = news.summary
    summary.seen += 1
    summary.save()
    return JsonResponse({'news': news.to_json(), 'summary': summary.to_json()}, safe=False)

@login_required
@csrf_exempt
def img(request, news_id):
    try:
        news = News.objects.get(id=news_id)
        img = news.summary.image_index
        return HttpResponse(img.read(), content_type=img.content_type)
    except:
        return JsonResponse({'error': 'خطا'})

@login_required
@csrf_exempt
def upgrade_user(request, code):
    if code == '1234':
        username = request.user.username
        user = User.objects.get(username=username)
        user = CustomUser.objects.get(user=user)
        user.modify(upsert=True, inc__validation_number=1)
        user.save()
        #return HttpResponse(user.validation_number)
        # return HttpResponse(user.validation_number)
        return JsonResponse({'error': 'کاربر ارتقا یافت'})
    else:
        return JsonResponse({'error': 'دسترسی داده نشد'})


@login_required
@csrf_exempt
def validate(request, news_id):
    try:
        news = News.objects.get(id=news_id)
        username = request.user.username
        user = User.objects.get(username=username)
        user = CustomUser.objects.get(user=user)

        #  return HttpResponse(user.validation_number)
        if user.validation_number >= 2:
            #  return HttpResponse('ds')
            news.summary.is_valid = True
            news.summary.save()
            return JsonResponse({"error": "خبر رسمی شد"})
        else:
            return JsonResponse({"error": "دسترسی داده نشد"})

    except DoesNotExist:
        return JsonResponse({'error': 'چنین خبری یافت نشد'})