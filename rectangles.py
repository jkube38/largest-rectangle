
'''Creates a list of tuples (w, h) and sorts them by enclosed area'''
__author__ = 'Jordan Kubista'

# Generates the tuple list
rectangles = [(width, height) for width in range(2, 10)
              for height in range(width, 10)]

# Sorts the tuple list by enclosed area
sorted_rectangles = sorted(rectangles, key=lambda x: (x[0]-1) * (x[1]-1),
                           reverse=True)

print(sorted_rectangles)
