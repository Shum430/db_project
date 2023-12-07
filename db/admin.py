from django.contrib import admin
from .models import Alien, Human, Spaceship, Abduction, Escape, Transportation, Experiment, Tour, LinkingTour, AlienKill


@admin.register(Alien)
class AlienAdmin(admin.ModelAdmin):
    list_display = ["alien_name"]


@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    list_display = ["human_name"]


@admin.register(Spaceship)
class SpaceshipAdmin(admin.ModelAdmin):
    list_display = ["spaceship_name"]


@admin.register(Abduction)
class AbductionAdmin(admin.ModelAdmin):
    list_display = ["abduction_date", "spaceship", "alien", "human"]


@admin.register(Escape)
class EscapeAdmin(admin.ModelAdmin):
    list_display = ["abduction_date", "spaceship", "alien", "human"]


@admin.register(Transportation)
class TransportationAdmin(admin.ModelAdmin):
    list_display = ["transportation_date", "spaceship_from", "spaceship_to", "alien", "human"]


@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    list_display = ["name", "experiment_date", "spaceship", "alien", "human"]


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ["tour_date", "spaceship", "alien", "name"]


@admin.register(LinkingTour)
class LinkingTourAdmin(admin.ModelAdmin):
    list_display = ["tour", "human"]


@admin.register(AlienKill)
class AlienKillAdmin(admin.ModelAdmin):
    list_display = ["kill_date", "alien", "human"]
