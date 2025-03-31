from manim import *
import numpy as np

class LinearProgrammingScene(Scene):
    def construct(self):
        # 1. Título
        title = Text("Linear Programming").scale(1.2)
        self.play(Write(title))
        self.wait(1)  # Ajusta este tiempo si es necesario
        self.play(title.animate.to_edge(UP))
        
        # 2. Definición de maximización y minimización
        definition = Text("Maximize or Minimize a function with constraints").scale(0.8)
        self.play(Write(definition))
        self.wait(2)  # Ajusta el tiempo según el audio
        self.play(FadeOut(definition))
        
        # 3. Graficar función seno (más pequeña)
        axes = Axes(
            x_range=[-PI, PI, 1],
            y_range=[-1.5, 1.5, 0.5],
            axis_config={"color": WHITE}
        ).scale(0.7)  # Escalar los ejes para hacerlos más pequeños
        sine_graph = axes.plot(lambda x: np.sin(x), color=YELLOW)
        moving_dot = Dot(axes.coords_to_point(PI/2, np.sin(PI/2)), color=RED)
        
        self.play(Create(axes), Create(sine_graph))
        self.wait(1)
        self.play(FadeIn(moving_dot))
        
        # Movimiento del punto entre el máximo local y el mínimo local
        self.play(moving_dot.animate.move_to(axes.coords_to_point(-PI/2, np.sin(-PI/2))), run_time=4, rate_func=smooth)
        self.wait(1)  # Momento en que mencionan "mínimo"
        self.play(FadeOut(moving_dot), FadeOut(axes), FadeOut(sine_graph))  # Desaparecer gráfica y punto
        
        # 4. Mostrar ecuación z = f(x, y)
        equation = MathTex("z = f(x, y)")
        self.play(Write(equation))
        self.wait(2)  # Ajustar según el audio
        self.play(FadeOut(equation))
        
        # 5. Mostrar "where z depends on x and y"
        final_text = Text("where z depends on x and y").scale(0.8)
        self.play(Write(final_text))
        self.wait(1)  # Mostrar el texto por 1 segundo
        self.play(FadeOut(final_text))  # Limpiar todo al final



























