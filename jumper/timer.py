import time

class Timer:
    def __init__(self):
        self.reset()

    def reset(self):
        self.last_time = 0
        self.total_time = 0
        self.is_started = False
        self.is_paused = False

    def start(self):
        if not self.is_started:
            self.reset()
            self.last_time = int(round(time.time()))
            self.is_started = True

    def restart(self):
        self.reset()
        self.start()

    def stop(self):
        self.is_started = False
        self.is_paused = False

    def pause(self):
        self.is_paused = True

    def resume(self):
        self.last_time = int(round(time.time()))
        self.is_paused = False

    def update(self):
        if self.is_started and not self.is_paused:
            current_time = int(round(time.time()))
            self.total_time += current_time - self.last_time
            self.last_time = current_time

    def get_time(self):
        return self.total_time

    def get_time_string(self):
        return self.parse_time(self.total_time)

def parse_time(second):
    m = int(second / 60)
    s = second % 60

    return "%02d:%02d" % (m, s)

