#!/usr/bin/env bash
set -e
# quick demo script for reviewers
cd "$(dirname "$0")/../ros2"
source install/setup.bash || true
# build if not built
colcon build --symlink-install || true
source install/setup.bash
# launch gazebo + spawn
ros2 launch rudra_gazebo spawn_sparc.launch.py
