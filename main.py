import math

# Define a list of points in 2D space
points = [(0, 0), (3, 4), (5, 12), (8, 15)]

# Define a function to calculate Euclidean distance between two points
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# List to store the distances between each pair of points
distances = []

# Calculate distances between each pair of points and store in 'distances'
for i in range(len(points)):
    for j in range(i + 1, len(points)):  # Avoid duplicate pairs
        distances.append(euclideanDistance(points[i], points[j]))

# Find the minimum distance
min_distance = min(distances)

# Display the results
distances, min_distance
