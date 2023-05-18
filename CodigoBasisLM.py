# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 22:46:36 2021

@author: Melissa
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 21:01:25 2020

@author: Melii
"""
import Leap, sys, thread, time
import numpy as np
import pandas as pd
from datetime import datetime

current = datetime.now().strftime('%Y%m%d%H%M%S')
label = 1

hand_position_x = []
hand_position_y = []
hand_position_z = []
pitch_list = []
roll_list = []
yaw_list = []
arm_direction_x = []
arm_direction_y = []
arm_direction_z = []
wrist_position_x = []
wrist_position_y = []
wrist_position_z = []
elbow_position_x = []
elbow_position_y = []
elbow_position_z = []

arm_basis_x_x = []
arm_basis_x_y = []
arm_basis_x_z = []

arm_basis_y_x = []
arm_basis_y_y = []
arm_basis_y_z = []

arm_basis_z_x = []
arm_basis_z_y = []
arm_basis_z_z = []

Hand_basis_x_x = []
Hand_basis_x_y = []
Hand_basis_x_z = []

Hand_basis_y_x = []
Hand_basis_y_y = []
Hand_basis_y_z = []

Hand_basis_z_x = []
Hand_basis_z_y = []
Hand_basis_z_z = []


Thumb_fin_meta_direction_x = []
Thumb_fin_meta_direction_y = []
Thumb_fin_meta_direction_z = []
Thumb_fin_prox_direction_x = []
Thumb_fin_prox_direction_y = []
Thumb_fin_prox_direction_z = []
Thumb_fin_inter_direction_x = []
Thumb_fin_inter_direction_y = []
Thumb_fin_inter_direction_z = []
Thumb_fin_dist_direction_x = []
Thumb_fin_dist_direction_y = []
Thumb_fin_dist_direction_z = []
Thumb_fin_meta_start_x=[]
Thumb_fin_meta_start_y=[]
Thumb_fin_meta_start_z=[]
Thumb_fin_meta_end_x=[]
Thumb_fin_meta_end_y=[]
Thumb_fin_meta_end_z=[]
Thumb_fin_prox_start_x=[]
Thumb_fin_prox_start_y=[]
Thumb_fin_prox_start_z=[]
Thumb_fin_prox_end_x=[]
Thumb_fin_prox_end_y=[]
Thumb_fin_prox_end_z=[]
Thumb_fin_inter_start_x=[]
Thumb_fin_inter_start_y=[]
Thumb_fin_inter_start_z=[]
Thumb_fin_inter_end_x=[]
Thumb_fin_inter_end_y=[]
Thumb_fin_inter_end_z=[]
Thumb_fin_dist_start_x=[]
Thumb_fin_dist_start_y=[]
Thumb_fin_dist_start_z=[]
Thumb_fin_dist_end_x=[]
Thumb_fin_dist_end_y=[]
Thumb_fin_dist_end_z=[]


Index_fin_meta_direction_x = []
Index_fin_meta_direction_y = []
Index_fin_meta_direction_z = []
Index_fin_prox_direction_x = []
Index_fin_prox_direction_y = []
Index_fin_prox_direction_z = []
Index_fin_inter_direction_x = []
Index_fin_inter_direction_y = []
Index_fin_inter_direction_z = []
Index_fin_dist_direction_x = []
Index_fin_dist_direction_y = []
Index_fin_dist_direction_z = []
Index_fin_meta_start_x=[]
Index_fin_meta_start_y=[]
Index_fin_meta_start_z=[]
Index_fin_meta_end_x=[]
Index_fin_meta_end_y=[]
Index_fin_meta_end_z=[]
Index_fin_prox_start_x=[]
Index_fin_prox_start_y=[]
Index_fin_prox_start_z=[]
Index_fin_prox_end_x=[]
Index_fin_prox_end_y=[]
Index_fin_prox_end_z=[]
Index_fin_inter_start_x=[]
Index_fin_inter_start_y=[]
Index_fin_inter_start_z=[]
Index_fin_inter_end_x=[]
Index_fin_inter_end_y=[]
Index_fin_inter_end_z=[]
Index_fin_dist_start_x=[]
Index_fin_dist_start_y=[]
Index_fin_dist_start_z=[]
Index_fin_dist_end_x=[]
Index_fin_dist_end_y=[]
Index_fin_dist_end_z=[]



Middle_fin_meta_direction_x = []
Middle_fin_meta_direction_y = []
Middle_fin_meta_direction_z = []
Middle_fin_prox_direction_x = []
Middle_fin_prox_direction_y = []
Middle_fin_prox_direction_z = []
Middle_fin_inter_direction_x = []
Middle_fin_inter_direction_y = []
Middle_fin_inter_direction_z = []
Middle_fin_dist_direction_x = []
Middle_fin_dist_direction_y = []
Middle_fin_dist_direction_z = []
Middle_fin_meta_start_x=[]
Middle_fin_meta_start_y=[]
Middle_fin_meta_start_z=[]
Middle_fin_meta_end_x=[]
Middle_fin_meta_end_y=[]
Middle_fin_meta_end_z=[]
Middle_fin_prox_start_x=[]
Middle_fin_prox_start_y=[]
Middle_fin_prox_start_z=[]
Middle_fin_prox_end_x=[]
Middle_fin_prox_end_y=[]
Middle_fin_prox_end_z=[]
Middle_fin_inter_start_x=[]
Middle_fin_inter_start_y=[]
Middle_fin_inter_start_z=[]
Middle_fin_inter_end_x=[]
Middle_fin_inter_end_y=[]
Middle_fin_inter_end_z=[]
Middle_fin_dist_start_x=[]
Middle_fin_dist_start_y=[]
Middle_fin_dist_start_z=[]
Middle_fin_dist_end_x=[]
Middle_fin_dist_end_y=[]
Middle_fin_dist_end_z=[]


    
Middle_x_basis_x=[]
Middle_x_basis_y=[]
Middle_x_basis_z=[]

Middle_y_basis_x=[]
Middle_y_basis_y=[]
Middle_y_basis_z=[]

Middle_z_basis_x=[]
Middle_z_basis_y=[]
Middle_z_basis_z=[]

Middle_origin_x=[]
Middle_origin_y=[]
Middle_origin_z=[]
                            

Ring_fin_meta_direction_x = []
Ring_fin_meta_direction_y = []
Ring_fin_meta_direction_z = []
Ring_fin_prox_direction_x = []
Ring_fin_prox_direction_y = []
Ring_fin_prox_direction_z = []
Ring_fin_inter_direction_x = []
Ring_fin_inter_direction_y = []
Ring_fin_inter_direction_z = []
Ring_fin_dist_direction_x = []
Ring_fin_dist_direction_y = []
Ring_fin_dist_direction_z = []
Ring_fin_meta_start_x=[]
Ring_fin_meta_start_y=[]
Ring_fin_meta_start_z=[]
Ring_fin_meta_end_x=[]
Ring_fin_meta_end_y=[]
Ring_fin_meta_end_z=[]
Ring_fin_prox_start_x=[]
Ring_fin_prox_start_y=[]
Ring_fin_prox_start_z=[]
Ring_fin_prox_end_x=[]
Ring_fin_prox_end_y=[]
Ring_fin_prox_end_z=[]
Ring_fin_inter_start_x=[]
Ring_fin_inter_start_y=[]
Ring_fin_inter_start_z=[]
Ring_fin_inter_end_x=[]
Ring_fin_inter_end_y=[]
Ring_fin_inter_end_z=[]
Ring_fin_dist_start_x=[]
Ring_fin_dist_start_y=[]
Ring_fin_dist_start_z=[]
Ring_fin_dist_end_x=[]
Ring_fin_dist_end_y=[]
Ring_fin_dist_end_z=[]


Pinky_fin_meta_direction_x = []
Pinky_fin_meta_direction_y = []
Pinky_fin_meta_direction_z = []
Pinky_fin_prox_direction_x = []
Pinky_fin_prox_direction_y = []
Pinky_fin_prox_direction_z = []
Pinky_fin_inter_direction_x = []
Pinky_fin_inter_direction_y = []
Pinky_fin_inter_direction_z = []
Pinky_fin_dist_direction_x = []
Pinky_fin_dist_direction_y = []
Pinky_fin_dist_direction_z = []
Pinky_fin_meta_start_x=[]
Pinky_fin_meta_start_y=[]
Pinky_fin_meta_start_z=[]
Pinky_fin_meta_end_x=[]
Pinky_fin_meta_end_y=[]
Pinky_fin_meta_end_z=[]
Pinky_fin_prox_start_x=[]
Pinky_fin_prox_start_y=[]
Pinky_fin_prox_start_z=[]
Pinky_fin_prox_end_x=[]
Pinky_fin_prox_end_y=[]
Pinky_fin_prox_end_z=[]
Pinky_fin_inter_start_x=[]
Pinky_fin_inter_start_y=[]
Pinky_fin_inter_start_z=[]
Pinky_fin_inter_end_x=[]
Pinky_fin_inter_end_y=[]
Pinky_fin_inter_end_z=[]
Pinky_fin_dist_start_x=[]
Pinky_fin_dist_start_y=[]
Pinky_fin_dist_start_z=[]
Pinky_fin_dist_end_x=[]
Pinky_fin_dist_end_y=[]
Pinky_fin_dist_end_z=[]
Tiempo=[]

label_list = []

"""
def data_maker(*data_list):
    if self.finger_names[finger.type] == 'Thumb':
        if self.bone_names[bone.type] == 'Metacarpal':
            Thumb_bone_list.append()
        if self.bone_names[bone.type] == 'Proximal':
            Thumb_bone_list.append()
        if self.bone_names[bone.type] == 'Intermediate':
            Thumb_bone_list.append()
        if self.bone_names[bone.type] == 'Distal':
