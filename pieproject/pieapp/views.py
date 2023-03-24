from django.http import HttpResponse
from django.views import View

class HomePage(View):
    greeting = "Hello there!"

    def get(self, request):
        return HttpResponse(self.greeting)
