# import numpy as np

# def CreateCircle(center, radius, colour, points = 10, offset = 0, semi = False):
#     vertices = [center[0], center[1], center[2], colour[0], colour[1], colour[2]]
#     indices = []

#     if semi == True:
#         for i in range(points+1):
#             vertices += [
#                 center[0] + radius * np.cos(float(i * np.pi)/points),
#                 center[1] + radius * np.sin(float(i * np.pi)/points),
#                 center[2],
#                 colour[0],
#                 colour[1],
#                 colour[2],
#                 ]
            
#             ind1 = i+1
#             ind2 = i+2 if i != points else 1
#             indices += [0 + offset, ind1 + offset, ind2 + offset]
#     else:
#         for i in range(points):
#             vertices += [
#                 center[0] + radius * np.cos(float(i * 2* np.pi)/points),
#                 center[1] + radius * np.sin(float(i * 2* np.pi)/points),
#                 center[2],
#                 colour[0],
#                 colour[1],
#                 colour[2],
#                 ]
            
#             ind1 = i+1
#             ind2 = i+2 if i != points-1 else 1
#             indices += [0 + offset, ind1 + offset, ind2 + offset]

#     return (vertices, indices)    


# def CreatePlayer():

#     vertices, indices = CreateCircle([0.0, 0.0, 0.0], 1.0, [220/255, 183/255, 139/255], 50, 0)

#     eye_verts1, eye_inds1 = CreateCircle([0.4, -0.5, 0.05], 0.3, [1,1,1], 20, len(vertices)/6)
#     vertices += eye_verts1
#     indices += eye_inds1

#     eye_verts2, eye_inds2 = CreateCircle([-0.4, -0.5, 0.05], 0.3, [1,1,1], 20, len(vertices)/6)
#     vertices += eye_verts2
#     indices += eye_inds2

#     eye_verts3, eye_inds3 = CreateCircle([-0.4, -0.5, 0.10], 0.12, [0,0,0], 10, len(vertices)/6)
#     vertices += eye_verts3
#     indices += eye_inds3

#     eye_verts4, eye_inds4 = CreateCircle([0.4, -0.5, 0.10], 0.12, [0,0,0], 10, len(vertices)/6)
#     vertices += eye_verts4
#     indices += eye_inds4

#     eye_verts5, eye_inds5 = CreateCircle([0.0, 0.0, 0.2], 1.0, [1,0,0], 25, len(vertices)/6, True)
#     vertices += eye_verts5
#     indices += eye_inds5

#     eye_verts6, eye_inds6 = CreateCircle([0.0, 0.95, 0.3], 0.3, [0.9,0.9,0.9], 20, len(vertices)/6)
#     vertices += eye_verts6
#     indices += eye_inds6

#     return vertices, indices

# def CreateBackground():
#     grassColour = [0,1,0]
#     waterColour = [0,0,1]

#     vertices = [
#         -500.0, 500.0, -0.9, grassColour[0], grassColour[1], grassColour[2],
#         -400.0, 500.0, -0.9, grassColour[0], grassColour[1], grassColour[2],
#         -400.0, -500.0, -0.9, grassColour[0], grassColour[1], grassColour[2],
#         -500.0, -500.0, -0.9, grassColour[0], grassColour[1], grassColour[2],

#         500.0, 500.0, -0.9, grassColour[0], grassColour[1], grassColour[2],
#         400.0, 500.0, -0.9, grassColour[0], grassColour[1], grassColour[2],
#         400.0, -500.0, -0.9, grassColour[0], grassColour[1], grassColour[2],
#         500.0, -500.0, -0.9, grassColour[0], grassColour[1], grassColour[2],

#         -400.0, 500.0, -0.9, waterColour[0], waterColour[1], waterColour[2],
#         400.0, 500.0, -0.9, waterColour[0], waterColour[1], waterColour[2],
#         400.0, -500.0, -0.9, waterColour[0], waterColour[1], waterColour[2],
#         -400.0, -500.0, -0.9, waterColour[0], waterColour[1], waterColour[2],
#     ]

#     indices = [
#         0,1,2, 0,3,2,
#         8,9,10, 8,11,10,
#         4,5,6, 4,7,6
#     ]

