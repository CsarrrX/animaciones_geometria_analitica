from manim import *
import numpy as np

class LinearProgrammingExplanation(Scene):
    def construct(self):
        # 1. Título principal y traslado a la parte superior
        title = Text("Solving a Linear Programming Problem").scale(1.1)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # 2. Función objetivo
        obj_text = Text("Objective Function: z = f(x, y)").scale(0.8)
        obj_text.next_to(title, DOWN, buff=MED_SMALL_BUFF)
        self.play(Write(obj_text))
        self.wait(2)
        self.play(FadeOut(obj_text))
        
        # 3. Restricciones: físicas (estructurales) y formales (de rango)
        restrictions = VGroup(
            Text("Physical Restrictions (e.g., resource limits)").scale(0.75),
            Text("Formal Restrictions (e.g., variable bounds)").scale(0.75)
        ).arrange(DOWN, aligned_edge=LEFT)
        restrictions.next_to(title, DOWN, buff=MED_SMALL_BUFF)
        self.play(Write(restrictions))
        self.wait(5)
        self.play(FadeOut(restrictions))
        
        # 4. Mencionar los métodos principales
        methods = Text("Main Methods: Graphical Method & Simplex Method", font_size=36)
        methods.next_to(title, DOWN, buff=MED_SMALL_BUFF)
        self.play(Write(methods))
        self.wait(2)
        self.play(FadeOut(methods))
        
        # 5. Explicación visual: ejemplo geométrico sencillo de la región factible
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 6, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_numbers": True},
        ).scale(0.8)  # Escalar los ejes para hacerlos más pequeños
        axes.to_edge(DOWN, buff=1)  # Reposicionar la gráfica hacia abajo
        self.play(Create(axes))
        
        # Dibujar las restricciones lineales simples: x + y <= 6, x >= 1, y >= 1
        line1 = axes.plot(lambda x: 6 - x)
        line1.set_color(BLUE)
        vertical = Line(axes.coords_to_point(1, 0), axes.coords_to_point(1, 6))
        vertical.set_color(GREEN)
        horizontal = Line(axes.coords_to_point(0, 1), axes.coords_to_point(6, 1))
        horizontal.set_color(GREEN)
        
        self.play(Create(line1), Create(vertical), Create(horizontal))
        self.wait(1)
        
        # Sombrear la región factible (triangular en este ejemplo)
        feasible_region = Polygon(
            axes.coords_to_point(1, 1),
            axes.coords_to_point(1, 5),  # intersección de x=1 y x+y=6 => y=5
            axes.coords_to_point(5, 1),  # intersección de y=1 y x+y=6 => x=5
            color=YELLOW,
            fill_color=YELLOW, fill_opacity=0.3
        )
        self.play(FadeIn(feasible_region, shift=DOWN))
        self.wait(2)
        
        # 6. Ejemplo de función objetivo en la región factible
        # Función objetivo: Maximizar z = 3x + 2y
        # Se representa con una línea que se traslada paralelamente para simular la optimización.
        obj_line_initial = axes.plot(lambda x: (3/2)*x - 1)  # Línea inicial más abajo
        obj_line_initial.set_color(RED)
        obj_line_final = axes.plot(lambda x: (3/2)*x + 4)  # Línea final más arriba
        obj_line_final.set_color(RED)
        
        self.play(Create(obj_line_initial))
        self.wait(1)
        self.play(Transform(obj_line_initial, obj_line_final), run_time=5)  # Mover la línea más lentamente
        self.wait(2)
        
        # 7. Conclusión: desvanecer todos los elementos
        self.play(
            FadeOut(obj_line_initial), 
            FadeOut(feasible_region), 
            FadeOut(line1),
            FadeOut(vertical), 
            FadeOut(horizontal), 
            FadeOut(axes)
        )
        self.wait(2)
