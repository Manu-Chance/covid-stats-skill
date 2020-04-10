from mycroft import MycroftSkill, intent_file_handler


class CovidStats(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('stats.covid.intent')
    def handle_stats_covid(self, message):
        self.speak_dialog('stats.covid')


def create_skill():
    return CovidStats()

