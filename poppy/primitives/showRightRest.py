#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import time

import pypot.primitive

class ShowRightRestBehave(pypot.primitive.Primitive):
    def run(self):
        poppy = self.robot

        for m in poppy.arms :
            m.compliant = False
        """
        poppy.r_shoulder_y.moving_speed = abs(-70 - poppy.r_shoulder_y.present_position)
        poppy.r_shoulder_x.moving_speed = abs(-35 - poppy.r_shoulder_x.present_position)
        poppy.r_arm_z.moving_speed = abs(-35 - poppy.r_arm_z.present_position)
        poppy.r_elbow_y.moving_speed = abs(80 - poppy.r_elbow_y.present_position)


        poppy.l_shoulder_y.moving_speed = abs(0 - poppy.l_shoulder_y.present_position)
        poppy.l_shoulder_x.moving_speed = abs(10 - poppy.l_shoulder_x.present_position)
        poppy.l_arm_z.moving_speed = abs(-35 - poppy.l_arm_z.present_position)
        poppy.l_elbow_y.moving_speed = abs(5 - poppy.l_elbow_y.present_position)

        poppy.r_shoulder_y.goal_position = -70
        poppy.r_shoulder_x.goal_position = -35
        poppy.r_arm_z.goal_position = -35
        poppy.r_elbow_y.goal_position = 80

        poppy.l_shoulder_y.goal_position = 0
        poppy.l_shoulder_x.goal_position = 10
        poppy.l_arm_z.goal_position = -35
        poppy.l_elbow_y.goal_position = 5


        """
        poppy.r_shoulder_y.goto_position(-70, 1, wait=False)
        poppy.r_shoulder_x.goto_position(-40, 1, wait=False)
        poppy.r_arm_z.goto_position(-35, 1, wait=False)
        poppy.r_elbow_y.goto_position(80, 1, wait=False)

        poppy.l_shoulder_y.goto_position(0, 1, wait=False)
        poppy.l_shoulder_x.goto_position(10, 1, wait=False)
        poppy.l_arm_z.goto_position(-35, 1, wait=False)
        poppy.l_elbow_y.goto_position(0, 1, wait=True)