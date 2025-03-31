from manim import *

class StaffingProblemVisual(Scene):
    def construct(self):
        # Configuration
        self.camera.background_color = BLACK
        primary_color = WHITE
        accent_yellow = "#FFFF00"
        accent_blue = "#00AAFF"
        accent_red = "#FF5555"
        
        # 1. Title
        title = Text("Staffing Optimization Problem", font_size=42, color=primary_color)
        subtitle = Text("Minimizing Labor Costs", font_size=32, color=primary_color)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.5)
        self.play(Write(title_group))
        self.wait(2)
        self.play(FadeOut(title_group))
        
        # 2. Problem Statement
        problem_lines = [
            "A department store needs to cover",
            "at least 3,600 work hours per week",
            "using full-time and part-time staff"
        ]
        
        problem_text = VGroup(*[
            Text(line, font_size=28, color=primary_color) 
            for line in problem_lines
        ]).arrange(DOWN, buff=0.4)
        
        # Highlight hour requirement
        problem_text[1].set_color(accent_yellow)
        
        self.play(Write(problem_text))
        self.wait(3)
        self.play(FadeOut(problem_text))
        
        # 3. Store Visualization
        store = Rectangle(
            height=3, width=5, 
            fill_color="#333333", 
            fill_opacity=1, 
            stroke_color=primary_color
        )
        sign = Text("DEPARTMENT STORE", font_size=24, color=primary_color).next_to(store, UP)
        
        self.play(
            DrawBorderThenFill(store),
            Write(sign),
            run_time=1.5
        )
        self.wait(1.5)
        
        # 4. Hour Requirement
        hours_text = Text("3,600 hours/week", font_size=32, color=accent_yellow)
        hours_text.next_to(store, DOWN)
        
        self.play(
            Write(hours_text),
            run_time=1.5
        )
        self.wait(2.5)
        
        # 5. Employee Introduction
        full_time = SVGMobject("person", fill_color=accent_blue).scale(0.6)
        part_time = SVGMobject("person", fill_color=primary_color).scale(0.6)
        
        employees = VGroup()
        labels = VGroup()
        details = VGroup()
        
        # Position employees with more spacing
        for i in range(1):
            # Employees
            ft = full_time.copy().shift(LEFT*3.5 + UP*i*1.5)
            pt = part_time.copy().shift(RIGHT*3.5 + UP*i*1.5)
            employees.add(ft, pt)
            
            # Labels
            ft_label = Text("Full-Time", color=accent_blue, font_size=24).next_to(ft, UP, buff=0.8)
            pt_label = Text("Part-Time", color=primary_color, font_size=24).next_to(pt, UP, buff=0.8)
            labels.add(ft_label, pt_label)
            
            # Details
            ft_hours = Text("40 hours", font_size=22, color=primary_color).next_to(ft, DOWN, buff=0.5)
            pt_hours = Text("25 hours", font_size=22, color=primary_color).next_to(pt, DOWN, buff=0.5)
            
            ft_cost = Text("$25/hour", font_size=22, color=accent_blue).next_to(ft_hours, DOWN, buff=0.3)
            pt_cost = Text("$18/hour", font_size=22, color=primary_color).next_to(pt_hours, DOWN, buff=0.3)
            details.add(ft_hours, pt_hours, ft_cost, pt_cost)
            
            # Animate in groups
            self.play(
                FadeIn(ft, shift=RIGHT*0.5),
                FadeIn(pt, shift=LEFT*0.5),
                run_time=1
            )
            self.play(
                Write(ft_label),
                Write(pt_label),
                run_time=0.75
            )
            self.wait(0.5)
        
        self.wait(1)
        
        # Animate details
        self.play(
            LaggedStart(*[Write(d) for d in details]),
            run_time=2
        )
        self.wait(3)
        
        # 6. Ratio Constraint
        constraint_title = Text("Operational Constraint:", font_size=26, color=primary_color)
        
        ratio_formula = MathTex(
            r"\text{FT} \geq 1.25 \times \text{PT}",
            color=accent_red
        ).scale(1.3)
        
        ratio_explanation = Text(
            "Full-time employees ≥ 1.25 × Part-time",
            font_size=24,
            color=accent_red
        )
        
        constraint_group = VGroup(
            constraint_title,
            ratio_formula,
            ratio_explanation
        ).arrange(DOWN, buff=0.6)
        
        self.play(Write(constraint_title))
        self.wait(0.5)
        self.play(Write(ratio_formula))
        self.wait(1)
        self.play(Write(ratio_explanation))
        self.wait(3)
        
        # 7. Key Questions
        question1 = Text(
            "How many employees of each type",
            font_size=28,
            color=primary_color
        )
        question2 = Text(
            "should be hired to minimize weekly costs?",
            font_size=28,
            color=primary_color
        ).next_to(question1, DOWN, buff=0.3)
        
        question_group = VGroup(question1, question2).center()
        
        self.play(
            FadeOut(*[mob for mob in self.mobjects if mob not in [store, sign]]),
            run_time=1.5
        )
        self.play(Write(question_group))
        self.wait(3)
        
        # 8. Data Summary Table
        table_title = Text("Summary Data", font_size=30, color=primary_color).to_edge(UP)
        
        table = Table(
            [["", "Hours/Week", "Cost/Hour"],
             ["Full-Time", "40", "$25"],
             ["Part-Time", "25", "$18"]],
            include_outer_lines=True,
            line_config={"color": primary_color}
        ).scale(0.7)
        
        # Color accents
        table.get_entries((2,0)).set_color(accent_blue)
        table.get_entries((2,1)).set_color(accent_blue)
        table.get_entries((2,2)).set_color(accent_blue)
        
        self.play(
            Write(table_title),
            run_time=1
        )
        self.wait(0.5)
        self.play(
            Create(table),
            run_time=2
        )
        self.wait(4)
        
        # Final transition
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)