from panda3d.core import Point3, AmbientLight, DirectionalLight, Texture
from direct.showbase.ShowBase import ShowBase
from math import sin, cos, pi
import random

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setup_scene()
        self.setup_lighting()
        self.setup_camera()
        self.create_large_world()

    def setup_scene(self):
        """Cargar y configurar la escena base."""
        self.scene = self.loader.loadModel("models/environment")
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

    def setup_lighting(self):
        """Configurar la iluminación de la escena."""
        # Luz ambiental
        ambient_light = AmbientLight('ambient_light')
        ambient_light.set_color((0.3, 0.3, 0.3, 1))  # Luz suave
        ambient_light_np = self.render.attach_new_node(ambient_light)
        self.render.set_light(ambient_light_np)

        # Luz direccional
        directional_light = DirectionalLight('directional_light')
        directional_light.set_color((1, 1, 1, 1))  # Luz blanca
        directional_light_np = self.render.attach_new_node(directional_light)
        directional_light_np.set_hpr(0, -60, 0)  # Dirección de la luz
        self.render.set_light(directional_light_np)

    def setup_camera(self):
        """Configurar la posición de la cámara."""
        self.camera.set_pos(0, -30, 10)  # Posicionar la cámara
        self.camera.look_at(Point3(0, 0, 0))  # Mirar hacia el centro

    def create_large_world(self):
        """Crear un mundo más grande con varios elementos."""
        # Crear un plano grande
        terrain = self.loader.loadModel("models/plane")
        terrain.reparentTo(self.render)
        terrain.setScale(100, 100, 1)  # Escalar el plano
        terrain.setPos(0, 0, 0)  # Posicionar el plano

        # Texturizar el terreno
        texture = self.loader.loadTexture("textures/grass.jpg")  # Asegúrate de tener una textura de hierba
        terrain.setTexture(texture)

        # Crear árboles o elementos decorativos
        for i in range(50):
            tree = self.loader.loadModel("models/tree")  # Cambia por tu modelo de árbol
            tree.reparentTo(self.render)
            tree.setScale(0.5, 0.5, 0.5)  # Escalar el árbol
            x = random.uniform(-50, 50)  # Posiciones aleatorias
            y = random.uniform(-50, 50)
            z = 0  # Altura del árbol
            tree.setPos(x, y, z)

app = MyApp()
app.run()
