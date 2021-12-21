from tortoise import Tortoise, fields, run_async
from tortoise.expressions import F
from tortoise.functions import Count, Sum
from tortoise.models import Model
from tortoise.query_utils import Prefetch


class Tournament(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()

    events: fields.ReverseRelation["Event"]

    def __str__(self):
        return self.name


class Event(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    tournament: fields.ForeignKeyRelation[Tournament] = fields.ForeignKeyField(
        "models.Tournament", related_name="events"
    )
    participants: fields.ManyToManyRelation["Team"] = fields.ManyToManyField(
        "models.Team", related_name="events", through="event_team"
    )
    n = fields.IntField()

    def __str__(self):
        return self.name


class Team(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    count = fields.IntField()

    events: fields.ManyToManyRelation[Event]

    def __str__(self):
        return self.name


async def run():
    await Tortoise.init(db_url="sqlite://:memory:", modules={"models": ["__main__"]})
    await Tortoise.generate_schemas()

    tournament = await Tournament.create(name="tournament")
    team = await Team.create(name='gomno', count=10)
    event = await Event.create(name="First", tournament=tournament, n=10)
    await Event.create(name="Second", tournament=tournament, n=30)
    await event.participants.add(team)
    tournament_with_filtered = (
        await Tournament.all()
        .prefetch_related(Prefetch("events", queryset=Event.filter(name="First")))
        .first()
    )
    print(tournament_with_filtered)
    print(await Tournament.first().prefetch_related("events"))

    tournament_with_filtered_to_attr = (
        await Tournament.all()
        .prefetch_related(
            Prefetch(
                "events", queryset=Event.filter(name="Second")
            ),
        )
        .annotate(f_c=Sum('events__n'))
        .first()
    )
    print(tournament_with_filtered_to_attr.f_c)


if __name__ == "__main__":
    run_async(run())