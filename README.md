# HAB2_ROS2

This repository contains a skeleton ROS 2 layout for a high altitude balloon
(HAB) project.  It is inspired by the original `HAB-GoatSee` code base and
breaks each sensor interface into its own node.  The current implementation is
lightweight and intended as a starting point for future development.

## Repository Structure

```
README.md               - Project overview and ROS 2 design
src/
  hab_main_node.py      - Central node subscribing to all sensor topics
  bmp280_node.py        - Publishes data from a BMP280 pressure/temperature sensor
  bosch_pressure_node.py- Publishes data from a Bosch pressure sensor
  mcp9600_node.py       - Publishes data from an MCP9600 thermocouple sensor
  gps_node.py           - Publishes GPS fixes
  status_node.py        - Aggregates data from other sensors
  clear_i2c.py          - Utility script that clears the I2C bus
launch/
  hab_launch.py         - Example launch file that starts all nodes
```

## ROS 2 Implementation Outline

1. **Sensor Nodes** – Each sensor (BMP280, Bosch pressure, MCP9600, GPS) runs in
   its own node and publishes a simple `std_msgs/String` message.  Real
   implementations would use custom message types containing the sensor data.
2. **`hab_main_node`** – Subscribes to all sensor topics and acts as the main
   orchestrator.  This node would be responsible for logging data, performing
   any higher-level decision making, or relaying data via radio.
3. **`status_node`** – Collects readings from the BMP280, Bosch pressure, and
   MCP9600 nodes and periodically reports a summary.
4. **I2C Recovery** – Sensor nodes directly call the helper function
   `clear_i2c.clear_bus()` if they encounter an I²C error.
5. **Launch File** – `launch/hab_launch.py` demonstrates how to start all nodes
   from one launch description.  It calls `clear_i2c.py` once at startup and
   then launches every node.

This repository currently provides stub implementations only.  Sensor drivers
from the original `HAB-GoatSee` project would need to be integrated where the
placeholder comments appear.
