# Motivation

Pyg stands for Python Ultimate Realtime Game Engine. Its purpose is rapid 2d game development that requires least coding possible. Pyg comes with a drawing and a physical engine, along with tools for networking, sprite management and sound playback. The project is in an early development phase, so all you just read is a lie.

It partly draws inspiration from the renowned and versatile `pygame` module. Unlike pygame, Pyg uses OpenGL 3.0 for all drawing. Using 3d sprites is encouraged, but all game mechanics are two-dimensional. Scripts using Pyg do not manage the game loop by themselves, which not only provides a huge performance boost, but also makes the code shorter and clearer. Pyg is top-class in brevity, at least if considering the module's name.

# Approach

We employ a test-driven development model, thus writing games first and only then coding a library to drive them. Most of the tests are playable and are located in the `examples` directory.