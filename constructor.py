

class Constructor:
    def __init__(self):
        pass

    def learn(self, data):
        camera_paras, solid_scene_paras, soft_scene_paras = self.scene_model(data)
        self.camera.set(camera_paras)
        self.solid_scene.set(solid_scene_paras)
        self.soft__scene.set(soft_scene_paras)
        synthesis = self.renderer(self.camera, self.solid_scene, self.soft_scene)
        loss = self.criterion(synthesis, data)
        return synthesis, loss