"""

class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()
        
   

        print "Frame id:" + str(frame.id) + "timestamp: " + str(frame.timestamp) + "hands: " +  str(len(frame.hands)) + "fingers: " + str(len(frame.fingers))

        # Get hands
        for hand in frame.hands:

            handType = "Left hand" if hand.is_left else "Right hand"

            """print "  %s, id %d, position: %s" % (handType, hand.id, hand.palm_position)"""
            print handType + " Han ID: " + str(hand.id) + "Palm Position: " + str(hand.palm_position)
            # Get the hand's normal vector and direction
            normal = hand.palm_normal
            direction = hand.direction

            pitch = direction.pitch * Leap.RAD_TO_DEG
            roll = normal.roll * Leap.RAD_TO_DEG
            yaw = direction.yaw * Leap.RAD_TO_DEG
            
            """print "Pitch: " + str(direction.pitch * Leap.RAD_TO_DEG) + "Roll: " 
            + str(normal.roll * Leap.RAD_TO_DEG) + "Yaw: " + str(direction.yaw * Leap.RAD_TO_DEG)"""
            # Calculate the hand's pitch, roll, and yaw angles
            print "  pitch: " + str(pitch)+ "roll: " + str(roll) + "yaw: " + str(yaw) + "handBasis: " + str(hand.basis)

            # Get arm bone
            arm = hand.arm
            
            
            
            print "  Arm direction: " + str(arm.direction) + "armM: " + str(arm.basis) + "arm_basis: " + str(arm.basis.x_basis) + "arm_basis_x: " + str(arm.basis.x_basis.x)
            

            # Get fingers

            for finger in hand.fingers:

                print " finger: " + self.finger_names[finger.type] + "id: " + str(finger.id) + "length: " + str(finger.length) + "width: " + str(finger.width)

                # Get bones
                for b in range(0, 4):
                    bone = finger.bone(b)
                    print "bone: " + self.bone_names[bone.type] + "M_basis" + str(bone.basis)  + "Basis_x:" + str(bone.basis.x_basis) + "Basis_x_y:" + str(bone.basis.x_basis.y)
                   

                    
## Pulgar
                    if self.finger_names[finger.type] == 'Thumb':
                        if self.bone_names[bone.type] == 'Metacarpal':
                            Thumb_fin_meta_direction_x.append(bone.direction.x)
                            Thumb_fin_meta_direction_y.append(bone.direction.y)
                            Thumb_fin_meta_direction_z.append(bone.direction.z)
                            Thumb_fin_meta_start_x.append(bone.prev_joint.x)
                            Thumb_fin_meta_start_y.append(bone.prev_joint.y)
                            Thumb_fin_meta_start_z.append(bone.prev_joint.z)
                            Thumb_fin_meta_end_x.append(bone.next_joint.x)
                            Thumb_fin_meta_end_y.append(bone.next_joint.y)
                            Thumb_fin_meta_end_z.append(bone.next_joint.z)
                        if self.bone_names[bone.type] == 'Proximal':
                            Thumb_fin_prox_direction_x.append(bone.direction.x)
                            Thumb_fin_prox_direction_y.append(bone.direction.y)
                            Thumb_fin_prox_direction_z.append(bone.direction.z)
                            Thumb_fin_prox_start_x.append(bone.prev_joint.x)
                            Thumb_fin_prox_start_y.append(bone.prev_joint.y)
                            Thumb_fin_prox_start_z.append(bone.prev_joint.z)
                            Thumb_fin_prox_end_x.append(bone.next_joint.x)
                            Thumb_fin_prox_end_y.append(bone.next_joint.y)
                            Thumb_fin_prox_end_z.append(bone.next_joint.z)
                        if self.bone_names[bone.type] == 'Intermediate':
                            Thumb_fin_inter_direction_x.append(bone.direction.x)
                            Thumb_fin_inter_direction_y.append(bone.direction.y)
                            Thumb_fin_inter_direction_z.append(bone.direction.z)
                            Thumb_fin_inter_start_x.append(bone.prev_joint.x)
                            Thumb_fin_inter_start_y.append(bone.prev_joint.y)
                            Thumb_fin_inter_start_z.append(bone.prev_joint.z)
                            Thumb_fin_inter_end_x.append(bone.next_joint.x)
                            Thumb_fin_inter_end_y.append(bone.next_joint.y)
                            Thumb_fin_inter_end_z.append(bone.next_joint.z)
                        if self.bone_names[bone.type] == 'Distal':
                            Thumb_fin_dist_direction_x.append(bone.direction.x)
                            Thumb_fin_dist_direction_y.append(bone.direction.y)
                            Thumb_fin_dist_direction_z.append(bone.direction.z)
                            Thumb_fin_dist_start_x.append(bone.prev_joint.x)
                            Thumb_fin_dist_start_y.append(bone.prev_joint.y)
                            Thumb_fin_dist_start_z.append(bone.prev_joint.z)
                            Thumb_fin_dist_end_x.append(bone.next_joint.x)
                            Thumb_fin_dist_end_y.append(bone.next_joint.y)
                            Thumb_fin_dist_end_z.append(bone.next_joint.z)
                            
## Indice
                    if self.finger_names[finger.type] == 'Index':
                        if self.bone_names[bone.type] == 'Metacarpal':
                            Index_fin_meta_direction_x.append(bone.direction.x)
                            Index_fin_meta_direction_y.append(bone.direction.y)
                            Index_fin_meta_direction_z.append(bone.direction.z)
                            Index_fin_meta_start_x.append(bone.prev_joint.x)
                            Index_fin_meta_start_y.append(bone.prev_joint.y)
                            Index_fin_meta_start_z.append(bone.prev_joint.z)
                            Index_fin_meta_end_x.append(bone.next_joint.x)
                            Index_fin_meta_end_y.append(bone.next_joint.y)
                            Index_fin_meta_end_z.append(bone.next_joint.z)
                        if self.bone_names[bone.type] == 'Proximal':
                            Index_fin_prox_direction_x.append(bone.direction.x)
                            Index_fin_prox_direction_y.append(bone.direction.y)
                            Index_fin_prox_direction_z.append(bone.direction.z)
                            Index_fin_prox_start_x.append(bone.prev_joint.x)
                            Index_fin_prox_start_y.append(bone.prev_joint.y)
                            Index_fin_prox_start_z.append(bone.prev_joint.z)
                            Index_fin_prox_end_x.append(bone.next_joint.x)
                            Index_fin_prox_end_y.append(bone.next_joint.y)
                            Index_fin_prox_end_z.append(bone.next_joint.z)
                        if self.bone_names[bone.type] == 'Intermediate':
                            Index_fin_inter_direction_x.append(bone.direction.x)
                            Index_fin_inter_direction_y.append(bone.direction.y)
                            Index_fin_inter_direction_z.append(bone.direction.z)
                            Index_fin_inter_start_x.append(bone.prev_joint.x)
                            Index_fin_inter_start_y.append(bone.prev_joint.y)
                            Index_fin_inter_start_z.append(bone.prev_joint.z)
                            Index_fin_inter_end_x.append(bone.next_joint.x)
                            Index_fin_inter_end_y.append(bone.next_joint.y)
                            Index_fin_inter_end_z.append(bone.next_joint.z)
                        if self.bone_names[bone.type] == 'Distal':
                            Index_fin_dist_direction_x.append(bone.direction.x)
                            Index_fin_dist_direction_y.append(bone.direction.y)
                            Index_fin_dist_direction_z.append(bone.direction.z)
                            Index_fin_dist_start_x.append(bone.prev_joint.x)
                            Index_fin_dist_start_y.append(bone.prev_joint.y)
                            Index_fin_dist_start_z.append(bone.prev_joint.z)
                            Index_fin_dist_end_x.append(bone.next_joint.x)
                            Index_fin_dist_end_y.append(bone.next_joint.y)
                            Index_fin_dist_end_z.append(bone.next_joint.z)
                            
## Dedo medio

                    if self.finger_names[finger.type] == 'Middle':
                        if self.bone_names[bone.type] == 'Metacarpal':
                            Middle_fin_meta_direction_x.append(bone.direction.x)
                            Middle_fin_meta_direction_y.append(bone.direction.y)
                            Middle_fin_meta_direction_z.append(bone.direction.z)
                            Middle_fin_meta_start_x.append(bone.prev_joint.x)
                            Middle_fin_meta_start_y.append(bone.prev_joint.y)
                            Middle_fin_meta_start_z.append(bone.prev_joint.z)
                            Middle_fin_meta_end_x.append(bone.next_joint.x)
                            Middle_fin_meta_end_y.append(bone.next_joint.y)
                            Middle_fin_meta_end_z.append(bone.next_joint.z)                       
                            
                        
                            
                        if self.bone_names[bone.type] == 'Proximal':
                            Middle_fin_prox_direction_x.append(bone.direction.x)
                            Middle_fin_prox_direction_y.append(bone.direction.y)
                            Middle_fin_prox_direction_z.append(bone.direction.z)
                            Middle_fin_prox_start_x.append(bone.prev_joint.x)
                            Middle_fin_prox_start_y.append(bone.prev_joint.y)
                            Middle_fin_prox_start_z.append(bone.prev_joint.z)
                            Middle_fin_prox_end_x.append(bone.next_joint.x)
                            Middle_fin_prox_end_y.append(bone.next_joint.y)
                            Middle_fin_prox_end_z.append(bone.next_joint.z)
                            
                                ##Vectores base
                                        
                            Middle_x_basis_x.append(bone.basis.x_basis.x)
                            Middle_x_basis_y.append(bone.basis.x_basis.y)
                            Middle_x_basis_z.append(bone.basis.x_basis.z)
                            
                            Middle_y_basis_x.append(bone.basis.y_basis.x)
                            Middle_y_basis_y.append(bone.basis.y_basis.y)
                            Middle_y_basis_z.append(bone.basis.y_basis.z)
                            
                            Middle_z_basis_x.append(bone.basis.z_basis.x)
                            Middle_z_basis_y.append(bone.basis.z_basis.y)
                            Middle_z_basis_z.append(bone.basis.z_basis.z)
                            
                            Middle_origin_x.append(bone.basis.origin.x)
                            Middle_origin_y.append(bone.basis.origin.y)
                            Middle_origin_z.append(bone.basis.origin.z)
                            
                        if self.bone_names[bone.type] == 'Intermediate':
                            Middle_fin_inter_direction_x.append(bone.direction.x)
                            Middle_fin_inter_direction_y.append(bone.direction.y)
                            Middle_fin_inter_direction_z.append(bone.direction.z)
                            Middle_fin_inter_start_x.append(bone.prev_joint.x)
                            Middle_fin_inter_start_y.append(bone.prev_joint.y)
                            Middle_fin_inter_start_z.append(bone.prev_joint.z)
                            Middle_fin_inter_end_x.append(bone.next_joint.x)
                            Middle_fin_inter_end_y.append(bone.next_joint.y)
                            Middle_fin_inter_end_z.append(bone.next_joint.z)
                        if self.bone_names[bone.type] == 'Distal':
                            Middle_fin_dist_direction_x.append(bone.direction.x)
                            Middle_fin_dist_direction_y.append(bone.direction.y)
                            Middle_fin_dist_direction_z.append(bone.direction.z)
                            Middle_fin_dist_start_x.append(bone.prev_joint.x)
                            Middle_fin_dist_start_y.append(bone.prev_joint.y)
                            Middle_fin_dist_start_z.append(bone.prev_joint.z)
                            Middle_fin_dist_end_x.append(bone.next_joint.x)
                            Middle_fin_dist_end_y.append(bone.next_joint.y)
                            Middle_fin_dist_end_z.append(bone.next_joint.z)
                            
## Dedoa anuñar
                            
                    if self.finger_names[finger.type] == 'Ring':
                        if self.bone_names[bone.type] == 'Metacarpal':
                            Ring_fin_meta_direction_x.append(bone.direction.x)
                            Ring_fin_meta_direction_y.append(bone.direction.y)
                            Ring_fin_meta_direction_z.append(bone.direction.z)
                            Ring_fin_meta_start_x.append(bone.prev_joint.x)
                            Ring_fin_meta_start_y.append(bone.prev_joint.y)
                            Ring_fin_meta_start_z.append(bone.prev_joint.z)
                            Ring_fin_meta_end_x.append(bone.next_joint.x)
                            Ring_fin_meta_end_y.append(bone.next_joint.y)
                            Ring_fin_meta_end_z.append(bone.next_joint.z)
                        if self.bone_names[bone.type] == 'Proximal':
                            Ring_fin_prox_direction_x.append(bone.direction.x)
                            Ring_fin_prox_direction_y.append(bone.direction.y)
                            Ring_fin_prox_direction_z.append(bone.direction.z)
                            Ring_fin_prox_start_x.append(bone.prev_joint.x)
                            Ring_fin_prox_start_y.append(bone.prev_joint.y)
                            Ring_fin_prox_start_z.append(bone.prev_joint.z)
                            Ring_fin_prox_end_x.append(bone.next_joint.x)
                            Ring_fin_prox_end_y.append(bone.next_joint.y)
                            Ring_fin_prox_end_z.append(bone.next_joint.z)
                        if self.bone_names[bone.type] == 'Intermediate':
                            Ring_fin_inter_direction_x.append(bone.direction.x)
                            Ring_fin_inter_direction_y.append(bone.direction.y)
                            Ring_fin_inter_direction_z.append(bone.direction.z)
                            Ring_fin_inter_start_x.append(bone.prev_joint.x)
                            Ring_fin_inter_start_y.append(bone.prev_joint.y)
                            Ring_fin_inter_start_z.append(bone.prev_joint.z)
                            Ring_fin_inter_end_x.append(bone.next_joint.x)
                            Ring_fin_inter_end_y.append(bone.next_joint.y)
                            Ring_fin_inter_end_z.append(bone.next_joint.z)
                        if self.bone_names[bone.type] == 'Distal':
                            Ring_fin_dist_direction_x.append(bone.direction.x)
                            Ring_fin_dist_direction_y.append(bone.direction.y)
                            Ring_fin_dist_direction_z.append(bone.direction.z)
                            Ring_fin_dist_start_x.append(bone.prev_joint.x)
                            Ring_fin_dist_start_y.append(bone.prev_joint.y)
                            Ring_fin_dist_start_z.append(bone.prev_joint.z)
                            Ring_fin_dist_end_x.append(bone.next_joint.x)
                            Ring_fin_dist_end_y.append(bone.next_joint.y)
                            Ring_fin_dist_end_z.append(bone.next_joint.z)
                            
## Dedo meñique
                            
                    if self.finger_names[finger.type] == 'Pinky':
                        if self.bone_names[bone.type] == 'Metacarpal':
                            Pinky_fin_meta_direction_x.append(bone.direction.x)
                            Pinky_fin_meta_direction_y.append(bone.direction.y)
                            Pinky_fin_meta_direction_z.append(bone.direction.z)
                            Pinky_fin_meta_start_x.append(bone.prev_joint.x)
                            Pinky_fin_meta_start_y.append(bone.prev_joint.y)
                            Pinky_fin_meta_start_z.append(bone.prev_joint.z)
                            Pinky_fin_meta_end_x.append(bone.next_joint.x)
                            Pinky_fin_meta_end_y.append(bone.next_joint.y)
                            Pinky_fin_meta_end_z.append(bone.next_joint.z)
                        if self.bone_names[bone.type] == 'Proximal':
                            Pinky_fin_prox_direction_x.append(bone.direction.x)
                            Pinky_fin_prox_direction_y.append(bone.direction.y)
                            Pinky_fin_prox_direction_z.append(bone.direction.z)
                            Pinky_fin_prox_start_x.append(bone.prev_joint.x)
                            Pinky_fin_prox_start_y.append(bone.prev_joint.y)
                            Pinky_fin_prox_start_z.append(bone.prev_joint.z)
                            Pinky_fin_prox_end_x.append(bone.next_joint.x)
                            Pinky_fin_prox_end_y.append(bone.next_joint.y)
                            Pinky_fin_prox_end_z.append(bone.next_joint.z)
                        if self.bone_names[bone.type] == 'Intermediate':
                            Pinky_fin_inter_direction_x.append(bone.direction.x)
                            Pinky_fin_inter_direction_y.append(bone.direction.y)
                            Pinky_fin_inter_direction_z.append(bone.direction.z)
                            Pinky_fin_inter_start_x.append(bone.prev_joint.x)
                            Pinky_fin_inter_start_y.append(bone.prev_joint.y)
                            Pinky_fin_inter_start_z.append(bone.prev_joint.z)
                            Pinky_fin_inter_end_x.append(bone.next_joint.x)
                            Pinky_fin_inter_end_y.append(bone.next_joint.y)
                            Pinky_fin_inter_end_z.append(bone.next_joint.z)
                        if self.bone_names[bone.type] == 'Distal':
                            Pinky_fin_dist_direction_x.append(bone.direction.x)
                            Pinky_fin_dist_direction_y.append(bone.direction.y)
                            Pinky_fin_dist_direction_z.append(bone.direction.z)
                            Pinky_fin_dist_start_x.append(bone.prev_joint.x)
                            Pinky_fin_dist_start_y.append(bone.prev_joint.y)
                            Pinky_fin_dist_start_z.append(bone.prev_joint.z)
                            Pinky_fin_dist_end_x.append(bone.next_joint.x)
                            Pinky_fin_dist_end_y.append(bone.next_joint.y)
                            Pinky_fin_dist_end_z.append(bone.next_joint.z)

            hand_position_x.append(hand.palm_position.x)
            hand_position_y.append(hand.palm_position.y)
            hand_position_z.append(hand.palm_position.z)
            
            Hand_basis_x_x.append(hand.basis.x_basis.x)
            Hand_basis_x_y.append(hand.basis.x_basis.y)
            Hand_basis_x_z.append(hand.basis.x_basis.z)
            
            Hand_basis_y_x.append(hand.basis.y_basis.x)
            Hand_basis_y_y.append(hand.basis.y_basis.y)
            Hand_basis_y_z.append(hand.basis.y_basis.z)
            
            Hand_basis_z_x.append(hand.basis.z_basis.x)
            Hand_basis_z_y.append(hand.basis.z_basis.y)
            Hand_basis_z_z.append(hand.basis.z_basis.z)
          

            pitch_list.append(pitch)
            roll_list.append(roll)
            yaw_list.append(yaw)
            arm_direction_x.append(arm.direction.x)
            arm_direction_y.append(arm.direction.y)
            arm_direction_z.append(arm.direction.z)
            wrist_position_x.append(arm.wrist_position.x)
            wrist_position_y.append(arm.wrist_position.y)
            wrist_position_z.append(arm.wrist_position.z)
            elbow_position_x.append(arm.elbow_position.x)
            elbow_position_y.append(arm.elbow_position.y)
            elbow_position_z.append(arm.elbow_position.z)
            
            arm_basis_x_x.append(arm.basis.x_basis.x)
            arm_basis_x_y.append(arm.basis.x_basis.y)
            arm_basis_x_z.append(arm.basis.x_basis.z)
            
            arm_basis_y_x.append(arm.basis.y_basis.x)
            arm_basis_y_y.append(arm.basis.y_basis.y)
            arm_basis_y_z.append(arm.basis.y_basis.z)
            
            arm_basis_z_x.append(arm.basis.z_basis.x)
            arm_basis_z_y.append(arm.basis.z_basis.y)
            arm_basis_z_z.append(arm.basis.z_basis.z)
            
            
            
            Tiempo.append(frame.timestamp)
            label_list.append(label)


        if not frame.hands.is_empty:
            print ""

def data_save_pandas():
    df = pd.DataFrame({
        "hand_position_x" : hand_position_x,
        "hand_position_y" : hand_position_y,
        "hand_position_z" : hand_position_z,
        "pitch" : pitch_list,
        "roll" : roll_list,
        "yaw" : yaw_list,
        "wrist_position_x" : wrist_position_x,
        "wrist_position_y" : wrist_position_y,
        "wrist_position_z" : wrist_position_z,
        "elbow_position_x" : elbow_position_x,
        "elbow_position_y" : elbow_position_y,
        "elbow_position_z" : elbow_position_z,
        "arm_direction_x" : arm_direction_x,
        "arm_direction_y" : arm_direction_y,
        "arm_direction_z" : arm_direction_z,
        
        "arm_basis_x_x" : arm_basis_x_x,
        "arm_basis_x_y" : arm_basis_x_y,
        "arm_basis_x_z" : arm_basis_x_z,        
        
        "arm_basis_y_x" : arm_basis_y_x,
        "arm_basis_y_y" : arm_basis_y_y,
        "arm_basis_y_z" : arm_basis_y_z,        
        
        "arm_basis_z_x" : arm_basis_z_x,
        "arm_basis_z_y" : arm_basis_z_y,
        "arm_basis_z_z" : arm_basis_z_z,
        
        "Hand_basis_x_x" : Hand_basis_x_x,
        "Hand_basis_x_y" : Hand_basis_x_y,
        "Hand_basis_x_z" : Hand_basis_x_z,        
        
        "Hand_basis_y_x" : Hand_basis_y_x,
        "Hand_basis_y_y" : Hand_basis_y_y,
        "Hand_basis_y_z" : Hand_basis_y_z,        
        
        "Hand_basis_z_x" : Hand_basis_z_x,
        "Hand_basis_z_y" : Hand_basis_z_y,
        "Hand_basis_z_z" : Hand_basis_z_z,
        
        
## Dedo pulgar
        
        "Thumb_fin_meta_direction_x" : Thumb_fin_meta_direction_x,
        "Thumb_fin_meta_direction_y" : Thumb_fin_meta_direction_y,
        "Thumb_fin_meta_direction_z" : Thumb_fin_meta_direction_z,
        "Thumb_fin_prox_direction_x" : Thumb_fin_prox_direction_x,
        "Thumb_fin_prox_direction_y" : Thumb_fin_prox_direction_y,
        "Thumb_fin_prox_direction_z" : Thumb_fin_prox_direction_z,
        "Thumb_fin_inter_direction_x" : Thumb_fin_inter_direction_x,
        "Thumb_fin_inter_direction_y" : Thumb_fin_inter_direction_y,
        "Thumb_fin_inter_direction_z" : Thumb_fin_inter_direction_z,
        "Thumb_fin_dist_direction_x" : Thumb_fin_dist_direction_x,
        "Thumb_fin_dist_direction_y" : Thumb_fin_dist_direction_y,
        "Thumb_fin_dist_direction_z" : Thumb_fin_dist_direction_z,
        
        "Thumb_fin_meta_start_x" : Thumb_fin_meta_start_x,
        "Thumb_fin_meta_start_y" : Thumb_fin_meta_start_y,
        "Thumb_fin_meta_start_z" : Thumb_fin_meta_start_z,
        "Thumb_fin_meta_end_x" : Thumb_fin_meta_end_x,
        "Thumb_fin_meta_end_y" : Thumb_fin_meta_end_y,
        "Thumb_fin_meta_end_z" : Thumb_fin_meta_end_z,
        "Thumb_fin_prox_start_x" : Thumb_fin_prox_start_x,
        "Thumb_fin_prox_start_y" : Thumb_fin_prox_start_y,
        "Thumb_fin_prox_start_z" : Thumb_fin_prox_start_z,
        "Thumb_fin_prox_end_x" : Thumb_fin_prox_end_x,
        "Thumb_fin_prox_end_y" : Thumb_fin_prox_end_y,
        "Thumb_fin_prox_end_z" : Thumb_fin_prox_end_z,
        "Thumb_fin_inter_start_x" : Thumb_fin_inter_start_x,
        "Thumb_fin_inter_start_y" : Thumb_fin_inter_start_y,
        "Thumb_fin_inter_start_z" : Thumb_fin_inter_start_z,
        "Thumb_fin_inter_end_x" : Thumb_fin_inter_end_x,
        "Thumb_fin_inter_end_y" : Thumb_fin_inter_end_y,
        "Thumb_fin_inter_end_z" : Thumb_fin_inter_end_z,
        "Thumb_fin_dist_start_x" : Thumb_fin_dist_start_x,
        "Thumb_fin_dist_start_y" : Thumb_fin_dist_start_y,
        "Thumb_fin_dist_start_z" : Thumb_fin_dist_start_z,
        "Thumb_fin_dist_end_x" : Thumb_fin_dist_end_x,
        "Thumb_fin_dist_end_y" : Thumb_fin_dist_end_y,
        "Thumb_fin_dist_end_z" : Thumb_fin_dist_end_z,
        
        
       #Dedo índice 
      
        
        "Index_fin_meta_direction_x" : Index_fin_meta_direction_x,
        "Index_fin_meta_direction_y" : Index_fin_meta_direction_y,
        "Index_fin_meta_direction_z" : Index_fin_meta_direction_z,
        "Index_fin_prox_direction_x" : Index_fin_prox_direction_x,
        "Index_fin_prox_direction_y" : Index_fin_prox_direction_y,
        "Index_fin_prox_direction_z" : Index_fin_prox_direction_z,
        "Index_fin_inter_direction_x" : Index_fin_inter_direction_x,
        "Index_fin_inter_direction_y" : Index_fin_inter_direction_y,
        "Index_fin_inter_direction_z" : Index_fin_inter_direction_z,
        "Index_fin_dist_direction_x" : Index_fin_dist_direction_x,
        "Index_fin_dist_direction_y" : Index_fin_dist_direction_y,
        "Index_fin_dist_direction_z" : Index_fin_dist_direction_z,
        
        "Index_fin_meta_start_x" : Index_fin_meta_start_x,
        "Index_fin_meta_start_y" : Index_fin_meta_start_y,
        "Index_fin_meta_start_z" : Index_fin_meta_start_z,
        "Index_fin_meta_end_x" : Index_fin_meta_end_x,
        "Index_fin_meta_end_y" : Index_fin_meta_end_y,
        "Index_fin_meta_end_z" : Index_fin_meta_end_z,
        "Index_fin_prox_start_x" : Index_fin_prox_start_x,
        "Index_fin_prox_start_y" : Index_fin_prox_start_y,
        "Index_fin_prox_start_z" : Index_fin_prox_start_z,
        "Index_fin_prox_end_x" : Index_fin_prox_end_x,
        "Index_fin_prox_end_y" : Index_fin_prox_end_y,
        "Index_fin_prox_end_z" : Index_fin_prox_end_z,
        "Index_fin_inter_start_x" : Index_fin_inter_start_x,
        "Index_fin_inter_start_y" : Index_fin_inter_start_y,
        "Index_fin_inter_start_z" : Index_fin_inter_start_z,
        "Index_fin_inter_end_x" : Index_fin_inter_end_x,
        "Index_fin_inter_end_y" : Index_fin_inter_end_y,
        "Index_fin_inter_end_z" : Index_fin_inter_end_z,
        "Index_fin_dist_start_x" : Index_fin_dist_start_x,
        "Index_fin_dist_start_y" : Index_fin_dist_start_y,
        "Index_fin_dist_start_z" : Index_fin_dist_start_z,
        "Index_fin_dist_end_x" : Index_fin_dist_end_x,
        "Index_fin_dist_end_y" : Index_fin_dist_end_y,
        "Index_fin_dist_end_z" : Index_fin_dist_end_z,
        
        

        
        "Middle_x_basis_x": Middle_x_basis_x,
        "Middle_x_basis_y": Middle_x_basis_y,
        "Middle_x_basis_z": Middle_x_basis_z,
        
                
        "Middle_y_basis_x": Middle_y_basis_x,
        "Middle_y_basis_y": Middle_y_basis_y,
        "Middle_y_basis_z": Middle_y_basis_z,
        
                
        "Middle_z_basis_x": Middle_z_basis_x,
        "Middle_z_basis_y": Middle_z_basis_y,
        "Middle_z_basis_z": Middle_z_basis_z,
        
                
        "Middle_origin_x": Middle_origin_x,
        "Middle_origin_y": Middle_origin_y,
        "Middle_origin_z": Middle_origin_z,
       

        #Dedo medio
        
        "Middle_fin_meta_direction_x" : Middle_fin_meta_direction_x,
        "Middle_fin_meta_direction_y" : Middle_fin_meta_direction_y,
        "Middle_fin_meta_direction_z" : Middle_fin_meta_direction_z,
        "Middle_fin_prox_direction_x" : Middle_fin_prox_direction_x,
        "Middle_fin_prox_direction_y" : Middle_fin_prox_direction_y,
        "Middle_fin_prox_direction_z" : Middle_fin_prox_direction_z,
        "Middle_fin_inter_direction_x" : Middle_fin_inter_direction_x,
        "Middle_fin_inter_direction_y" : Middle_fin_inter_direction_y,
        "Middle_fin_inter_direction_z" : Middle_fin_inter_direction_z,
        "Middle_fin_dist_direction_x" : Middle_fin_dist_direction_x,
        "Middle_fin_dist_direction_y" : Middle_fin_dist_direction_y,
        "Middle_fin_dist_direction_z" : Middle_fin_dist_direction_z,
        
        "Middle_fin_meta_start_x" : Middle_fin_meta_start_x,
        "Middle_fin_meta_start_y" : Middle_fin_meta_start_y,
        "Middle_fin_meta_start_z" : Middle_fin_meta_start_z,
        "Middle_fin_meta_end_x" : Middle_fin_meta_end_x,
        "Middle_fin_meta_end_y" : Middle_fin_meta_end_y,
        "Middle_fin_meta_end_z" : Middle_fin_meta_end_z,
        "Middle_fin_prox_start_x" : Middle_fin_prox_start_x,
        "Middle_fin_prox_start_y" : Middle_fin_prox_start_y,
        "Middle_fin_prox_start_z" : Middle_fin_prox_start_z,
        "Middle_fin_prox_end_x" : Middle_fin_prox_end_x,
        "Middle_fin_prox_end_y" : Middle_fin_prox_end_y,
        "Middle_fin_prox_end_z" : Middle_fin_prox_end_z,
        "Middle_fin_inter_start_x" : Middle_fin_inter_start_x,
        "Middle_fin_inter_start_y" : Middle_fin_inter_start_y,
        "Middle_fin_inter_start_z" : Middle_fin_inter_start_z,
        "Middle_fin_inter_end_x" : Middle_fin_inter_end_x,
        "Middle_fin_inter_end_y" : Middle_fin_inter_end_y,
        "Middle_fin_inter_end_z" : Middle_fin_inter_end_z,
        "Middle_fin_dist_start_x" : Middle_fin_dist_start_x,
        "Middle_fin_dist_start_y" : Middle_fin_dist_start_y,
        "Middle_fin_dist_start_z" : Middle_fin_dist_start_z,
        "Middle_fin_dist_end_x" : Middle_fin_dist_end_x,
        "Middle_fin_dist_end_y" : Middle_fin_dist_end_y,
        "Middle_fin_dist_end_z" : Middle_fin_dist_end_z,
        
## dedo Anular
        "Ring_fin_meta_direction_x" : Ring_fin_meta_direction_x,
        "Ring_fin_meta_direction_y" : Ring_fin_meta_direction_y,
        "Ring_fin_meta_direction_z" : Ring_fin_meta_direction_z,
        "Ring_fin_prox_direction_x" : Ring_fin_prox_direction_x,
        "Ring_fin_prox_direction_y" : Ring_fin_prox_direction_y,
        "Ring_fin_prox_direction_z" : Ring_fin_prox_direction_z,
        "Ring_fin_inter_direction_x" : Ring_fin_inter_direction_x,
        "Ring_fin_inter_direction_y" : Ring_fin_inter_direction_y,
        "Ring_fin_inter_direction_z" : Ring_fin_inter_direction_z,
        "Ring_fin_dist_direction_x" : Ring_fin_dist_direction_x,
        "Ring_fin_dist_direction_y" : Ring_fin_dist_direction_y,
        "Ring_fin_dist_direction_z" : Ring_fin_dist_direction_z,
        
        "Ring_fin_meta_start_x" : Ring_fin_meta_start_x,
        "Ring_fin_meta_start_y" : Ring_fin_meta_start_y,
        "Ring_fin_meta_start_z" : Ring_fin_meta_start_z,
        "Ring_fin_meta_end_x" : Ring_fin_meta_end_x,
        "Ring_fin_meta_end_y" : Ring_fin_meta_end_y,
        "Ring_fin_meta_end_z" : Ring_fin_meta_end_z,
        "Ring_fin_prox_start_x" : Ring_fin_prox_start_x,
        "Ring_fin_prox_start_y" : Ring_fin_prox_start_y,
        "Ring_fin_prox_start_z" : Ring_fin_prox_start_z,
        "Ring_fin_prox_end_x" : Ring_fin_prox_end_x,
        "Ring_fin_prox_end_y" : Ring_fin_prox_end_y,
        "Ring_fin_prox_end_z" : Ring_fin_prox_end_z,
        "Ring_fin_inter_start_x" : Ring_fin_inter_start_x,
        "Ring_fin_inter_start_y" : Ring_fin_inter_start_y,
        "Ring_fin_inter_start_z" : Ring_fin_inter_start_z,
        "Ring_fin_inter_end_x" : Ring_fin_inter_end_x,
        "Ring_fin_inter_end_y" : Ring_fin_inter_end_y,
        "Ring_fin_inter_end_z" : Ring_fin_inter_end_z,
        "Ring_fin_dist_start_x" : Ring_fin_dist_start_x,
        "Ring_fin_dist_start_y" : Ring_fin_dist_start_y,
        "Ring_fin_dist_start_z" : Ring_fin_dist_start_z,
        "Ring_fin_dist_end_x" : Ring_fin_dist_end_x,
        "Ring_fin_dist_end_y" : Ring_fin_dist_end_y,
        "Ring_fin_dist_end_z" : Ring_fin_dist_end_z,
        
## Dedo meñique 
        
        "Pinky_fin_meta_direction_x" : Pinky_fin_meta_direction_x,
        "Pinky_fin_meta_direction_y" : Pinky_fin_meta_direction_y,
        "Pinky_fin_meta_direction_z" : Pinky_fin_meta_direction_z,
        "Pinky_fin_prox_direction_x" : Pinky_fin_prox_direction_x,
        "Pinky_fin_prox_direction_y" : Pinky_fin_prox_direction_y,
        "Pinky_fin_prox_direction_z" : Pinky_fin_prox_direction_z,
        "Pinky_fin_inter_direction_x" : Pinky_fin_inter_direction_x,
        "Pinky_fin_inter_direction_y" : Pinky_fin_inter_direction_y,
        "Pinky_fin_inter_direction_z" : Pinky_fin_inter_direction_z,
        "Pinky_fin_dist_direction_x" : Pinky_fin_dist_direction_x,
        "Pinky_fin_dist_direction_y" : Pinky_fin_dist_direction_y,
        "Pinky_fin_dist_direction_z" : Pinky_fin_dist_direction_z,
        
        "Pinky_fin_meta_start_x" : Pinky_fin_meta_start_x,
        "Pinky_fin_meta_start_y" : Pinky_fin_meta_start_y,
        "Pinky_fin_meta_start_z" : Pinky_fin_meta_start_z,
        "Pinky_fin_meta_end_x" : Pinky_fin_meta_end_x,
        "Pinky_fin_meta_end_y" : Pinky_fin_meta_end_y,
        "Pinky_fin_meta_end_z" : Pinky_fin_meta_end_z,
        "Pinky_fin_prox_start_x" : Pinky_fin_prox_start_x,
        "Pinky_fin_prox_start_y" : Pinky_fin_prox_start_y,
        "Pinky_fin_prox_start_z" : Pinky_fin_prox_start_z,
        "Pinky_fin_prox_end_x" : Pinky_fin_prox_end_x,
        "Pinky_fin_prox_end_y" : Pinky_fin_prox_end_y,
        "Pinky_fin_prox_end_z" : Pinky_fin_prox_end_z,
        "Pinky_fin_inter_start_x" : Pinky_fin_inter_start_x,
        "Pinky_fin_inter_start_y" : Pinky_fin_inter_start_y,
        "Pinky_fin_inter_start_z" : Pinky_fin_inter_start_z,
        "Pinky_fin_inter_end_x" : Pinky_fin_inter_end_x,
        "Pinky_fin_inter_end_y" : Pinky_fin_inter_end_y,
        "Pinky_fin_inter_end_z" : Pinky_fin_inter_end_z,
        "Pinky_fin_dist_start_x" : Pinky_fin_dist_start_x,
        "Pinky_fin_dist_start_y" : Pinky_fin_dist_start_y,
        "Pinky_fin_dist_start_z" : Pinky_fin_dist_start_z,
        "Pinky_fin_dist_end_x" : Pinky_fin_dist_end_x,
        "Pinky_fin_dist_end_y" : Pinky_fin_dist_end_y,
        "Pinky_fin_dist_end_z" : Pinky_fin_dist_end_z,
        
# Tiempo y etiqueta
        "Tiempo" : Tiempo,
        "label" : label_list,
    })
    df.to_csv("./{0}_{1}.csv".format(current, str(label)))

def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)
        data_save_pandas()

if __name__ == "__main__":
    main()

