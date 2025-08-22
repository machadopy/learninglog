from django.shortcuts import render
from .models import Topic, Entry

# Create your views here.

def index(request):
    '''pagina principal do learning Logs'''
    return render(request,'learning_logs/index.html')


def topics(request):
    '''todos os Topicos'''
    topics = Topic.objects.order_by('date_added')
    entries = Entry.objects.order_by('date_added')
    context = {'topics': topics, 'entries': entries}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    '''mostra um topico'''
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return request(request, 'learning_logs/topic.html', context)