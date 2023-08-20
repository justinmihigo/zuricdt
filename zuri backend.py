# class defintion
class Research:
    def __init__(self, speed, realtime):
        self.speed = speed
        self.realtime = realtime
        self.is_impen = False
# creating function that will calculate the expected time and #timeduratio if exceeds 60
    def rock_detect(self, point_a, point_b):
        self.location_a = point_a[0] + point_b[0]
        self.location_b = point_a[1] + point_b[1]
        self.distance = self.location_a - self.location_b
        self.exp_time = self.distance / self.speed
        is_impen=self.realtime - self.exp_time>60
        return is_impen

# starting main excecution with the lists of point a and b
point_a = [53.5872,-2.4138]
point_b = [53.474,-2.2388]
research = Research(45, 78)
exp_time = research.rock_detect(point_a, point_b)
if exp_time:
    print("There is obstruction and is Impenetratable")
else:
    print("There is obstruction but is penetratable")