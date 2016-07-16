from sambalNews.models import *
from mongoengine import *
from random import randint, random

db = connect('test_1')


tags = ['ali', 'poo', 'نماز', 'baalesh', 'بیجامه', 'شاهرخ', 'وزیر', 'بی رخ', 'عاشق اصفهانی', 'khordaad',]
words = ['است', 'طاقت فرسا', 'ایستگاه', 'مولای', 'اتوبوس', 'انتقال', 'حضرت', 'هوا',
         'من', 'آلاینده ها', 'بود', 'برخورد جددی', 'توانا', 'امر', 'ترفند ناب', 'اگر چه',
         'دربند', 'تریپت منو ..', 'ما', 'خبر', 'مالیخولیا', 'روند', 'مشکلات روزمره', 'نانوایی', ]

def produce_list(E, list):
    l = randint(-E + 1, E - 1) + E
    s = []
    while len(s) != l:
        s.append(list[randint(0, len(list) - 1)])
    return s

def produce_string(E):
    return ' '.join(produce_list(E, words)) + '.'


for i in range(1000):
    summary = Summary(title=produce_string(4))
    summary.tags = produce_list(2, tags)
    summary.is_hot = True if random() < .5 else False
    summary.is_condid = True if random() < .5 else False
    summary.is_valid = True if random() < .5 else False
    d = randint(1, 26)
    m = randint(1, 12)
    date = datetime.datetime.strptime("2016-" + str(m) + "-" + str(d) + " 15:56:40.601691", "%Y-%m-%d %H:%M:%S.%f")
    summary.publish_date = date

    dir = '/home/pouriya/PycharmProjects/taptapNews/sambalNews/img/'
    name = 'images (%d).jpg' %randint(0, 13)
    with open(dir + name, 'rb') as img:
        summary.image_index.put(img, content_type='image/' + 'jpg')

    news = News(text=produce_string(30))
    news.summary = summary
    summary.save()
    news.save()
