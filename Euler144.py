import numpy as np

starting_pt = np.array([1.4,-9.6],dtype=np.float64)
starting_vel = np.array([1.4,-9.6 - 10.1],dtype=np.float64)

def get_next_vel(pt,vel):
    m = -4*pt[0] / pt[1]
    vel[1] = -vel[1]
    theta = np.arctan(m)
    rotation = np.array([[np.cos(2*theta),-np.sin(2*theta)],
                        [np.sin(2*theta),np.cos(2*theta)]]
                        )
    return rotation.dot(vel)

def get_next_pt(pt,vel):
    t = (-2 * vel[1]*pt[1] - 8*vel[0]*pt[0])/ (4*vel[0]**2 + vel[1]**2)
    return pt[0] + t*vel[0], pt[1] + t*vel[1]

count = 1

this_pt = starting_pt
this_vel = starting_vel

while 1:
    next_vel = get_next_vel(this_pt,this_vel)
    next_pt = get_next_pt(this_pt,next_vel)
    print('Have hit {c} times, upcoming pt is {next_pt}'.format(c = count,next_pt= next_pt))
    if next_pt[0] <= .01 and next_pt[0] >= -.01 and next_pt[1] > 0:
        break
    count+=1
    this_pt = next_pt
    this_vel = next_vel

print(count)
