#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Ozer Ozkahraman (ozero@kth.se)



CURRENT_PLAN_ACTION = 'current_plan_action'
LAST_PLAN_ACTION_FEEDBACK = 'last_plan_action_feedback'

##########################
# ROS TOPICS
##########################
# DO NOT PUT SLASHES BEFORE TOPIC NAMES, that puts them in 'root' in ros's eyes.
PLAN_TOPIC = 'plan_db'
ESTIMATED_STATE_TOPIC = 'estimated_state'
PLAN_CONTROL_STATE_TOPIC = 'plan_control_state'
ABORT_TOPIC = 'abort'
DEPTH_TOPIC = 'ctrl/depth_feedback'
ALTITUDE_TOPIC = 'ctrl/altitude_feedback'

BASE_LINK = '/sam/base_link'


######################
# BLACKBOARD VARIABLES
######################
ABORT_BB = 'abort'

DEPTH_BB = 'depth'
ALTITUDE_BB = 'altitude'

MISSION_PLAN_STR_BB = 'plan_str'
MISSION_PLAN_OBJ_BB = 'misison_plan'

UTM_BAND_BB = 'utm_band'
UTM_ZONE_BB = 'utm_zone'

WORLD_ROT_BB = 'world_rot'
WORLD_TRANS_BB = 'world_trans'





########################
# DEFAULT VALUES
########################
SAM_MAX_DEPTH = 5
SAM_MIN_ALTITUDE = 2

MINIMUM_PLAN_STR_LEN = 135 # somehow Chris found this number, i'll reuse this

# these are from croatia, biograd coast
DEFAULT_UTM_ZONE = 33
DEFAULT_UTM_BAND = 'T'
