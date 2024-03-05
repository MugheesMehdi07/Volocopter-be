class Volodrone():
    def __init__(self, world_dimensions, start_position):
        self.world_dimensions = world_dimensions
        self.position = start_position
        self.movements = []
        self.drone_size = 1

    def move_drone(self, command_sequence):
        """
             Move the drone according to the command sequence
            :param command_sequence:
            :return:
        """
        for order, direction, distance in command_sequence:
            vector = self.get_movement_vector(direction, distance)
            new_position = tuple(self.position[i] + vector[i] for i in range(3))
            direction_val = 1 if direction.upper() in ["RIGHT", "UP", "FORWARD"] else -1

            if self.is_valid_position(new_position,direction_val):
                print(new_position)
                self.position = new_position
                self.movements.append((vector, new_position))

    def get_movement_vector(self, direction, distance):
        """
        Get the movement vector based on the direction and distance
        :param direction:
        :param distance: integer value
        :return:
        """

        direction_vectors = {
            "LEFT": (-distance, 0, 0),
            "RIGHT": (distance, 0, 0),
            "UP": (0, distance, 0),
            "DOWN": (0, -distance, 0),
            "FORWARD": (0, 0, distance),
            "BACKWARD": (0, 0, -distance)
        }

        return direction_vectors[direction.upper()]

    def is_valid_position(self, position, direction_val):
        """
        Check if the all the vector position coordinates are valid and under the world dimensions
        :param position:
        :return:
        """

        return all(0 <= position[i]+ (self.drone_size*direction_val) < self.world_dimensions[i]
                   for i in range(3))

    def display_movements(self):
        print("=== Volodrone Initialising")
        print(f"=== Volodrone Sensor Data read.\nWorld: "
              f"(x=range(0, {self.world_dimensions[0]}),"
              f"y=range(0, {self.world_dimensions[1]}),"
              f"z=range(0, {self.world_dimensions[2]}))")

        print(f"Drone starts at: {self.position}")
        print("=== Volodrone Take Off")
        for vector, position in self.movements:
            print(f"{vector}->{position}")
        print("=== Volodrone Landing")


