import requests
from coord_field import CoordField
from haversine import haversine, Unit, inverse_haversine, Direction
import math
from hkb_diamondsquare import DiamondSquare as DS




# # url = "https://ava-iimm3tykgq-uc.a.run.app/coordinate?h=1&r=1&s=.1&longitudeCoord=37&latitudeCoord=82"
# url_test = "http://127.0.0.1:5000/testAPI?h=1&r=1&s=.1&longitudeCoord=37&latitudeCoord=82"

# payload={}
# headers = {
#   'x-api-key': 'Av@Ap1K3y'
# }

# response = requests.request("GET", url_test, headers=headers, data=payload)
# print(len(response.text))
# print(response.text)
# cf = CoordField(15,-15,3,1)
# cf.fillField()
# # print(cf.xList)
# # print(cf.yList)
 
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# # Generate some random data
# x = np.random.normal(size=100)
# y = np.random.normal(size=100)
# z = np.random.normal(size=100)
# c = np.random.randint(0, 4, size=100)

# # Create a figure and a 3D axis
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Create the scatter plot
# scatter = ax.scatter(x, y, z, c=c, cmap='viridis')

# # Add a color bar to the plot
# cbar = plt.colorbar(scatter)

# # Set the labels and title
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')
# plt.title('3D Scatter Plot with Color-Coded Regions')

# # Show the plot
# plt.show()import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

# Generate the data for the heatmap
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the heatmap surface
surf = ax.plot_surface(X, Y, Z, cmap='coolwarm', linewidth=0)

# Add a colorbar
fig.colorbar(surf)

# Set the axis labels and limits
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-1, 1)

# Show the plot
plt.show()
