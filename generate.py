import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5

pyrosim.Start_SDF("boxes.sdf")

# pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])

for i in range(1, 11):
    length *= 0.9
    width *= 0.9
    height *= 0.9
    for j in range(1, 5):
        for k in range(1, 5):
            pyrosim.Send_Cube(name="Box", pos=[x + j, y + k, z + i], size=[length, width, height])

pyrosim.End()
