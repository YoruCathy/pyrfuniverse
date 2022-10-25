import os
import numpy as np
import pandas as pd
from pyrfuniverse.envs.base_env import RFUniverseBaseEnv

mesh_path = '../Mesh/drink1/drink1.obj'
pose_path = '../Mesh/drink1/grasps_rfu.csv'

data = pd.read_csv(pose_path, usecols=['x', 'y', 'z', 'qx', 'qy', 'qz', 'qw'])
data = data.to_numpy()
positions = data[:, 0:3].reshape(-1).tolist()
quaternions = data[:, 3:7].reshape(-1).tolist()

env = RFUniverseBaseEnv(
    # executable_file='/home/yanbing/Project/rfuniverse/rfuniverse/Build/usr/local/RFUniverse/RFUniverse.x86_64',
)

env.asset_channel.set_action(
    'InstanceObject',
    id=123123,
    name='GraspSim'
)
env.instance_channel.set_action(
    'ShowGraspPose',
    id=123123,
    mesh=os.path.abspath(mesh_path),
    gripper='SimpleFrankaGripper',
    positions=positions,
    quaternions=quaternions,
)
while True:
    env._step()
