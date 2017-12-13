class FireAlarm(object):
    def __init__(self):
        self.observers = []

    def reg(self, observer):
        self.observers.append(observer)

    def unreg(self, observer):
        self.observers.append(observer)

    def notify_all(self, reason):
        for observer in self.observers:
            observer.alarm(reason)


class Office(object):
    def __init__(self, name=''):
        self.name = name

    def alarm(self, reason):
        print('I am {name} and was notified about {reason}'.format(
            name=self.name, reason=reason)
        )


class OfficeSecurity(object):
    def alarm(self, reason):
        print('Notified about {reason}. Evacuating everyone!'.format(
            reason=reason)
        )


if __name__ == "__main__":
    fire_alarm = FireAlarm()

    fire_alarm.reg(Office('Office_1'))
    fire_alarm.reg(Office('Office_2'))
    fire_alarm.reg(OfficeSecurity())

    fire_alarm.notify_all(reason='Fire')