#     return vertices, indices

# playerVerts, playerInds = CreatePlayer()
# playerProps = {
#     'vertices' : np.array(playerVerts, dtype = np.float32),
    
#     'indices' : np.array(playerInds, dtype = np.uint32),

#     'position' : np.array([0, 0, 0], dtype = np.float32),

#     'rotation_z' : 0.0,

#     'scale' : np.array([30, 30, 1], dtype = np.float32),

#     'sens' : 125,

#     'velocity' : np.array([0, 0, 0], dtype = np.float32)
# }

# backgroundVerts, backgroundInds = CreateBackground()
# backgroundProps = {
#     'vertices' : np.array(backgroundVerts, dtype = np.float32),
    
#     'indices' : np.array(backgroundInds, dtype = np.uint32),

#     'position' : np.array([0, 0, 0], dtype = np.float32),

#     'rotation_z' : 0.0,

#     'scale' : np.array([1, 1, 1], dtype = np.float32),

#     'boundary' : [500.0, -500.0, 500.0, 500.0],

#     'river_banks': [-400.0, 400.0]
# }

# homepageVerts = [
#     -500.0, 500.0, 0.0, 0.57, 0.90, 0.96,
#     500.0, 500.0, 0.0, 0.57, 0.90, 0.96, 
#     500.0, -500.0, 0.0, 0.57, 0.90, 0.96,
#     -500.0, -500.0, 0.0, 0.57, 0.90, 0.96
# ]

# homepageInds = [
#     0, 1, 2,
#     0, 2, 3 
# ]

# homepageProps = {
#     'vertices': np.array(homepageVerts, dtype=np.float32),
#     'indices': np.array(homepageInds, dtype=np.uint32),
#     'position': np.array([0, 0, 0], dtype=np.float32),
#     'rotation_z': 0.0,
#     'scale': np.array([1, 1, 1], dtype=np.float32)
# }


# newGameButtonVerts = [
#     -100.0, 25.0, 0.1,
#     100.0, 25.0, 0.1,
#     100.0, -25.0, 0.1,
#     -100.0, -25.0, 0.1,
# ]


# newGameButtonInds = [
#     0, 1, 2,
#     0, 2, 3
# ]

# newGameButton_min_x = min(newGameButtonVerts[0::6]) 
# newGameButton_max_x = max(newGameButtonVerts[0::6]) 
# newGameButton_min_y = min(newGameButtonVerts[1::6]) 
# newGameButton_max_y = max(newGameButtonVerts[1::6]) 

# newGameButton_width = newGameButton_max_x - newGameButton_min_x 
# newGameButton_height = newGameButton_max_y - newGameButton_min_y  

# newGameButtonProps = {
#     'vertices': np.array(newGameButtonVerts, dtype=np.float32),
#     'indices': np.array(newGameButtonInds, dtype=np.uint32),
#     'position': np.array([0, 120, 0.1], dtype=np.float32),
#     'rotation_z': 0.0,
#     'scale': np.array([1, 1, 1], dtype=np.float32),
#     'size': np.array([newGameButton_width, newGameButton_height], dtype=np.float32),
# }

# loadGameButtonVerts = [
#     -100.0, 25.0, 0.1, 
#     100.0, 25.0, 0.1,
#     100.0, -25.0, 0.1, 
#     -100.0, -25.0, 0.1,
# ]

# loadGameButtonInds = [
#     0, 1, 2,
#     0, 2, 3
# ]

# loadGameButton_min_x = min(loadGameButtonVerts[0::6])  
# loadGameButton_max_x = max(loadGameButtonVerts[0::6])  
# loadGameButton_min_y = min(loadGameButtonVerts[1::6])  
# loadGameButton_max_y = max(loadGameButtonVerts[1::6])  

# loadGameButton_width = loadGameButton_max_x - loadGameButton_min_x  
# loadGameButton_height = loadGameButton_max_y - loadGameButton_min_y  

# loadGameButtonProps = {
#     'vertices': np.array(loadGameButtonVerts, dtype=np.float32),
#     'indices': np.array(loadGameButtonInds, dtype=np.uint32),
#     'position': np.array([0, 60, 0.1], dtype=np.float32),
#     'rotation_z': 0.0,
#     'scale': np.array([1, 1, 1], dtype=np.float32),
#     'size': np.array([loadGameButton_width, loadGameButton_height], dtype=np.float32),
# }


