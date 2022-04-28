#!/bin/bash

if [ "$#" -ne 5 ]; then
	echo "Error: There should be 5 parameters."
	exit -1;
fi;
rostopic pub /modelo/arm_controller/command \
trajectory_msgs/JointTrajectory \
"[$1, $2, $3, $4, $5]" \
"[0.0, 0.0, 0.0, 0.0, 0.0]" \
"[0.0, 0.0, 0.0, 0.0, 0.0]" \
"[0.0, 0.0, 0.0, 0.0, 0.0]" \
"[0, 0]" "-1"
