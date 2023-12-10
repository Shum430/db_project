from django.db import models


class Alien(models.Model):
    alien_name = models.CharField(max_length=100)

    def __str__(self):
        return self.alien_name


class Human(models.Model):
    human_name = models.CharField(max_length=100)

    def __str__(self):
        return self.human_name


class Spaceship(models.Model):
    spaceship_name = models.CharField(max_length=100)

    def __str__(self):
        return self.spaceship_name


class Abduction(models.Model):
    abduction_date = models.DateField()
    spaceship = models.ForeignKey(Spaceship, on_delete=models.CASCADE)
    alien = models.ForeignKey(Alien, on_delete=models.CASCADE)
    human = models.ForeignKey(Human, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.abduction_date} - {self.spaceship} - {self.alien} - {self.human}"


class Escape(models.Model):
    abduction_date = models.DateField()
    spaceship = models.ForeignKey(Spaceship, on_delete=models.CASCADE)
    alien = models.ForeignKey(Alien, on_delete=models.CASCADE)
    human = models.ForeignKey(Human, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.abduction_date} - {self.spaceship} - {self.alien} - {self.human}"


class Transportation(models.Model):
    transportation_date = models.DateField()
    spaceship_from = models.ForeignKey(Spaceship, on_delete=models.CASCADE, related_name='transports_from')
    spaceship_to = models.ForeignKey(Spaceship, on_delete=models.CASCADE, related_name='transports_to')
    alien = models.ForeignKey(Alien, on_delete=models.CASCADE)
    human = models.ForeignKey(Human, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.transportation_date} - {self.spaceship_from} to {self.spaceship_to} - {self.alien} - {self.human}"


class Experiment(models.Model):
    name = models.CharField(max_length=100)
    experiment_date = models.DateField()
    spaceship = models.ForeignKey(Spaceship, on_delete=models.CASCADE)
    alien = models.ForeignKey(Alien, on_delete=models.CASCADE)
    human = models.ForeignKey(Human, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.experiment_date} - {self.spaceship} - {self.alien} - {self.human}"


class Tour(models.Model):
    name = models.CharField(max_length=100, default="tour")
    tour_date = models.DateField()
    spaceship = models.ForeignKey(Spaceship, on_delete=models.CASCADE)
    alien = models.ForeignKey(Alien, on_delete=models.CASCADE)
    human = models.ForeignKey(Human, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tour_date} - {self.spaceship} - {self.alien}"

class LinkingTour(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    human = models.ForeignKey(Human, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tour} - {self.human}"


class AlienKill(models.Model):
    kill_date = models.DateField()
    alien = models.ForeignKey(Alien, on_delete=models.CASCADE)
    human = models.ForeignKey(Human, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.kill_date} - {self.alien} - {self.human}"
