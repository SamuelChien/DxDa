from django.http import HttpResponse

def user(request):
    html = "<html><body>Hello World!</body></html>"
    return HttpResponse(html)

