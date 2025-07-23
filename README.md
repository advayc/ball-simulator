# Ball Simulator - Interactive Physics Demo

 **[▶️ Play Live Demo](https://advayc.github.io/ball-simulator/)** 

A mesmerizing physics-based ball simulation with dynamic visual styles including rainbow colors, neon pulse effects, particle trails, and classic rendering.

## Features

- **Multiple Animation Styles**:
  - **Rainbow**: Continuously cycling rainbow color effect
  - **Neon Pulse**: Dynamic pulsing glow with rainbow colors
  - **Particle Trail**: Leaves colorful particles and trails on movement and collision
  - **Classic**: Simple solid white ball for minimalist visuals
- **Real-time Physics**: Gravity simulation with realistic collision detection
- **Smart Collisions**: Ball bounces off circular boundaries and window edges
- **Progressive Growth**: Ball grows with each collision until reset
- **Continuous Demo**: Auto-resets for endless entertainment
- **Web-Optimized**: Runs directly in browser via WebAssembly
- **Cross-Platform**: Works on desktop and mobile browsers with touch support

### Play Online (Recommended)
Just visit: **https://advayc.github.io/ball-simulator/**

### Run Locally
```bash
python main.py
```

### Deploy to Web
To deploy your simulator to the web, you'll need Pygbag:

```bash
# Install Pygbag
pip install pygbag

# Build and run locally
pygbag --port 8000 main.py

# Build for deployment
pygbag --build --ume_block 0 main.py
```

After building, upload the `build/web` directory to your web server or GitHub Pages.

### Controls

- **Style Buttons**: Click to change animation style
- **Touch/Click**: Works on mobile and desktop
- **Close button**: Exit the simulation

## How It Works

The simulation features:

1. **Animation Styles System**: Choose between different visual effects
2. **Gravity System**: The ball experiences constant downward acceleration
3. **Collision Physics**: 
   - Ball bounces off the inner edge of the green circular boundary
   - Ball bounces off window edges
   - Collision detection triggers style-specific visual effects
4. **Particle System**: Creates dynamic particles on collision
5. **Trail System**: Leaves a colorful trail behind the ball
6. **Responsive UI**: Works on desktop and mobile with touch support

## Code Structure

- `Ball` class: Handles ball physics, movement, and rendering
  - `apply_physics()`: Updates position and handles collisions
  - `update_color()`: Manages dynamic coloring based on style
  - `draw()`: Renders the ball with current style effects
  - `add_collision_particles()`: Creates particles on collision
- Style system: Dictionary-based configuration for visual effects
- Touch-friendly UI: Works across devices with proper event handling
- Web-compatible: Designed to run in browsers via Pygbag/WebAssembly

## Implementation Details

### Physics System
- **Gravity**: Constant acceleration applied each frame
- **Collision Detection**: Distance calculation for circular boundary and edge detection
- **Reflection**: Vector reflection based on surface normal
- **Growth**: Ball grows on collision until maximum size

### Visual Effects System
- **Rainbow Color**: HSV color space for smooth transitions
- **Pulse Effect**: Sinusoidal size variation
- **Trail System**: Position and color history with fade effect
- **Particle System**: Physics-based particles with lifetime

### Web Compatibility
- **Asyncio Integration**: Web-friendly event loop with proper timing
- **Responsive Design**: Handles window resizing events
- **Touch Support**: Works with mouse and touch input
- **WebAssembly**: Compiles to web-compatible format via Pygbag

## Customization

You can modify various parameters in the code:
- **Animation Styles**: Edit the `STYLES` dictionary to create new effects
- **Physics Parameters**: Adjust gravity, velocity, and collision response
- **UI Elements**: Modify button placement and appearance
- **Visual Effects**: Customize particles, trails, and color transitions

## Screenshots

The simulation displays:
- A white ball affected by gravity
- A green circular boundary that the ball bounces off
- Smooth, anti-aliased graphics for better visual quality

## Contributing

Feel free to fork this project and submit improvements! Some ideas for enhancements:
- Additional animation styles with new visual effects
- Multiple balls with ball-to-ball collisions
- Different gravity modes (planetary, zero-g, etc.)
- More UI controls for adjusting physics parameters
- High score tracking for longest time before reset

## Web Deployment Troubleshooting

If you encounter issues with web deployment:

1. **Blank Screen**: Check browser console for errors, ensure all resources are loading
2. **Performance Issues**: Reduce particle count or animation complexity
3. **Touch Not Working**: Ensure FINGERDOWN events are being processed
4. **Size Problems**: Test with different viewport sizes and orientations
5. **Loading Errors**: Check that all Python imports are web-compatible

## License

This project is open source and available under the MIT License.
