from manim import *

class LinearProgrammingStepsCompact(Scene):
    def construct(self):
        # Title
        title = Text("Steps to Solve a Linear Programming Problem").scale(0.6).to_edge(UP)
        self.play(Write(title))
        self.wait(1)  # Reduced wait time

        # List of steps
        steps = VGroup(
            Text("1. Write the objective function"),
            Text("2. Write the constraints"),
            Text("3. Graph the feasible region")
        ).scale(0.5).arrange(DOWN, aligned_edge=LEFT, buff=0.7).to_edge(LEFT, buff=1)
        
        self.play(Write(steps))
        self.wait(1)  # Reduced wait time

        # Example step 1
        example1 = MathTex("z = 2x + 3y").scale(0.6).next_to(steps[0], RIGHT, buff=1.5)
        self.play(Write(example1))
        self.wait(1)  # Reduced wait time

        # Example step 2 (system of inequalities in one line)
        example2 = MathTex("x \geq 0, \quad y \geq 0, \quad x + y \leq 4").scale(0.6).next_to(steps[1], RIGHT, buff=1.5)
        self.play(Write(example2))
        self.wait(1)  # Reduced wait time

        # Example step 3 (larger graph)
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            axis_config={"include_numbers": False},
        ).scale(0.2).next_to(steps[2], RIGHT, buff=1.5)
        line = axes.plot(lambda x: 4 - x, x_range=[0, 4], color=BLUE)
        region = Polygon(
            axes.coords_to_point(0, 0),
            axes.coords_to_point(4, 0),
            axes.coords_to_point(0, 4),
            fill_opacity=0.2,
            color=GREEN,
        )
        self.play(Create(axes), Create(line), FadeIn(region))
        self.wait(1)  # Reduced wait time

        # Clear the screen and leave only the title
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob != title])
        self.wait(1)  # Reduced wait time

        # Step 4: Evaluate the objective function
        step4 = Text("4. Evaluate the objective function").scale(0.5).to_edge(LEFT, buff=1)
        self.play(Write(step4))
        obj_func = Text("Recall that our objective function is: z = 2x + 3y").scale(0.3).to_edge(UP, buff=1.6)
        self.play(Write(obj_func))
        self.wait(1)  # Reduced wait time
        
        evaluations = VGroup(
            MathTex("z(0,0) = 0").scale(0.5),
            MathTex("z(4,0) = 8").scale(0.5),
            MathTex("z(0,4) = 12").scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(step4, RIGHT, buff=1.5)
        self.play(Write(evaluations))
        self.wait(1)  # Reduced wait time

        # Conclusion
        self.wait(2)  # Reduced wait time
