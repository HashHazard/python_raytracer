import subprocess
import math
from tqdm import tqdm
from vec import Vector
from ray import Ray
# import turtle

# s = turtle.getscreen()
# t = turtle.Turtle()

def hit_sphere(center, radius, r):
    oc = r.origin - center
    a = r.direction.dot(r.direction)
    b = oc.dot(r.direction)*2.0
    c = oc.dot(oc) - radius*radius
    discriminant = b*b - a*c*4
    if (discriminant < 0):
        return -1.0
    else:
        return (-b - math.sqrt(discriminant)) / (a*2.0)
    return False

def write_color(color):
    return f'{int(255.999*color.x)} {int(255.999*color.y)} {int(255.999*color.z)}\n'

def ray_color(r):
    t = hit_sphere(Vector(0, 0, -1), 0.5, r)
    if(t > 0.0):
        N = r.at(t) - Vector(0 ,0, -1)
        N = N.normalize()
        return Vector(N.x+1,N.y+1,N.z+1,)*0.5
    unit_dir = r.direction.normalize();
    t = 0.5*(unit_dir.y+1.0)
    return Vector(1.0, 1.0, 1.0)*(1.0-t) + Vector(0.5, 0.7, 1.0)*t

# image
ASPECT_RATIO = 16.0/9.0
IMAGE_WIDTH = 512
IMAGE_HEIGHT = int(IMAGE_WIDTH/ASPECT_RATIO)

# camera
viewport_height = 2.0
viewport_width = ASPECT_RATIO * viewport_height
focal_length = 1.0

origin = Vector(0, 0, 0)
horizontal = Vector(viewport_width, 0, 0)
vertical = Vector(0, viewport_height, 0)
lower_left_corner = origin - horizontal*0.5 - vertical*0.5 - Vector(0, 0, focal_length)
# print(lower_left_corner)

# render
with open('../images/img.ppm', 'w') as f:
    f.write(f'P3\n{IMAGE_WIDTH} {IMAGE_HEIGHT}\n255\n')
    for j in tqdm(range(IMAGE_HEIGHT-1, -1, -1)):
        for i in range(0, IMAGE_WIDTH):
            u = i/(IMAGE_WIDTH-1)
            v = j/(IMAGE_HEIGHT-1)
            r = Ray(origin, lower_left_corner + horizontal*u + vertical*v - origin)
            # direction = lower_left_corner + horizontal*u + vertical*v - origin
            # if (i%200 == 0):
            #     t.speed(100000000000)
            #     t.goto(direction.x*50, direction.y*50)
            # b = 0.25
            r_col = ray_color(r)
            f.write(write_color(r_col))
# turtle.done()
cmd = ['eog','../images/img.ppm']
subprocess.call(cmd)
