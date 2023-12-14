from django import forms

from .models import Alien, Human, Spaceship


class AlienRobHumanForm(forms.Form):
    abduction_date = forms.DateField(
        widget=forms.widgets.DateInput(
            attrs={'type': 'date'}
        )
    )
    alien = forms.ModelChoiceField(queryset=Alien.objects.all())
    human = forms.ModelChoiceField(queryset=Human.objects.all())
    spaceship = forms.ModelChoiceField(queryset=Spaceship.objects.all())


class HumanEscapeForm(forms.Form):
    abduction_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    alien = forms.ModelChoiceField(queryset=Alien.objects.all())
    human = forms.ModelChoiceField(queryset=Human.objects.all())
    spaceship = forms.ModelChoiceField(queryset=Spaceship.objects.all())


class AlienTransportForm(forms.Form):
    transportation_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    spaceship_from = forms.ModelChoiceField(queryset=Spaceship.objects.all())
    spaceship_to = forms.ModelChoiceField(queryset=Spaceship.objects.all())
    alien = forms.ModelChoiceField(queryset=Alien.objects.all())
    human = forms.ModelChoiceField(queryset=Human.objects.all())


class AliensMakeExperimentForm(forms.Form):
    name = forms.CharField(max_length=255)
    experiment_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    spaceship = forms.ModelChoiceField(queryset=Spaceship.objects.all())
    alien = forms.ModelChoiceField(queryset=Alien.objects.all())
    human = forms.ModelChoiceField(queryset=Human.objects.all())


class AlienMakesTourForm(forms.Form):
    name = forms.CharField(max_length=255)
    tour_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    spaceship = forms.ModelChoiceField(queryset=Spaceship.objects.all())
    alien = forms.ModelChoiceField(queryset=Alien.objects.all())
    human = forms.ModelChoiceField(queryset=Human.objects.all())


class HumanKillsAlienForm(forms.Form):
    kill_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    alien = forms.ModelChoiceField(queryset=Alien.objects.all())
    human = forms.ModelChoiceField(queryset=Human.objects.all())


# QUERIES
class AbductionQueryForm(forms.Form):
    alien = forms.ModelChoiceField(queryset=Alien.objects.all(), label='Alien')
    min_abductions = forms.IntegerField(min_value=1, label='Minimum Abductions')
    date_from = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))


class SpaceshipQueryForm(forms.Form):
    human = forms.ModelChoiceField(queryset=Human.objects.all(), label='Human')
    date_from = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))


class RobbingAlienSearchForm(forms.Form):
    human = forms.ModelChoiceField(queryset=Human.objects.all(), label='Human')
    min_abductions = forms.IntegerField(label='Minimum abduction', min_value=1)
    start_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))


class KilledAlienSearchForm(forms.Form):
    human = forms.ModelChoiceField(queryset=Human.objects.all(), label='Human')
    start_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))


class KillRobbedSearchForm(forms.Form):
    human = forms.ModelChoiceField(queryset=Human.objects.all(), label='Human')


class RobNPeopleSearchForm(forms.Form):
    min_abduction = forms.IntegerField(label='Minimum abduction', min_value=1)
    start_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))


class RobbedNTimesSearchForm(forms.Form):
    min_abduction = forms.IntegerField(label='Minimum abduction', min_value=1)
    start_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))


class CommonExcursionExperimentSearchForm(forms.Form):
    alien = forms.ModelChoiceField(queryset=Alien.objects.all(), label='Alien')
    human = forms.ModelChoiceField(queryset=Human.objects.all(), label='Human')
    start_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))


class NineTaskSearchForm(forms.Form):
    alien = forms.ModelChoiceField(queryset=Alien.objects.all(), label='Alien')
    start_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    min_humans = forms.IntegerField(label='Minimum abduction', min_value=1)


class TenTaskSearchForm(forms.Form):
    human = forms.ModelChoiceField(queryset=Human.objects.all(), label='Human')
    start_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    min_alians = forms.IntegerField(label='Minimum abduction', min_value=1)


class ElevenTaskSearchForm(forms.Form):
    alien = forms.ModelChoiceField(queryset=Alien.objects.all(), label='Alien')
    start_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    min_abduction = forms.IntegerField(label='Minimum abduction', min_value=1)


class TwelveTaskSearchForm(forms.Form):
    alien = forms.ModelChoiceField(queryset=Alien.objects.all(), label='Alien')
    start_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))


