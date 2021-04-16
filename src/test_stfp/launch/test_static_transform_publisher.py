"""A file to test the number of static_transform_publishers being created"""

from launch import LaunchDescription
from launch_ros.actions import Node

def get_nodes(num_nodes):
    nodes = []
    for i in range(num_nodes):
        tf_args = [ '0.0', '0.0', '0.0',
                    '0.0', '0.0', '0.0', '1.0',
                    'frame_{}'.format(i), 'frame_{}'.format(i+1)
                  ]
        nodes.append(
            Node(
                package='tf2_ros',
                executable='static_transform_publisher',
                name='tf_publisher_{}_to_{}'.format(i, i+1),
                arguments=tf_args
            )
        )

    return nodes

def generate_launch_description():
    return LaunchDescription(get_nodes(101))

