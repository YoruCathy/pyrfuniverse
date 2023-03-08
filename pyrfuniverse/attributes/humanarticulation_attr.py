import pyrfuniverse.attributes as attr
from pyrfuniverse.side_channel.side_channel import (
    IncomingMessage,
    OutgoingMessage,
)
import pyrfuniverse.utils.rfuniverse_utility as utility

def parse_message(msg: IncomingMessage) -> dict:
    this_object_data = attr.base_attr.parse_message(msg)
    return this_object_data

# bone name list:
# Pelvis
# Spine1
# Spine2
# Spine3
# LeftShoulder
# LeftUpperArm
# LeftLowerArm
# LeftHand
# RightShoulder
# RightUpperArm
# RightLowerArm
# RightHand
# LeftUpperLeg
# LeftLowerLeg
# LeftFoot
# LeftToes
# RightUpperLeg
# RightLowerLeg
# RightFoot
# RightToes
# Neck
# Head
# LeftEye
# RightEye
# Jaw
# LeftThumb1
# LeftThumb2
# LeftThumb3
# LeftIndex1
# LeftIndex2
# LeftIndex3
# LeftMiddle1
# LeftMiddle2
# LeftMiddle3
# LeftRing1
# LeftRing2
# LeftRing3
# LeftPinky1
# LeftPinky2
# LeftPinky3
# RightThumb1
# RightThumb2
# RightThumb3
# RightIndex1
# RightIndex2
# RightIndex3
# RightMiddle1
# RightMiddle2
# RightMiddle3
# RightRing1
# RightRing2
# RightRing3
# RightPinky1
# RightPinky2
# RightPinky3

def SetNameBonePosition(kwargs: dict) -> OutgoingMessage:
    compulsory_params = ['id', 'bone_name', 'bone_position']
    optional_params = []
    utility.CheckKwargs(kwargs, compulsory_params)

    msg = OutgoingMessage()

    msg.write_int32(kwargs['id'])
    msg.write_string('SetNameBonePosition')
    msg.write_string(kwargs['bone_name'])
    msg.write_float32(kwargs['bone_position'])

    return msg

def SetNameBonePositionDirectly(kwargs: dict) -> OutgoingMessage:
    compulsory_params = ['id', 'bone_name', 'bone_position']
    optional_params = []
    utility.CheckKwargs(kwargs, compulsory_params)

    msg = OutgoingMessage()

    msg.write_int32(kwargs['id'])
    msg.write_string('SetNameBonePositionDirectly')
    msg.write_string(kwargs['bone_name'])
    msg.write_float32(kwargs['bone_position'])

    return msg

def SaveArticulationBoneData(kwargs: dict) -> OutgoingMessage:
    compulsory_params = ['id', 'path']
    optional_params = []
    utility.CheckKwargs(kwargs, compulsory_params)

    msg = OutgoingMessage()

    msg.write_int32(kwargs['id'])
    msg.write_string('SaveArticulationBoneData')
    msg.write_string(kwargs['path'])

    return msg
