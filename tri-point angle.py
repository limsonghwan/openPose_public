import numpy as np
points = np.array([[343.8998, 168.1526], [351.2377, 173.7503], [353.531, 182.72]])

A = points[2] - points[0]
B = points[1] - points[0]
C = points[2] - points[1]

angles = []
for e1, e2 in ((A, B), (A, C), (B, -C)):
    num = np.dot(e1, e2)
    denom = np.linalg.norm(e1) * np.linalg.norm(e2)
    angles.append(np.arccos(num/denom) * 180 / np.pi)
print (angles)
print (sum(angles))
