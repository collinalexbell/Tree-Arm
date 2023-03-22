from joint import Joint

def move_joint_to_pos(joint: Joint, position: float, millis: int):
    cmd = {}
    cmd["joint"] = joint.id(),
    cmd["position"] = position
    cmd["millis"] = millis
