"""Views for the portfolio app."""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from portfolio.models import Project
from portfolio.forms import PortfolioForm


@login_required
def portfolio(request):
    """Render the portfolio page."""
    projects = Project.objects.all()

    if request.method == "POST":
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("portfolio:portfolio")
    else:
        form = PortfolioForm()

    return render(
        request, "portfolio/portfolio.html", {"projects": projects, "form": form}
    )
