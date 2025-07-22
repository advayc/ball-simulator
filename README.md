# Ball Simulator - Interactive Physics Demo

 **[▶️ Play Live Demo](https://advayc.github.io/ball-simulator/)** 

A mesmerizing physics-based ball simulation with dynamic rainbow colors and synchronized audio segments that play on collision.

##  Features

- **Dynamic Rainbow Colors**: Continuously cycling rainbow effect
- ** Audio Synchronization**: Plays sequential 0.2s segments of UNITY song on each collision  
- ** Real-time Physics**: Gravity simulation with realistic collision detection
- ** Smart Collisions**: Ball bounces off circular boundaries and window edges
- ** Progressive Growth**: Ball grows with each collision until reset
- ** Continuous Demo**: Auto-resets for endless entertainment
- ** Web-Optimized**: Runs directly in browser via WebAssembly
- ** Cross-Platform**: Works on desktop and mobile browsers

### Play Online (Recommended)
Just visit: **https://advayc.github.io/ball-simulator/**

### Run Locally
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
