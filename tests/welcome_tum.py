import compas_rrc as rrc

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Print text on FlexPenant
    abb.send(rrc.PrintText('Welcome TUM to COMPAS_RRC ;)'))

    # Define robot joint positions
    robot_pos_joints_park = [-90.0, -30.0, 70.0, 0.0, 50.0, 0.0]
    robot_pos_joints_start = [-135.0, 30.0, 20.0, 0.0, 30.0, 0.0]


    # Set speed [mm/s]
    speed = 30
    external_axis_dummy = []
    # Move to start position
    done = abb.send_and_wait(rrc.MoveToJoints(robot_pos_joints_start, external_axis_dummy, speed, rrc.Zone.Z0))

    # Move to park position
    done = abb.send_and_wait(rrc.MoveToJoints(robot_pos_joints_park, external_axis_dummy, speed, rrc.Zone.Z0))

    # Print feedback
    print('Feedback = ', done)

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
