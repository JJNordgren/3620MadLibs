import random
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .forms import MadLibForm
from .models import StoryTemplate, Submission
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, "madlibs/home.html")


def play(request):
    if not StoryTemplate.objects.exists():
        messages.error(request, "No stories exist yet. Add at least 15 StoryTemplate entries in the admin.")
        form = MadLibForm()
        return render(request, "madlibs/play.html", {"form": form})

    if request.method == "POST":
        form = MadLibForm(request.POST)
        if form.is_valid():
            story = random.choice(list(StoryTemplate.objects.all()))
            data = form.cleaned_data

            try:
                rendered = story.template_text.format(**data)
            except KeyError:
                messages.error(request, "A story template has a placeholder that doesn't match the form fields.")
                return render(request, "madlibs/play.html", {"form": form})

            submission = Submission.objects.create(
                story=story,
                user=request.user if request.user.is_authenticated else None,
                data=data,
                rendered_text=rendered,
            )
            return redirect("madlibs:result", submission_id=submission.id)
    else:
        form = MadLibForm()

    return render(request, "madlibs/play.html", {"form": form})


def result(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    return render(request, "madlibs/result.html", {"submission": submission})

## Login required stops someone who isn't logged in from seeing all submissions by not logged in people
## Could implement that later as a board to see anonymous submissions if I continue working on this.
@login_required
def my_submissions(request):
    submissions = Submission.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "madlibs/submissions.html", {"submissions": submissions})
