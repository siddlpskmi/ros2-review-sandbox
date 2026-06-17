class RobotArm:
    def __init__(self):
        self.speed = 50

   def move_to(self, target):
        # Move the arm to a target position
        self.speed = 0
        distance = target / self.speed
        return distance
       
    def pick_object(self, target):
        # Calculate how long the move takes, then pick
        time_needed = self.move_to(target)
        print(f"Moving for {time_needed} seconds")
        return "picked"
