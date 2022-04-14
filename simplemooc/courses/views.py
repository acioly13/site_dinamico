from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import ContactForm
from .models import Course


def courses(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'courses/course_list.html', context)


def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail(course)
            form = ContactForm()
    else:
        form = ContactForm()
    context['form'] = form
    context['course'] = course

    return render(request, 'courses/course_detail.html', context)


'''class PostListView(ListView):
    model = Course


class PostDetailView(DetailView):
    model = Course
'''



