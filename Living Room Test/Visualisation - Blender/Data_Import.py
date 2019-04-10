import bpy
import bmesh
import numpy as np
import pandas as pd

print("vertpaint------------------------------------------")

data_path = "cnstdata.csv"

temps = pd.read_csv(data_path, header = None)


def clfnc(temp):
 
    if temp<20:
        R = 1+(temp-20)/10
        G = 1-(((temp-20)/10)**2)**0.5
        B = 1
    elif temp>20:
        R = 1
        G = 1-(((temp-20)/10)**2)**0.5
        B = 1-(temp-20)/10
    else:
        R=1
        B=1
        G=1
    
    return (R,G,B)

def getcol(snsr):
        scene = bpy.context.scene
        frame = scene.frame_current
        try:
            temp = temps.iat[frame,snsr]
            color = clfnc(temp)
        except IndexError:
            color = (0,0,0)
        
        return color

def canim(scene):
        

        ob = bpy.context.active_object

        mesh = ob.data

        if mesh.vertex_colors:
            vcol_layer = mesh.vertex_colors.active
        else:
            vcol_layer = mesh.vertex_colors.new()

        
        for vert in range(len(mesh.vertices)):
             for poly in mesh.polygons:
                    for loop_index in poly.loop_indices:
                        loop_vert_index = mesh.loops[loop_index].vertex_index
                        if vert == loop_vert_index:
                            color = getcol(vert+1)
                            vcol_layer.data[loop_index].color = color
                        
bpy.app.handlers.frame_change_pre.append(canim)

#https://blender.stackexchange.com/questions/36577/how-are-vertex-indices-determined