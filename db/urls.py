from django.contrib import admin
from django.urls import path
from db.views import (
    index,
    HumanListView,
    AlienListView,
    SpaceshipListView,
    possibilities,
    alien_robbing_human_view,
    human_escaping_ship_view,
    alien_transporting_human_view,
    aliens_making_experiment_view,
    alien_making_tour_view,
    human_killing_alien_view,
    abduction_query_view, spaceship_query_view, robbing_alien_query_view, killed_alien_query_view,
    robbed_and_killed_query_view,
    rob_n_people_query_view, robbed_n_times_query_view, common_excursion_experiment_query_view,
    AbductionListView, twelve_task_query_view, eleven_task_query_view, ten_task_query_view, ninth_task_query_view,
    ExperimentListView, TourListView
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("humans/", HumanListView.as_view(), name="human-list"),
    path("aliens/", AlienListView.as_view(), name="alien-list"),
    path("spaceships/", SpaceshipListView.as_view(), name="spaceship-list"),
    path("possibilities/", possibilities, name="events-and-queries"),
    path("abductions/", AbductionListView.as_view(), name="abduction-list"),
    path("experiments/", ExperimentListView.as_view(), name="experiment-list"),
    path("tours/", TourListView.as_view(), name="tour-list"),
    path("possibilities/alien_robbing_human/", alien_robbing_human_view, name="alien_robbing_human_form"),
    path("possibilities/human_escaping_ship/", human_escaping_ship_view, name="human_escaping_ship_form"),
    path("possibilities/alien_transporting_human/", alien_transporting_human_view,
         name="alien_transporting_human_form"),
    path("possibilities/aliens_making_experiment_form", aliens_making_experiment_view, name="aliens_making_experiment_form"),
    path("possibilities/alien_making_tour_form", alien_making_tour_view, name="alien_making_tour_form"),
    path("possibilities/human_killing_alien_form", human_killing_alien_view, name="human_killing_alien_form"),
    path("possibilities/abduction_results", abduction_query_view, name="abduction_query_form"),
    path("possibilities/spaceship_results", spaceship_query_view, name="spaceship_query_form"),
    path("possibilities/robbing_results", robbing_alien_query_view, name="robbing_results_form"),
    path("possibilities/killed_results", killed_alien_query_view, name="killed_results_form"),
    path("possibilities/rob_killed_results", robbed_and_killed_query_view, name="robbed_and_killed_results_form"),
    path("possibilities/rob_n_people_results", rob_n_people_query_view, name="rob_n_people_results_form"),
    path("possibilities/robbed_n_times_results", robbed_n_times_query_view, name="robbed_n_times_results_form"),
    path(
        "possibilities/common_excursion_experiment_results",
        common_excursion_experiment_query_view,
        name="common_excursion_experiment_results_form"
    ),
    path(
        "possibilities/ninth_task_results",
        ninth_task_query_view,
        name="ninth_task_results_form"
    ),
    path(
        "possibilities/ten_task_results",
        ten_task_query_view,
        name="ten_task_results_form"
    ),
    path(
        "possibilities/eleven_task_results",
        eleven_task_query_view,
        name="eleven_task_results_form"
    ),
    path(
        "possibilities/twelve_task_results",
        twelve_task_query_view,
        name="twelve_task_results_form"
    )
]


app_name = "db"
