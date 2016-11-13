from cafaapp.models import Job

def job_context(request):
    print('wow')
    context_data = dict()
    context_data['job'] = Job.filter(jid=request.POST.get('jid',False))[0]
    return context_data