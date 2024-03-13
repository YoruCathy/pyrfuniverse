# testing_object_data

## 1. Basic Features

- Test and print object data information.

## 2. Implementation Process

### 2.1 Initialize the Environment

```python
env = RFUniverseBaseEnv(assets=["Rigidbody_Box", "franka_panda"])
```

### 2.2 Test and Print Object Data Information

```python
box = env.InstanceObject(name="Rigidbody_Box", id=123456, attr_type=attr.RigidbodyAttr)
box.SetTransform(position=[0, 1, 0])
env.step(5)
for key in box.data:
    print(key)
    print(box.data[key])

robot = env.InstanceObject(
    name="franka_panda", id=789789, attr_type=attr.ControllerAttr
)
robot.SetTransform(position=[1, 0, 0])
env.step()
for key in robot.data:
    print(key)
    print(robot.data[key])
env.close()
```

- `InstanceObject`: Instantiate an object from assets, i.e., create an object in the virtual scene.
- `SetTransform`: Set the position and orientation of the object.

Below is the information printed by the program:
```bash
name
Rigidbody_Box
position
[0.0, 0.9411399960517883, 0.0]
rotation
[-0.0, 0.0, 0.0]
quaternion
[0.0, 0.0, 0.0, 1.0]
local_position
[0.0, 0.9411399960517883, 0.0]
local_rotation
[-0.0, 0.0, 0.0]
local_quaternion
[0.0, 0.0, 0.0, 1.0]
local_to_world_matrix
[[1.      0.      0.      0.     ]
 [0.      1.      0.      0.94114]
 [0.      0.      1.      0.     ]
 [0.      0.      0.      1.     ]]
move_done
True
rotate_done
True
velocity
[0.0, -0.9810000061988831, 0.0]
angular_vel
[0.0, 0.0, 0.0]
name
franka_panda
position
[1.0, 0.0, 0.0]
rotation
[-0.0, 0.0, 0.0]
quaternion
[0.0, 0.0, 0.0, 1.0]
local_position
[1.0, 0.0, 0.0]
local_rotation
[-0.0, 0.0, 0.0]
local_quaternion
[0.0, 0.0, 0.0, 1.0]
local_to_world_matrix
[[1. 0. 0. 1.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
move_done
True
rotate_done
True
number_of_joints
9
names
['panda_link0', 'panda_joint1', 'panda_joint2', 'panda_joint3', 'panda_joint4', 'panda_joint5', 'panda_joint6', 'panda_joint7', 'panda_joint8']
types
['FixedJoint', 'RevoluteJoint', 'RevoluteJoint', 'RevoluteJoint', 'RevoluteJoint', 'RevoluteJoint', 'RevoluteJoint', 'RevoluteJoint', 'FixedJoint']
positions
[[1.0, 0.0, 0.0], [0.9999999403953552, 0.3330000042915344, 0.0], [0.9999999403953552, 0.3330000042915344, 0.0], [1.0, 0.6490004062652588, 0.0], [1.0, 0.6490005850791931, 0.08250003308057785], [0.9999999403953552, 1.0330020189285278, 7.450580596923828e-09], [0.9999999403953552, 1.0330030918121338, 7.450580596923828e-09], [0.9999999403953552, 1.0330041646957397, 0.08800002932548523], [1.0, 0.9260044097900391, 0.08800002932548523]]
rotations
[[-0.0, 0.0, 0.0], [-0.0, 0.0, 0.0], [-0.0, -0.0, 90.0], [-0.0, 0.0, 0.0], [-0.0, 0.0, 270.0], [-0.0, 0.0, 0.0], [-0.0, 0.0, 270.0], [-0.0, 0.0, 180.0], [-0.0, 0.0, 180.0]]
quaternions
[[-0.0, -0.0, -0.0, 1.0], [-0.0, -0.0, -0.0, 1.0], [-0.0, -0.0, 0.7071068286895752, 0.7071068286895752], [-0.0, -0.0, -0.0, 1.0000001192092896], [-0.0, -0.0, -0.70710688829422, 0.70710688829422], [-0.0, -0.0, -0.0, 1.000000238418579], [-0.0, -0.0, -0.7071070075035095, 0.7071070075035095], [-0.0, -0.0, -1.0000003576278687, 0.0], [-0.0, -0.0, -1.0000003576278687, 0.0]]
local_positions
[[0.0, 0.0, 0.0], [-5.960464477539063e-08, 0.3330000042915344, 0.0], [0.0, 0.0, 0.0], [0.316000372171402, -8.940696716308594e-08, 0.0], [-2.8421716206667585e-14, 1.7881400538044545e-07, 0.08250003308057785], [-0.38400137424468994, -1.4901161193847656e-07, -0.08250002562999725], [1.1368686482667034e-13, 1.0728839470175444e-06, 0.0], [-1.0728840607043821e-06, 0.0, 0.08800002187490463], [-1.3411049337719305e-07, 0.10699975490570068, 0.0]]
local_rotations
[[-0.0, 0.0, 0.0], [-0.0, 0.0, 0.0], [-0.0, -0.0, 90.0], [-0.0, 0.0, 270.0], [-0.0, 0.0, 270.0], [-0.0, -0.0, 90.0], [-0.0, 0.0, 270.0], [-0.0, 0.0, 270.0], [-0.0, 0.0, 0.0]]
local_quaternions
[[-0.0, -0.0, -0.0, 1.0], [-0.0, -0.0, -0.0, 1.0], [-0.0, -0.0, 0.7071068286895752, 0.7071068286895752], [-0.0, -0.0, -0.7071068286895752, 0.7071068286895752], [-0.0, -0.0, -0.7071068286895752, 0.7071068286895752], [-0.0, -0.0, 0.7071068286895752, 0.7071068286895752], [-0.0, -0.0, -0.7071068286895752, 0.7071068286895752], [-0.0, -0.0, -0.7071068286895752, 0.7071068286895752], [-0.0, -0.0, -0.0, 1.0]]
velocities
[[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
angular_velocity
[[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
number_of_moveable_joints
7
joint_positions
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
joint_velocities
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
joint_accelerations
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
joint_force
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
joint_lower_limit
[-170.00230407714844, -105.000244140625, -170.00230407714844, -180.00042724609375, -170.00230407714844, -5.001921653747559, -170.00230407714844]
joint_upper_limit
[170.00230407714844, 105.000244140625, 170.00230407714844, 0.0, 170.00230407714844, 219.0016632080078, 170.00230407714844]
joint_stiffness
[100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 100000.0]
joint_damping
[9000.0, 9000.0, 9000.0, 9000.0, 9000.0, 9000.0, 9000.0]
```