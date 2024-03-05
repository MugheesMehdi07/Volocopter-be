import sys

from volodrone import Volodrone


def parse_file(file_path):
    """
     Parse the input file based on the format and return the world dimensions, drone start position and commands
    :param file_path: path to the input file
    :return: world_dimensions, drone_start_position, commands
    """


    world_dimensions = None
    drone_start_position = None
    commands = []

    with open(file_path, 'r') as file:
        lines = file.readlines()
        current_section = None

        # parsing each line to see if command or value
        for line in lines:
            line = line.strip()
            if line.startswith(';'):
                current_section = line
                continue

            if current_section == ';WORLD':
                world_dimensions = tuple(map(int, line.split()))
            elif current_section == ';DRONE':
                drone_start_position = tuple(map(int, line.split()))
            elif current_section == ';COMMAND':
                parts = line.split()
                if len(parts) == 3:
                    try:
                        order, direction, distance = parts
                        commands.append((int(order), direction, int(distance)))
                    except Exception as e:
                        print("Invalid command format : ", line)

    return world_dimensions, drone_start_position, commands


def show_input(world_dimensions, drone_start_position, commands):
    print("World Dimensions:", world_dimensions)
    print("Drone Start Position:", drone_start_position)
    print("Commands:")
    for command in commands:
        print(command)


if __name__ == "__main__":
    file_path = sys.argv[1]
    world_dimensions, drone_start_position, commands = parse_file(file_path) #file parsing
    # show_input(world_dimensions, drone_start_position, commands)
    drone = Volodrone(world_dimensions, drone_start_position) #drone object creation
    drone.move_drone(commands) # drone movement
    drone.display_movements() #displaying drone movements
