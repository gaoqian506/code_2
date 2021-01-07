
class Renderer:
    def __init__(self):
        pass

    def forward(self, camera, solid_scene, soft_scene):
        synthesis = 0.0
        for s in sample_count:
            rays = camera.sample()
            colors = 0.0
            first_hit = solid_scene.hit(rays)
            first_ts, points, normals, materials = first_hit
            for b in bounce_count:
                colors += color(points, normals, materials)
                rays = bound(points, normals, materials)
                _, points, normals, materials = solid_scene.hit(rays)
            synthesis += colors

        for s in sample_count:
            rays = camera.sample()
            ts = 0.0

            while all ts < first_ts:



        return synthesis




