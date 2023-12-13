from django.db.models import Count
from django.views import generic
from django.shortcuts import render
from .models import (
    Human,
    Alien,
    Spaceship,
    Abduction,
    Escape,
    Experiment,
    Tour,
    AlienKill, LinkingTour, Transportation
)
from .forms import (
    AlienRobHumanForm,
    HumanEscapeForm,
    AlienTransportForm,
    AliensMakeExperimentForm,
    AlienMakesTourForm,
    HumanKillsAlienForm,
    AbductionQueryForm,
    SpaceshipQueryForm,
    RobbingAlienSearchForm,
    KilledAlienSearchForm,
    KillRobbedSearchForm,
    RobNPeopleSearchForm, RobbedNTimesSearchForm, CommonExcursionExperimentSearchForm, NinthTaskSearchForm,
)


def index(request):
    num_humans = Human.objects.count()
    num_aliens = Alien.objects.count()  # Fix: Use Alien.objects.count() instead of Human.objects.count()
    num_ships = Spaceship.objects.count()  # Fix: Use Spaceship.objects.count() instead of Human.objects.count()

    context = {
        "num_humans": num_humans,
        "num_aliens": num_aliens,
        "num_ships": num_ships,
    }

    return render(request, "db/index.html", context=context)


class AlienListView(generic.ListView):
    model = Alien
    template_name = "db/alien_list.html"
    queryset = Alien.objects.order_by("id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_aliens"] = Alien.objects.count()
        return context


class HumanListView(generic.ListView):
    model = Human
    template_name = "db/human_list.html"
    queryset = Human.objects.order_by("id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_humans"] = Human.objects.count()
        return context


class SpaceshipListView(generic.ListView):
    model = Spaceship
    template_name = "db/spaceship_list.html"
    queryset = Spaceship.objects.order_by("id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_ships"] = Spaceship.objects.count()
        return context


def possibilities(request):
    return render(request, "db/possibilities.html")


def alien_robbing_human_view(request):
    if request.method == "GET":
        context = {
            "form": AlienRobHumanForm()
        }
        return render(request, "db/alien_robbing_human_form.html", context=context)
    elif request.method == "POST":
        form = HumanEscapeForm(request.POST)
        if form.is_valid():
            Abduction.objects.create(**form.cleaned_data)
        context = {
            "form": form,
        }
        return render(request, 'db/alien_robbing_human_form.html', context=context)


def human_escaping_ship_view(request):
    if request.method == "GET":
        context = {
            "form": HumanEscapeForm()
        }
        return render(request, "db/human_escaping_ship_form.html", context=context)
    elif request.method == "POST":
        form = HumanEscapeForm(request.POST)
        if form.is_valid():
            # Get the human and spaceship objects based on the form data
            human_name = form.cleaned_data['human']
            spaceship_name = form.cleaned_data['spaceship']

            # Check if the specified human exists on the specified spaceship
            human_on_spaceship = Human.objects.filter(human_name=human_name, abduction__spaceship__spaceship_name=spaceship_name).exists()

            if human_on_spaceship:
                # Human is on the spaceship, create the Escape object
                Escape.objects.create(**form.cleaned_data)
            else:
                # Human is not on the specified spaceship, handle the error
                form.add_error('human', 'Selected human is not on the specified spaceship.')

        context = {
            "form": form,
        }
        return render(request, "db/human_escaping_ship_form.html", context=context)


def alien_transporting_human_view(request):
    success_message = None

    if request.method == 'POST':
        # If the form is submitted
        form = AlienTransportForm(request.POST)

        if form.is_valid():
            # Form is valid, create a new instance of the Transportation model
            transportation_date = form.cleaned_data['transportation_date']
            spaceship_from = form.cleaned_data['spaceship_from']
            spaceship_to = form.cleaned_data['spaceship_to']
            alien = form.cleaned_data['alien']
            human = form.cleaned_data['human']

            # Create a new instance of the Transportation model
            transportation = Transportation.objects.create(
                transportation_date=transportation_date,
                spaceship_from=spaceship_from,
                spaceship_to=spaceship_to,
                alien=alien,
                human=human
            )

            # Optionally, you can do additional processing here

            # Set a success message
            success_message = "Transportation successful!"

    else:
        # If it's a GET request, create a new form
        form = AlienTransportForm()

    # Render the template with the form and the success message
    return render(request, 'db/alien_transporting_human_form.html', {'form': form, 'success_message': success_message})


