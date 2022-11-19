from django.db.models import (Model,
                              CharField,
                              ForeignKey,
                              CASCADE, DO_NOTHING, )

class Curator(Model):
    first_name = CharField(max_length = 20)

    def __str__(self):
        return "курат. "+self.first_name

class Direction(Model):
    name = CharField(max_length=20)
    curator = ForeignKey('Curator',
                       on_delete = CASCADE,
                       related_name = 'direction')
    def __str__(self):
        return "напр. "+self.name
class Group(Model):
    group_name = CharField(max_length=20)
    curator = ForeignKey('Direction',
                         on_delete=CASCADE,
                         related_name='group',
                         )
    def __str__(self):
        return "группа "+self.group_name
class Student(Model):
    surname = CharField(max_length = 10)
    group = ForeignKey('Group',
                       on_delete = DO_NOTHING,
                       related_name = 'student')
    def __str__(self):
        return "Фамилия студента " + self.surname


