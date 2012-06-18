#from django.http import HttpResponse
from polls.models import Poll
#from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
##    t = loader.get_template('polls/index.html')
##    c = Context({
##        'latest_poll_list': latest_poll_list,
##    })
##    return HttpResponse(t.render(c))
    # alternate way to above
    return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})

def detail(request, poll_id):
##    try:
##        p = Poll.objects.get(pk=poll_id)
##    except Poll.DoesNotExist:
##        raise Http404
    #return HttpResponse("You're looking at poll %s" % poll_id)
    p = get_object_or_404(Poll, pk=poll_id)
    print "testing where this goes"
    return render_to_response('polls/detail.html', {'poll': p})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
