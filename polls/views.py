from django.http import HttpResponse, HttpResponseRedirect
from polls.models import Poll, Choice
from django.core.urlresolvers import reverse
#from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.template import RequestContext
from django.views.generic import DetailView

#- Only the Vote view is being used currently after switching to generic views
#  (DetailView and ListView) that just take the default model objects and
#  display them based on templates.  Had to also switch the reverse function to
# the name we assigned for the results.

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
    return render_to_response('polls/detail.html', {'poll': p},
                              context_instance=RequestContext(request))

def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/results.html', {'poll': p})

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        print "No choice selected"
        return render_to_response('polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after dealing with
        # Post data successfully.  This prevents data from being posted twice
        # if user hits back (basic rest stuff)
        return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))
    
#  Testing subclassing Detail view for a view.
class PollDetailView(DetailView):
    print "Poll detail view: " 
    template_name = "polls/detail.html"
    model = Poll

    print "template name set %s" % template_name