def aliens_making_experiment_view(request):
    if request.method == "GET":
        context = {
            "form": AliensMakeExperimentForm()
        }
        return render(request, "db/aliens_making_experiment_form.html", context=context)
    elif request.method == "POST":
        form = AliensMakeExperimentForm(request.POST)
        if form.is_valid():
            Experiment.objects.create(**form.cleaned_data)
        context = {
            "form": form,
        }
        return render(request, "db/aliens_making_experiment_form.html", context=context)


def alien_making_tour_view(request):
    if request.method == "GET":
        context = {
            "form": AlienMakesTourForm()
        }
        return render(request, "db/alien_making_tour_form.html", context=context)
    elif request.method == "POST":
        form = AlienMakesTourForm(request.POST)
        if form.is_valid():
            Tour.objects.create(**form.cleaned_data)
        context = {
            "form": form,
        }
        return render(request, "db/alien_making_tour_form.html", context=context)


def human_killing_alien_view(request):
    if request.method == "GET":
        context = {
            "form": HumanKillsAlienForm()
        }
        return render(request, "db/human_killing_alien_form.html", context=context)
    elif request.method == "POST":
        form = HumanKillsAlienForm(request.POST)
        if form.is_valid():
            AlienKill.objects.create(**form.cleaned_data)
        context = {
            "form": form,
        }
        return render(request, "db/human_killing_alien_form.html", context=context)


# views for queries
def abduction_query_view(request):
    abducted_humans = []

    if request.method == 'POST':
        form = AbductionQueryForm(request.POST)
        if form.is_valid():
            alien = form.cleaned_data['alien']
            min_abductions = form.cleaned_data['min_abductions']
            date_from = form.cleaned_data['date_from']
            date_to = form.cleaned_data['date_to']

            abductions = Abduction.objects.filter(alien=alien, abduction_date__range=(date_from, date_to))

            abducted_humans = [human for human in Human.objects.all() if
                               abductions.filter(human=human).count() >= min_abductions]

    else:
        form = AbductionQueryForm()

    context = {"form": form, "abducted_humans": abducted_humans}
    return render(request, "db/abduction_results_form.html", context)


def spaceship_query_view(request):
    spaceships = []  # Initialize spaceships before the if block

    if request.method == 'POST':
        form = SpaceshipQueryForm(request.POST)
        if form.is_valid():
            human = form.cleaned_data['human']
            date_from = form.cleaned_data['date_from']
            date_to = form.cleaned_data['date_to']

            # Знайти кораблі через модель Abduction
            spaceships = Spaceship.objects.filter(abduction__human=human,
                                                  abduction__abduction_date__range=(date_from, date_to)).distinct()
    else:
        form = SpaceshipQueryForm()

    context = {"form": form, "spaceships": spaceships}
    return render(request, 'db/spaceship_results_form.html', context=context)


def robbing_alien_query_view(request):
    robbing_aliens = []

    if request.method == 'POST':
        form = RobbingAlienSearchForm(request.POST)
        if form.is_valid():
            human = form.cleaned_data['human']
            min_abductions = form.cleaned_data['min_abductions']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            # Find aliens who abducted the specific human at least N times within the specified period
            robbing_aliens = Alien.objects.filter(
                abduction__human=human,
                abduction__abduction_date__range=(start_date, end_date)
            ).annotate(abduction_count=Count('abduction')).filter(abduction_count__gte=min_abductions).distinct()

    else:
        form = RobbingAlienSearchForm()

    context = {"form": form, "robbing_aliens": robbing_aliens}
    return render(request, 'db/robbing_results_form.html', context=context)


