import WRSUtil
WRSUtil.loadProject(
    "MultiSceneViews", "TS3", [ "AGXSimulator", "AISTSimulator" ], "Quadcopter",
    enableMulticopterSimulation = True, enableVisionSimulation = True, remoteType = "ROS")
