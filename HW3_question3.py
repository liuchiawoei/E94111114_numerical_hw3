import numpy as np
from scipy.interpolate import CubicHermiteSpline

# Given data points

# Time (seconds)
T = np.array([0, 3, 5, 8, 13]) 

# Distance (feet)
D = np.array([0, 200, 375, 620, 990]) 

# Velocity (feet/second)
V = np.array([75, 77, 80, 74, 72]) 

# Hermite interpolation
hermite_poly = CubicHermiteSpline(T, D, V)

# Part (a): Calculate position and velocity at t = 10 seconds
example_time = 10
example_distance = hermite_poly(example_time)

# Compute velocity using the derivative
hermite_velocity = hermite_poly.derivative()
example_velocity = hermite_velocity(example_time)

print("a.")
print(f"Distance at time {example_time} seconds: {example_distance:.2f} feet")
print(f"Velocity at time {example_time} seconds: {example_velocity:.2f} feet/second")

# Part (b): Check if velocity exceeds 55 mi/h (80.685 ft/s)
speed_limit = 55 * 1.467  # Convert mi/h to ft/s

# Generate fine time points to evaluate velocity
time_points = np.linspace(0, 13, 1000)  # High-resolution time range
velocities = hermite_velocity(time_points)  # Compute velocities at these points

# Find when the velocity first exceeds the speed limit
exceed_indices = np.where(velocities > speed_limit)[0]
velocity_exceeds_ever = len(exceed_indices) > 0

print("b.")
if velocity_exceeds_ever:
    first_exceed_time = time_points[exceed_indices[0]]
    print(f"The car first exceeds {speed_limit:.2f} ft/s at time {first_exceed_time:.2f} seconds")
else:
    print("The car never exceeds the speed limit.")

# Part (c): Find the predicted maximum speed
max_velocity = np.max(velocities)

print("c.")
print(f"The predicted maximum speed is {max_velocity:.2f} feet/second")