from django.shortcuts import get_object_or_404, redirect, render

from .forms import PledgeForm
from .models import Fundraiser, Payment, Pledge


def home(request):
    fundraisers = Fundraiser.objects.order_by("-created")
    return render(request, "fundraisers/home.html", {"fundraisers": fundraisers})


def fundraiser_detail(request, fundraiser_id):
    fundraiser = get_object_or_404(Fundraiser, id=fundraiser_id)
    pledges = fundraiser.pledges.order_by("name")
    return render(request, "fundraisers/fundraiser_detail.html", {"fundraiser": fundraiser, "pledges": pledges})


def pledge_create(request, fundraiser_id):
    fundraiser = get_object_or_404(Fundraiser, id=fundraiser_id)
    if request.method == "POST":
        form = PledgeForm(request.POST)
        if form.is_valid():
            pledge = form.save(commit=False)
            pledge.fundraiser = fundraiser
            pledge.save()
            return redirect("fundraiser_detail", fundraiser_id=fundraiser.id)
    else:
        form = PledgeForm()
    return render(request, "fundraisers/pledge_form.html", {"fundraiser": fundraiser, "form": form})
