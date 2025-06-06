import genesis as gs

gs.init()

scene = gs.Scene(
    show_viewer=True,
    viewer_options=gs.options.ViewerOptions(
        res=(1280, 960),
        camera_pos=(3.5, 0.0, 2.5),
        camera_lookat=(0.0, 0.0, 0.5),
        camera_fov=40,
        max_FPS=60,
    ),
    vis_options=gs.options.VisOptions(
        show_world_frame=True,
        world_frame_size=1.0,
        show_link_frame=False,
        show_cameras=False,
        plane_reflection=True,
        ambient_light=(0.1, 0.1, 0.1),
    ),
)

plane = scene.add_entity(
    # gs.morphs.Plane(),
    gs.morphs.URDF(file="urdf/plane/plane.urdf", fixed=True)
)

turtlebot = scene.add_entity(
    gs.morphs.URDF(file="robot_models/turtlebot3/urdf/turtlebot3_waffle_pi.urdf"),
)

wheel_joints = ["wheel_left_joint", "wheel_right_joint"]
wheel_idxs = [turtlebot.get_joint(name).dof_idx_local for name in wheel_joints]


scene.build()

# render rgb, depth, segmentation, normal
# rgb, depth, segmentation, normal = cam.render(rgb=True, depth=True, segmentation=True, normal=True)

# cam.start_recording()
import numpy as np

for i in range(12000):
    turtlebot.control_dofs_velocity(np.array([5.0, 5.0]), wheel_idxs)
    forces = turtlebot.get_dofs_control_force(wheel_idxs)
    print(forces)
    
    scene.step()
    
    # cam.render()
# cam.stop_recording(save_to_filename="video.mp4", fps=60)
