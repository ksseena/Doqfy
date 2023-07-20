from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from snippets.models import Snippet

def create_snippet(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        secret_key = request.POST.get('secret_key')
        snippet = Snippet.objects.create(content=content, secret_key=secret_key)
        return redirect('view_snippet', snippet_id=snippet.id)
    return render(request, 'create_snippet.html')

def view_snippet(request, snippet_id):
    snippet = get_object_or_404(Snippet, id=snippet_id)
    if request.method == 'POST':
        provided_key = request.POST.get('secret_key')
        if provided_key == snippet.secret_key:
            return HttpResponse(snippet.content)
        else:
            return HttpResponse('Invalid key')
    return render(request, 'view_snippet.html')