import numpy as np

def CreateCircle(center, radius, colour, points = 10, offset = 0, semi = False):
    vertices = [center[0], center[1], center[2], colour[0], colour[1], colour[2]]
    indices = []

    if semi == True:
        for i in range(points+1):
            vertices += [
                center[0] + radius * np.cos(float(i * np.pi)/points),
                center[1] + radius * np.sin(float(i * np.pi)/points),
                center[2],
                colour[0],
                colour[1],
                colour[2],
                ]
            
            ind1 = i+1
            ind2 = i+2 if i != points else 1
            indices += [0 + offset, ind1 + offset, ind2 + offset]
    else:
        for i in range(points):
            vertices += [
                center[0] + radius * np.cos(float(i * 2* np.pi)/points),
                center[1] + radius * np.sin(float(i * 2* np.pi)/points),
                center[2],
                colour[0],
                colour[1],
                colour[2],
                ]
            
            ind1 = i+1
            ind2 = i+2 if i != points-1 else 1
            indices += [0 + offset, ind1 + offset, ind2 + offset]

    return (vertices, indices)    


def CreatePlayer():

    vertices, indices = CreateCircle([0.0, 0.0, 0.0], 1.0, [220/255, 183/255, 139/255], 50, 0)

    eye_verts1, eye_inds1 = CreateCircle([0.4, -0.5, 0.05], 0.3, [1,1,1], 20, len(vertices)/6)
    vertices += eye_verts1
    indices += eye_inds1

    eye_verts2, eye_inds2 = CreateCircle([-0.4, -0.5, 0.05], 0.3, [1,1,1], 20, len(vertices)/6)
    vertices += eye_verts2
    indices += eye_inds2

    eye_verts3, eye_inds3 = CreateCircle([-0.4, -0.5, 0.10], 0.12, [0,0,0], 10, len(vertices)/6)
    vertices += eye_verts3
    indices += eye_inds3

    eye_verts4, eye_inds4 = CreateCircle([0.4, -0.5, 0.10], 0.12, [0,0,0], 10, len(vertices)/6)
    vertices += eye_verts4
    indices += eye_inds4

    eye_verts5, eye_inds5 = CreateCircle([0.0, 0.0, 0.2], 1.0, [1,0,0], 25, len(vertices)/6, True)
    vertices += eye_verts5
    indices += eye_inds5

    eye_verts6, eye_inds6 = CreateCircle([0.0, 0.95, 0.3], 0.3, [0.9,0.9,0.9], 20, len(vertices)/6)
    vertices += eye_verts6
    indices += eye_inds6

    return vertices, indices

def CreateBackground():
    grassColour = [0,1,0]
    waterColour = [0,0,1]

    vertices = [
        -500.0, 500.0, -0.9, grassColour[0], grassColour[1], grassColour[2],
        -400.0, 500.0, -0.9, grassColour[0], grassColour[1], grassColour[2],
        -400.0, -500.0, -0.9, grassColour[0], grassColour[1], grassColour[2],
        -500.0, -500.0, -0.9, grassColour[0], grassColour[1], grassColour[2],

        500.0, 500.0, -0.9, grassColour[0], grassColour[1], grassColour[2],
        400.0, 500.0, -0.9, grassColour[0], grassColour[1], grassColour[2],
        400.0, -500.0, -0.9, grassColour[0], grassColour[1], grassColour[2],
        500.0, -500.0, -0.9, grassColour[0], grassColour[1], grassColour[2],

        -400.0, 500.0, -0.9, waterColour[0], waterColour[1], waterColour[2],
        400.0, 500.0, -0.9, waterColour[0], waterColour[1], waterColour[2],
        400.0, -500.0, -0.9, waterColour[0], waterColour[1], waterColour[2],
        -400.0, -500.0, -0.9, waterColour[0], waterColour[1], waterColour[2],
    ]

    indices = [
        0,1,2, 0,3,2,
        8,9,10, 8,11,10,
        4,5,6, 4,7,6
    ]

    return vertices, indices

