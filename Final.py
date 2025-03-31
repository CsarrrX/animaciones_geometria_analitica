from manim import *

class OptimalSolutionAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        
        # Colors
        FT_COLOR = BLUE
        PT_COLOR = ORANGE
        HIGHLIGHT = YELLOW
        RESULT_COLOR = GREEN
        
        # 1. Show points of interest
        points_text = Tex(
            "Key intersection points:",
            "(60, 48) and (90, 0)",
            tex_to_color_map={
                "(60, 48)": HIGHLIGHT,
                "(90, 0)": HIGHLIGHT
            },
            font_size=36
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(UP)
        
        self.play(Write(points_text[0]), run_time=1.5)
        self.wait(0.5)
        self.play(Write(points_text[1]), run_time=1.5)
        self.wait(2)
        
        # 2. Recall objective function
        obj_func = MathTex(
            "z = f(x,y) = ",
            "1000", "x", "+", "450", "y",
            tex_to_color_map={
                "x": FT_COLOR,
                "y": PT_COLOR,
                "1000": FT_COLOR,
                "450": PT_COLOR
            },
            font_size=36
        ).next_to(points_text, DOWN, buff=1)
        
        self.play(Write(obj_func), run_time=2)
        self.wait(2)
        
        # 3. Evaluate first point (60,48)
        eval1_title = Tex("Evaluating at (60, 48):", font_size=32).to_edge(LEFT)
        self.play(Write(eval1_title), run_time=1.5)
        
        eval1_calc = MathTex(
            "z = ",
            "1000", "\\cdot", "60", "+", "450", "\\cdot", "48",
            "=", "81600",
            tex_to_color_map={
                "1000": FT_COLOR,
                "60": HIGHLIGHT,
                "450": PT_COLOR,
                "48": HIGHLIGHT,
                "81600": RESULT_COLOR
            },
            font_size=36
        ).next_to(eval1_title, DOWN, buff=0.7, aligned_edge=LEFT)
        
        self.play(Write(eval1_calc[:8]), run_time=2.5)  # Show calculation
        self.wait(1)
        self.play(Write(eval1_calc[8:]), run_time=1.5)  # Show result
        self.wait(2)
        
        # 4. Evaluate second point (90,0)
        eval2_title = Tex("Evaluating at (90, 0):", font_size=32
                         ).next_to(eval1_calc, DOWN, buff=0.7, aligned_edge=LEFT)
        self.play(Write(eval2_title), run_time=1.5)
        
        eval2_calc = MathTex(
            "z = ",
            "1000", "\\cdot", "90", "+", "450", "\\cdot", "0",
            "=", "90000",
            tex_to_color_map={
                "1000": FT_COLOR,
                "90": HIGHLIGHT,
                "450": PT_COLOR,
                "0": HIGHLIGHT,
                "90000": RESULT_COLOR
            },
            font_size=36
        ).next_to(eval2_title, DOWN, buff=0.7, aligned_edge=LEFT)
        
        self.play(Write(eval2_calc[:8]), run_time=2)
        self.wait(0.8)
        self.play(Write(eval2_calc[8:]), run_time=1.2)
        self.wait(2)
        
        # 5. Comparison and optimal solution
        comparison = Tex(
            "81,600 < 90,000",
            color=HIGHLIGHT,
            font_size=40
        ).next_to(eval2_calc, DOWN, buff=1)
        
        self.play(Write(comparison), run_time=1.5)
        self.wait(1.5)
        
        optimal_solution = Tex(
            "Optimal staffing:",
            "60 full-time, 48 part-time",
            "Minimum weekly cost: \\$81,600",
            tex_to_color_map={
                "60 full-time": FT_COLOR,
                "48 part-time": PT_COLOR,
                "\\$81,600": RESULT_COLOR
            },
            font_size=36
        ).arrange(DOWN, aligned_edge=LEFT).next_to(comparison, DOWN, buff=1)
        
        self.play(LaggedStart(
            Write(optimal_solution[0]),
            Write(optimal_solution[1]),
            Write(optimal_solution[2]),
            lag_ratio=0.5,
            run_time=3
        ))
        self.wait(3)
        
        # 6. Final highlight
        box = SurroundingRectangle(
            optimal_solution,
            color=RESULT_COLOR,
            buff=0.4,
            corner_radius=0.2
        )
        self.play(Create(box), run_time=1.5)
        self.wait(3)