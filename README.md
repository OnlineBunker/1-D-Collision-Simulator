# 1-D Collision Simulator

A real-time 1D elastic collision simulator that models object collisions based on mass and velocity inputs, following conservation laws.

## 🌐 Live Demo

Check it out here: [https://onlinebunker.github.io/1-D-Collision-Simulator/](https://onlinebunker.github.io/1-D-Collision-Simulator/)

## 🚀 Tech Stack

* Python
* Pygame
* Pygbag (for web deployment)

## 📦 Features

Real-time physics simulation with accurate collision modeling. Customizable mass and velocity inputs in desktop version. Smooth animation with wall bounce and elastic collisions.

## 💡 Description

This simulator demonstrates the behavior of two objects colliding in one dimension, governed by the principles of conservation of momentum and kinetic energy. Users can modify masses and velocities to observe different outcomes.

## 🖥️ Running the Project Locally

Make sure you have Python and Pygame installed.

```bash
pip install pygame
python main.py
```

This version allows **custom values** to be entered for masses and velocities of the objects.

## 🌐 Web Version Notice

The [live web version](https://onlinebunker.github.io/1-D-Collision-Simulator/) is powered by **Pygbag**, which compiles Python to WebAssembly. Due to limitations in browser input support for compiled Pygame applications, only **predefined values** are used for masses and velocities in the web version.

## 📁 File Structure

```
├── docs/                 # For GitHub Pages deployment
│   └── index.html        # Pygbag-generated HTML build
├── main.py               # Main simulation script
├── README.md             # Project overview
```

## 📸 Screenshots
<img width="797" alt="Screenshot 2025-04-01 at 7 18 21 AM" src="https://github.com/user-attachments/assets/94ad15a1-e227-4448-bd80-deca58a37ff5" />
