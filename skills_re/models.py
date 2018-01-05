from django.db import models
from resume.basemodel import AbstractDateModel
from profile_re.models import Profile


class Skill(AbstractDateModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


level_1 = '1'
level_2 = '2'
level_3 = '3'
level_4 = '4'
level_5 = '5'
level_6 = '6'
level_7 = '7'
level_8 = '8'
level_9 = '9'
level_10 = '10'

levels = (
    (level_1, 'level_1'),
    (level_2, 'level_2'),
    (level_3, 'level_3'),
    (level_4, 'level_4'),
    (level_5, 'level_5'),
    (level_6, 'level_6'),
    (level_7, 'level_7'),
    (level_8, 'level_8'),
    (level_9, 'level_9'),
    (level_10, 'level_10'),
)


class SkillLevel(AbstractDateModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.CharField(choices=levels, max_length=255, blank=True, null=True)

    def __str__(self):
        return '{} {} {}'.format(self.user, self.skill, self.level)


class LanguageLevel(AbstractDateModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Language(AbstractDateModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class UserLanguageLevel(AbstractDateModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    level = models.ForeignKey(LanguageLevel, on_delete=models.CASCADE)
