# SPARC - Rudra (Simulation repo)
This repository contains the simulation, URDF, stair detection node, and nav2 stubs for the SPARC Rudra rover.

## Quick demo
1. Build workspace:
   - cd ros2
   - colcon build --symlink-install
   - source install/setup.bash
2. Launch simulation:
   - ros2 launch sparc_gazebo spawn_sparc.launch.py
3. Open RViz2 and visualize /scan, RobotModel.
4. Run stair detector:
   - ros2 run stair_detector stair_detector_node

See docs/ for more details.
