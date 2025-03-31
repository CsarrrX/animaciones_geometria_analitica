from manim import *

class LinearInequalities(Scene):
    def construct(self):
        # Crear los ejes (gráfica más pequeña con escala)
        axes = Axes(
            x_range=[0, 100, 10],
            y_range=[0, 100, 10],
            axis_config={"include_numbers": True},
        ).scale(0.8)  # Escalar la gráfica al 80% de su tamaño original
        self.play(Create(axes, run_time=3))  # Hacer que la creación de los ejes sea más lenta

        # Líneas límite
        line1 = axes.plot(lambda x: x / 1.25, x_range=[0, 100], color=BLUE)  # x ≥ 1.25y
        line2 = axes.plot(lambda x: (3600 - 40 * x) / 25, x_range=[0, 90], color=RED)  # 40x + 25y ≥ 3600

        # Etiquetas de líneas (hacerlas más pequeñas y mover una hacia abajo)
        label1 = axes.get_graph_label(line1, "x = 1.25y", direction=UP).scale(0.7)  # Reducir tamaño
        label2 = axes.get_graph_label(line2, "40x + 25y = 3600", direction=DOWN).scale(0.7)  # Reducir tamaño y mover hacia abajo

        self.play(Create(line1, run_time=3), Create(line2, run_time=3))  # Hacer que las líneas se dibujen más lentamente
        self.play(Write(label1, run_time=2), Write(label2, run_time=2))  # Hacer que las etiquetas aparezcan más lentamente

        # Sombrear región factible (área óptima a la derecha de las líneas)
        region = Polygon(
            axes.coords_to_point(60, 48),       # Punto de intersección (60, 48)
            axes.coords_to_point(100, 80),      # Punto en la primera desigualdad extendida
            axes.coords_to_point(100, 0),       # Punto en el eje X (100, 0)
            axes.coords_to_point(90, 0),        # Punto en la primera desigualdad (90, 0)
            fill_opacity=0.2,
            color=GREEN,
        )
        self.play(FadeIn(region, run_time=4))  # Hacer que el área óptima aparezca más lentamente

        # Mostrar el punto de intersección (60, 48)
        intersection = Dot(axes.coords_to_point(60, 48), color=YELLOW)
        intersection_label = MathTex("(60, 48)").scale(0.5).next_to(intersection, UP)
        self.play(FadeIn(intersection, run_time=2), Write(intersection_label, run_time=2))  # Hacer que el punto y la etiqueta aparezcan más lentamente

        # Resaltar el punto (90, 0)
        point_90_0 = Dot(axes.coords_to_point(90, 0), color=YELLOW)
        point_90_0_label = MathTex("(90, 0)").scale(0.5).next_to(point_90_0, UP)
        self.play(FadeIn(point_90_0, run_time=2), Write(point_90_0_label, run_time=2))  # Hacer que el punto y la etiqueta aparezcan más lentamente

        self.wait(3)  # Pausa final para extender la duración del video