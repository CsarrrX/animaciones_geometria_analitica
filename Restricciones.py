from manim import *

class ConstraintsAnimationFinal(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        
        # Colors
        FT_COLOR = BLUE
        PT_COLOR = ORANGE
        CONSTRAINT_COLOR = YELLOW
        HIGHLIGHT = "#FF6B6B"
        
        # 1. Title (matches speaking pace)
        title = Tex("Step 2: Establish Constraints", 
                   color=WHITE, 
                   font_size=36).to_edge(UP)
        self.play(Write(title), run_time=1.5)
        self.wait(1)
        
        # 2. Hours constraint (centered and compact)
        hours_text = Tex(
            "At least 3,600 work hours needed:",
            color=CONSTRAINT_COLOR,
            font_size=32
        ).shift(UP*0.8)
        
        hours_eq = MathTex(
            "40x", "+", "25y", "\\geq", "3600",
            substrings_to_isolate=["40x", "25y", "3600"]
        ).set_color_by_tex("40x", FT_COLOR
        ).set_color_by_tex("25y", PT_COLOR
        ).set_color_by_tex("3600", HIGHLIGHT
        ).next_to(hours_text, DOWN, buff=0.4)
        
        # Animate with speaking pace
        self.play(Write(hours_text), run_time=2)
        self.wait(0.5)  # Natural pause
        self.play(Write(hours_eq), run_time=2)
        self.wait(1.5)  # Processing time
        
        # 3. Ratio constraint (adjusted position)
        ratio_text = Tex(
            "FT employees $\geq$ 1.25 PT:",
            color=CONSTRAINT_COLOR,
            font_size=32
        ).next_to(hours_eq, DOWN, buff=0.7)  # Reduced spacing
        
        ratio_eq = MathTex(
            "x", "\\geq", "1.25", "y",
            substrings_to_isolate=["x", "y"]
        ).set_color_by_tex("x", FT_COLOR
        ).set_color_by_tex("y", PT_COLOR
        ).next_to(ratio_text, DOWN, buff=0.4)
        
        self.play(Write(ratio_text), run_time=1.8)
        self.wait(0.3)
        self.play(Write(ratio_eq), run_time=1.5)
        self.wait(1.5)
        
        # 4. Non-negativity (adjusted position)
        nonneg_text = Tex(
            "Non-negative employees:",
            color=CONSTRAINT_COLOR,
            font_size=32
        ).next_to(ratio_eq, DOWN, buff=0.7)  # Reduced spacing
        
        nonneg_eq = MathTex(
            "x \\geq 0, \\quad y \\geq 0",
            substrings_to_isolate=["x", "y"]
        ).set_color_by_tex("x", FT_COLOR
        ).set_color_by_tex("y", PT_COLOR
        ).next_to(nonneg_text, DOWN, buff=0.4)
        
        self.play(Write(nonneg_text), run_time=1.5)
        self.wait(0.3)
        self.play(Write(nonneg_eq), run_time=1.2)
        self.wait(2)
        
        # 5. Highlight box (fits all content)
        all_constraints = VGroup(
            hours_text, hours_eq,
            ratio_text, ratio_eq,
            nonneg_text, nonneg_eq
        ).center()  # Ensure everything is centered
        
        box = SurroundingRectangle(
            all_constraints, 
            color=HIGHLIGHT, 
            buff=0.4,  # Tighter padding
            corner_radius=0.2
        )
        
        # Final reveal after pause
        self.wait(1)
        self.play(Create(box), run_time=1.5)
        self.wait(2)
        
        # Smooth exit
        self.play(
            FadeOut(VGroup(all_constraints, box, title)),
            run_time=1.5
        )