def killed_alien_query_view(request):
    killed_aliens = []

    if request.method == 'POST':
        form = KilledAlienSearchForm(request.POST)
        if form.is_valid():
            human = form.cleaned_data['human']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            # Find aliens killed by the specific human within the specified period
            killed_aliens = Alien.objects.filter(
                alienkill__human=human,
                alienkill__kill_date__range=(start_date, end_date)
            ).distinct()

    else:
        form = KilledAlienSearchForm()

    context = {"form": form, "killed_aliens": killed_aliens}
    return render(request, 'db/killed_results_form.html', context=context)


def robbed_and_killed_query_view(request):
    robbed_and_killed_aliens = []

    if request.method == 'POST':
        form = KillRobbedSearchForm(request.POST)
        if form.is_valid():
            human = form.cleaned_data['human']

            # Find aliens who abducted the specific human and were killed by the same human
            robbed_and_killed_aliens = Alien.objects.filter(
                abduction__human=human,
                alienkill__human=human
            ).distinct()

    else:
        form = KillRobbedSearchForm()

    context = {"form": form, "robbed_and_killed_aliens": robbed_and_killed_aliens}
    return render(request, 'db/robbed_and_killed_form.html', context=context)


def rob_n_people_query_view(request):
    robbed_aliens = []

    if request.method == 'POST':
        form = RobNPeopleSearchForm(request.POST)
        if form.is_valid():
            min_abduction = form.cleaned_data['min_abduction']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            # Find aliens who abducted at least N different people within the specified period
            robbed_aliens = Alien.objects.filter(
                abduction__abduction_date__range=(start_date, end_date)
            ).annotate(abduction_count=Count('abduction__human', distinct=True)).filter(
                abduction_count__gte=min_abduction
            ).distinct()

    else:
        form = RobNPeopleSearchForm()

    context = {"form": form, "rob_aliens": robbed_aliens}
    return render(request, 'db/rob_n_people_form.html', context=context)


def robbed_n_times_query_view(request):
    abducted_humans = []

    if request.method == 'POST':
        form = RobbedNTimesSearchForm(request.POST)
        if form.is_valid():
            min_abduction = form.cleaned_data['min_abduction']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            # Find humans who were abducted at least N times within the specified period
            abducted_humans = Human.objects.filter(
                abduction__abduction_date__range=(start_date, end_date)
            ).annotate(abduction_count=Count('abduction')).filter(
                abduction_count__gte=min_abduction
            ).distinct()

    else:
        form = RobbedNTimesSearchForm()

    context = {"form": form, "abducted_humans": abducted_humans}
    return render(request, 'db/robbed_n_times_form.html', context=context)


def common_excursion_experiment_query_view(request):
    common_events = []

    if request.method == 'POST':
        form = CommonExcursionExperimentSearchForm(request.POST)
        if form.is_valid():
            alien = form.cleaned_data['alien']
            human = form.cleaned_data['human']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            # Find all common excursions and experiments for the specified alien and human
            tour_events = Tour.objects.filter(
                alien=alien,
                tour_date__range=(start_date, end_date),
                humans=human
            )

            experiment_events = Experiment.objects.filter(
                alien=alien,
                experiment_date__range=(start_date, end_date),
                human=human
            )

            # Combine results into a single list
            common_events = list(tour_events) + list(experiment_events)

    else:
        form = CommonExcursionExperimentSearchForm()

    context = {"form": form, "common_events": common_events}
    return render(request, 'db/common_excursion_experiment_form.html', context=context)


def ninth_task_query_view(request):
    result = None

    if request.method == 'POST':
        form = NinthTaskSearchForm(request.POST)
        if form.is_valid():
            alien = form.cleaned_data['alien']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            min_abduction = form.cleaned_data['min_abduction']

            # Query to find the number of tours for the given alien and meeting the criteria
            result = LinkingTour.objects.filter(
                tour__alien=alien,
                tour__tour_date__range=(start_date, end_date)
            ).annotate(num_humans=Count('tour__humans')).filter(num_humans__gte=min_abduction).count()

    else:
        form = NinthTaskSearchForm()

    context = {"form": form, "result": result}
    return render(request, 'db/ninth_task_form.html', context=context)



