from manim import *

class ObjectiveFunctionFinalRefined(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        
        # Colors
        FT_COLOR = BLUE
        PT_COLOR = ORANGE
        Z_COLOR = GREEN
        HIGHLIGHT = YELLOW
        
        # 1. Introduce variables with smaller text
        x_icon = Square(color=FT_COLOR, fill_opacity=0.5).set_height(1)
        x_label = Text("Full-time", color=FT_COLOR, font_size=20).next_to(x_icon, DOWN)  # Reduced font size
        x_group = Group(x_icon, x_label)

        y_icon = Circle(color=PT_COLOR, fill_opacity=0.5).set_height(0.8)
        y_label = Text("Part-time", color=PT_COLOR, font_size=20).next_to(y_icon, DOWN)  # Reduced font size
        y_group = Group(y_icon, y_label)

        variables = Group(x_group, y_group).arrange(RIGHT, buff=1.5)  # Reduced buffer
        
        self.play(
            DrawBorderThenFill(x_icon),
            Write(x_label),
            run_time=1.5
        )
        self.wait(0.5)
        self.play(
            DrawBorderThenFill(y_icon),
            Write(y_label),
            run_time=1.5
        )
        self.wait(2)
        
        # 2. Show cost calculation with smaller text
        ft_calc_text = Text("40 × $25 =", color=FT_COLOR, font_size=20).shift(UP*1.5 + LEFT*2)  # Adjusted position
        ft_cost_text = Text("$1000/week", color=HIGHLIGHT, font_size=24).next_to(ft_calc_text, RIGHT)  # Reduced font size
        
        arrow_x = Arrow(x_icon.get_top(), ft_calc_text.get_bottom(), color=WHITE)
        
        self.play(
            Create(arrow_x),
            Write(ft_calc_text),
            run_time=1.5
        )
        self.wait(1)
        self.play(
            Write(ft_cost_text),
            run_time=1
        )
        self.wait(1.5)
        
        # Part-time calculation
        pt_calc_text = Text("25 × $18 =", color=PT_COLOR, font_size=20).shift(UP*1.5 + RIGHT*2)  # Adjusted position
        pt_cost_text = Text("$450/week", color=HIGHLIGHT, font_size=24).next_to(pt_calc_text, RIGHT)  # Reduced font size
        
        arrow_y = Arrow(y_icon.get_top(), pt_calc_text.get_bottom(), color=WHITE)
        
        self.play(
            Create(arrow_y),
            Write(pt_calc_text),
            run_time=1.5
        )
        self.wait(1)
        self.play(
            Write(pt_cost_text),
            run_time=1
        )
        self.wait(2)
        
        # 3. Build the objective function
        self.play(
            FadeOut(arrow_x),
            FadeOut(arrow_y),
            ft_calc_text.animate.move_to(LEFT*3 + UP*1),
            ft_cost_text.animate.next_to(ft_calc_text, RIGHT),
            pt_calc_text.animate.move_to(RIGHT*3 + UP*1),
            pt_cost_text.animate.next_to(pt_calc_text, RIGHT),
            run_time=1.5
        )
        
        # Create centered Z label
        z_label = Text("Minimize:", color=Z_COLOR, font_size=28).shift(UP*3)  # Centered and reduced size
        z_symbol = Text("z =", color=Z_COLOR, font_size=28).next_to(z_label, RIGHT)
        z_header = Group(z_label, z_symbol) # Centered group
        
        self.play(
            Write(z_label),
            Write(z_symbol),
            run_time=1
        )
        
        # Animate building the function with smaller text
        x_term = Text("1000x", color=FT_COLOR, font_size=28).next_to(z_symbol, RIGHT)  # Reduced font size
        plus = Text(" + ", color=WHITE, font_size=28).next_to(x_term, RIGHT)  # Reduced font size
        y_term = Text("450y", color=PT_COLOR, font_size=28).next_to(plus, RIGHT)  # Reduced font size
        
        self.play(
            ReplacementTransform(ft_cost_text.copy(), x_term),
            run_time=1.5
        )
        self.wait(0.5)
        self.play(
            Write(plus),
            run_time=0.5
        )
        self.wait(0.5)
        self.play(
            ReplacementTransform(pt_cost_text.copy(), y_term),
            run_time=1.5
        )
        self.wait(2)
        
        # 4. Final highlight
        full_func = Group(z_header, x_term, plus, y_term)
        box = SurroundingRectangle(full_func, color=HIGHLIGHT, buff=0.3)
        
        self.play(
            Create(box),
            run_time=1.5
        )
        self.wait(3)
        
        # Clean transition to next part
        all_mobjects = Group(*[mob for mob in self.mobjects if isinstance(mob, (VMobject, Mobject))])
        self.play(
            FadeOut(all_mobjects),
            run_time=1.5
        )