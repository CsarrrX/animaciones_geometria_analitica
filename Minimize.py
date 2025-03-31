from manim import *

class MinimizationGraph(Scene):
    def construct(self):
        # Definir el plano cartesiano
        plane = NumberPlane(
            x_range=[-1, 6], y_range=[-1, 6],
            axis_config={"include_numbers": True}
        )
        self.play(Create(plane))
        
        # Restricciones
        r1 = Line(start=plane.c2p(4, 0), end=plane.c2p(0, 4), color=BLUE)
        r2 = Line(start=plane.c2p(0, 0), end=plane.c2p(4, 0), color=BLUE)
        r3 = Line(start=plane.c2p(0, 0), end=plane.c2p(0, 4), color=BLUE)
        
        # Región factible (triángulo)
        region = Polygon(
            plane.c2p(0, 0), plane.c2p(4, 0), plane.c2p(0, 4),
            color=GREEN, fill_opacity=0.3
        )
        
        # Función objetivo Z = x + 2y
        objective_line = Line(
            start=plane.c2p(3, 0), end=plane.c2p(0, 1.5), color=RED
        )
        
        # Texto explicativo
        text = Text("Minimizando Z = x + 2y", font_size=24).to_edge(UP)
        
        self.play(Create(r1), Create(r2), Create(r3))
        self.play(FadeIn(region))
        self.play(Write(text))
        
        # Animar la línea de nivel moviéndose en dirección de minimización
        moving_line = objective_line.copy()
        self.play(Create(moving_line))
        self.wait(1)
        self.play(moving_line.animate.shift(DOWN * 2.5 + LEFT * 1.5))
        
        # Punto óptimo (mínimo en (0,0))
        min_point = Dot(plane.c2p(0, 0), color=YELLOW)
        min_text = Text("Mínimo", font_size=20).next_to(min_point, DOWN+LEFT)
        self.play(FadeIn(min_point), Write(min_text))
        
        self.wait(2)