playerVerts, playerInds = CreatePlayer()
playerProps = {
    'vertices' : np.array(playerVerts, dtype = np.float32),
    
    'indices' : np.array(playerInds, dtype = np.uint32),

    'position' : np.array([0, 0, 0], dtype = np.float32),

    'rotation_z' : 0.0,

    'scale' : np.array([30, 30, 1], dtype = np.float32),

    'sens' : 125,

    'velocity' : np.array([0, 0, 0], dtype = np.float32)
}

backgroundVerts, backgroundInds = CreateBackground()
backgroundProps = {
    'vertices' : np.array(backgroundVerts, dtype = np.float32),
    
    'indices' : np.array(backgroundInds, dtype = np.uint32),

    'position' : np.array([0, 0, 0], dtype = np.float32),

    'rotation_z' : 0.0,

    'scale' : np.array([1, 1, 1], dtype = np.float32),

    'boundary' : [500.0, -500.0, 500.0, 500.0],

    'river_banks': [-400.0, 400.0]
}

homepageVerts = [
    -500.0, 500.0, 0.0, 0.57, 0.90, 0.96,
    500.0, 500.0, 0.0, 0.57, 0.90, 0.96, 
    500.0, -500.0, 0.0, 0.57, 0.90, 0.96,
    -500.0, -500.0, 0.0, 0.57, 0.90, 0.96
]

homepageInds = [
    0, 1, 2,
    0, 2, 3 
]

homepageProps = {
    'vertices': np.array(homepageVerts, dtype=np.float32),
    'indices': np.array(homepageInds, dtype=np.uint32),
    'position': np.array([0, 0, 0], dtype=np.float32),
    'rotation_z': 0.0,
    'scale': np.array([1, 1, 1], dtype=np.float32)
}


newGameButtonVerts = [
    -100.0, 25.0, 0.1,
    100.0, 25.0, 0.1,
    100.0, -25.0, 0.1,
    -100.0, -25.0, 0.1,
]


newGameButtonInds = [
    0, 1, 2,
    0, 2, 3
]

newGameButton_min_x = min(newGameButtonVerts[0::6]) 
newGameButton_max_x = max(newGameButtonVerts[0::6]) 
newGameButton_min_y = min(newGameButtonVerts[1::6]) 
newGameButton_max_y = max(newGameButtonVerts[1::6]) 

newGameButton_width = newGameButton_max_x - newGameButton_min_x 
newGameButton_height = newGameButton_max_y - newGameButton_min_y  

newGameButtonProps = {
    'vertices': np.array(newGameButtonVerts, dtype=np.float32),
    'indices': np.array(newGameButtonInds, dtype=np.uint32),
    'position': np.array([0, 120, 0.1], dtype=np.float32),
    'rotation_z': 0.0,
    'scale': np.array([1, 1, 1], dtype=np.float32),
    'size': np.array([newGameButton_width, newGameButton_height], dtype=np.float32),
}

loadGameButtonVerts = [
    -100.0, 25.0, 0.1, 
    100.0, 25.0, 0.1,
    100.0, -25.0, 0.1, 
    -100.0, -25.0, 0.1,
]

loadGameButtonInds = [
    0, 1, 2,
    0, 2, 3
]

loadGameButton_min_x = min(loadGameButtonVerts[0::6])  
loadGameButton_max_x = max(loadGameButtonVerts[0::6])  
loadGameButton_min_y = min(loadGameButtonVerts[1::6])  
loadGameButton_max_y = max(loadGameButtonVerts[1::6])  

loadGameButton_width = loadGameButton_max_x - loadGameButton_min_x  
loadGameButton_height = loadGameButton_max_y - loadGameButton_min_y  

loadGameButtonProps = {
    'vertices': np.array(loadGameButtonVerts, dtype=np.float32),
    'indices': np.array(loadGameButtonInds, dtype=np.uint32),
    'position': np.array([0, 60, 0.1], dtype=np.float32),
    'rotation_z': 0.0,
    'scale': np.array([1, 1, 1], dtype=np.float32),
    'size': np.array([loadGameButton_width, loadGameButton_height], dtype=np.float32),
}
