import pytest
from volodrone import Volodrone

def test_drone_movement_within_boundaries():
    world = (10, 10, 10)
    start_position = (5, 5, 5)
    drone1 = Volodrone(world, start_position)
    drone2 = Volodrone(world, start_position)
    drone3 = Volodrone(world, start_position)
    commands_1 = [
        (1, "FORWARD", 2),
        (2, "UP", 2)
    ]
    commands_2 = [
        (1, "Backward", 2),
        (2, "Down", 2)
    ]
    commands_3 = [
        (1, "left", 2),
        (2, "right", 3)
    ]
    drone1.move_drone(commands_1)
    assert drone1.position == (5, 7, 7), "Drone should move within boundaries correctly."
    drone2.move_drone(commands_2)
    assert drone2.position == (5, 3, 3), "Drone should move within boundaries correctly."
    drone3.move_drone(commands_3)
    assert drone3.position == (6, 5, 5), "Drone should move within boundaries correctly."


def test_drone_prevents_movement_outside_boundaries():
    world = (10, 10, 10)
    start_position = (0, 0, 0)
    drone1 = Volodrone(world, start_position)
    commands1 = [
        (1, "LEFT", 1),
    ]
    drone1.move_drone(commands1)
    assert drone1.position == (0, 0, 0), "Drone should not have moved outside boundaries."

    drone1 = Volodrone(world, start_position)
    commands2 = [
        (1, "UP", 11),
    ]
    drone1.move_drone(commands2)
    assert drone1.position == (0, 0, 0), "Drone should not have moved outside boundaries."



def test_drone_movement_vector():
    world = (10, 10, 10)
    start_position = (5, 5, 5)
    drone = Volodrone(world, start_position)
    vector_up = drone.get_movement_vector("UP", 3)
    vector_down = drone.get_movement_vector("DOWN", 3)
    vector_left = drone.get_movement_vector("LEFT", 3)
    vector_right = drone.get_movement_vector("RIGHT", 3)
    vector_for = drone.get_movement_vector("FORWARD", 3)
    vector_back = drone.get_movement_vector("BACKWARD", 3)
    assert vector_up == (0, 3, 0), "Movement vector for 'UP' with distance 3 should be (0, 3, 0)."
    assert vector_down == (0, -3, 0), "Movement vector for 'DOWN' with distance 3 should be (0, -3, 0)."
    assert vector_left == (-3, 0, 0), "Movement vector for 'LEFT' with distance 3 should be (-3, 0, 0)."
    assert vector_right == (3, 0, 0), "Movement vector for 'RIGHT' with distance 3 should be (3, 0, 0)."
    assert vector_for == (0, 0, 3), "Movement vector for 'FORWARD' with distance 3 should be (0, 0, 3)."
    assert vector_back == (0, 0, -3), "Movement vector for 'BACKWARDS' with distance 3 should be (0, 0, -3)."



def test_drone_size_limitation_at_edge():
    world = (10, 10, 10)
    start_position = (8, 8, 8)
    drone = Volodrone(world, start_position)
    drone.move_drone([(1, "RIGHT", 2)])  # Considering, this should not move
    assert drone.position == (8, 8, 8), "Drone should consider its size when moving near the edge."


if __name__ == "__main__":
    pytest.main()
