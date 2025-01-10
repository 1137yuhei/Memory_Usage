import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    memory_usage_publisher = launch_ros.actions.Node(
        package='memory_usage',      #パッケージの名前を指定
        executable='memory_usage_publisher',  #実行するファイルの指定
        )
    listener = launch_ros.actions.Node(
        package='memory_usage',
        executable='listener',
        output='screen'        #ログを端末に出すための設定
        )
    return launch.LaunchDescription([memory_usage_publisher, listener])
