# Gravity Collision Simulator

A physics-based ball simulation built with Python and Pygame, featuring realistic gravity and collision detection.

## Features

- **Realistic Physics**: Gravity simulation with proper acceleration
- **Collision Detection**: Ball bounces off circular boundaries and window edges
- **Energy Damping**: Energy loss on collisions for realistic behavior
- **Anti-aliased Graphics**: Smooth, high-quality rendering
- **Interactive Controls**: Reset functionality with keyboard input

## Requirements

- Python 3.6+
- Pygame library

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install pygame
   ```

## Usage

Run the simulation:
```bash
python main.py
```

### Controls

- **R key**: Reset the ball to its starting position
- **Close button**: Exit the simulation

## How It Works

The simulation features:

1. **Gravity System**: The ball experiences constant downward acceleration
2. **Collision Physics**: 
   - Ball bounces off the inner edge of the green circular boundary
   - Ball bounces off window edges
   - Energy is lost on each collision (85% energy retention)
3. **Realistic Motion**: Velocity and position are updated each frame based on physics calculations

## Code Structure

- `Ball` class: Handles ball physics, movement, and rendering
  - `apply_physics()`: Updates position and handles collisions
  - `draw()`: Renders the ball with anti-aliasing
- Main game loop: Handles events, updates physics, and renders graphics

## Physics Implementation

The simulation uses:
- **Gravity**: Constant acceleration of 0.2 units/frame²
- **Collision Detection**: Distance calculation between ball center and circle center
- **Reflection**: Vector reflection based on surface normal
- **Damping**: 15% energy loss per collision for realistic bouncing

## Customization

You can modify various parameters in the code:
- `gravity`: Strength of gravitational acceleration
- `bounce_damping`: Energy retention after collisions (0.0 - 1.0)
- Ball size, color, and starting position
- Window size and circle dimensions

## Screenshots

The simulation displays:
- A white ball affected by gravity
- A green circular boundary that the ball bounces off
- Smooth, anti-aliased graphics for better visual quality

## Contributing

Feel free to fork this project and submit improvements! Some ideas for enhancements:
- Multiple balls with ball-to-ball collisions
- Different gravity modes (planetary, zero-g, etc.)
- Particle trails
- Sound effects
- GUI controls for real-time parameter adjustment

## License

This project is open source and available under the MIT License.
