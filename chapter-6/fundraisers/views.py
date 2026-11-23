import random

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


def lipa(request, pledge_id):
    pledge = get_object_or_404(Pledge, id=pledge_id)
    return render(request, "fundraisers/lipa.html", {"pledge": pledge})


def payment_callback(request, pledge_id):
    pledge = get_object_or_404(Pledge, id=pledge_id)
    if request.method == "POST" and pledge.balance() > 0:
        reference = "SD" + str(random.randint(10000000, 99999999))
        Payment.objects.create(pledge=pledge, amount=pledge.balance(), reference=reference)
        return render(request, "fundraisers/paid.html", {"pledge": pledge, "reference": reference})
    return redirect("fundraiser_detail", fundraiser_id=pledge.fundraiser.id)
