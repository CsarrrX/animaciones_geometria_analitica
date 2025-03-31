from manim import *

class FeasibleRegionTriangle(Scene):
    def construct(self):
        # Title
        title = Text("GRAPHIC METHOD", font_size=60)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Create smaller axes without arrow tips
        axes = Axes(
            x_range=[0, 8, 1],
            y_range=[0, 8, 1],
            x_length=4,  # Smaller x-axis length
            y_length=4,  # Smaller y-axis length
            axis_config={"include_numbers": True},
            tips=False  # Remove arrow tips
        )
        axes.to_edge(DOWN, buff=1)  # Reposition axes
        self.play(Create(axes), run_time=1.5)

        # Plot constraints forming a triangle
        lines = VGroup(
            axes.plot(lambda x: 6 - x, color=BLUE),  # x + y <= 6
            DashedLine(axes.coords_to_point(1, 0), axes.coords_to_point(1, 6), color=WHITE),  # x >= 1
            DashedLine(axes.coords_to_point(0, 1), axes.coords_to_point(6, 1), color=WHITE),  # y >= 1
        )
        self.play(Create(lines), run_time=2)

        # Feasible region (triangle)
        vertices = [
            axes.coords_to_point(1, 1),
            axes.coords_to_point(1, 5),
            axes.coords_to_point(5, 1)
        ]
        feasible_region = Polygon(*vertices, color=YELLOW, fill_color=YELLOW, fill_opacity=0.4)
        self.play(FadeIn(feasible_region, shift=DOWN), run_time=2)

        # Mark vertices
        dots = VGroup(*[Dot(point, color=RED) for point in vertices])
        self.play(FadeIn(dots), run_time=1.5)

        self.wait(8)
