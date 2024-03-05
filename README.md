
# Drone Simulation Project

This drone simulation project simulates the movement of a drone within a 3D environment based on commands read from a text file. The simulation accounts for the boundaries of the environment and prevents the drone from moving outside these boundaries.


You check basic flow here : https://www.figma.com/file/dkJsGnlyrjbLFAJwgFWYYa/Volodrone-Test?type=whiteboard&node-id=0%3A1&t=3mOEl7TEUgZcaTqE-1

## Features

- **Environment Setup**: Defines a 3D space where the drone can move.
- **Drone Movement**: Processes a series of movement commands from a text file.
- **Boundary Checks**: Ensures the drone does not move outside the predefined space.
- **File Parsing**: Parses input from a structured text file to set up the environment and drone movements.

## Setup

Ensure Python 3.6 or newer is installed on your system. No external libraries are required for the main application, but you will need `pytest` for running tests.

```bash
pip install pytest
```

## File Structure

- `main.py` : Contains the main entry point for the drone simulation and includes the file parsing logic
- `volodrone.py`: Contains the main logic for the drone simulation, including the `Volodrone` class.
- `test_volodrone.py`: Contains pytest unit tests for the drone simulator.
- `commands.txt`: An example input file containing the environment setup and drone commands.

## File Parsing

The simulation reads from a text file with the following format:

```
;WORLD
10 10 10
;DRONE
5 5 5
;COMMAND
01 LEFT 2
02 UP 3
...
```

- **WORLD**: Defines the dimensions of the 3D space (width, depth, height).
- **DRONE**: Sets the starting position of the drone (x, y, z).
- **COMMAND**: Lists the movement commands for the drone. Each command includes an order number, a direction (`LEFT`, `RIGHT`, `UP`, `DOWN`, `FORWARD`, `BACKWARD`), and a distance.

## Drone Movement

The drone responds to commands parsed from the file, moving within the 3D space while avoiding boundary violations. The simulation tracks the drone's position and outputs each movement step.

## Running the Simulation

To run the simulation, execute the following command, replacing `input.txt` with the path to your input file:

```bash
python main.py commands.txt
```

## Testing

Tests are implemented using `pytest`. To run the tests, navigate to the project directory and execute:

```bash
pytest
```

This command will automatically find and run all tests in `test_volodrone.py`, outputting the results.
