from manim import *

class ObjectiveFunctionExplanation(Scene):
    def construct(self):
        # Título
        title = Text("¿Qué es una función objetivo?", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Mostrar z = f(x, y) debajo del título
        formula = Text("z = f(x, y)", font_size=28, color=YELLOW).next_to(title, DOWN)
        self.play(Write(formula))
        self.wait(1)

        # Variables independientes x, y
        x_text = Text("x: Variable independiente", font_size=24, color=BLUE).shift(LEFT * 3 + UP)
        y_text = Text("y: Variable independiente", font_size=24, color=GREEN).shift(RIGHT * 3 + UP)
        self.play(FadeIn(x_text), FadeIn(y_text))
        self.wait(1)

        # Variable dependiente z
        z_text = Text("z: Variable dependiente", font_size=24, color=RED).shift(DOWN * 2)
        self.play(FadeIn(z_text))
        self.wait(1)

        # Flechas que conectan x, y con z
        arrow_x_to_z = Arrow(start=x_text.get_bottom(), end=z_text.get_top(), color=BLUE)
        arrow_y_to_z = Arrow(start=y_text.get_bottom(), end=z_text.get_top(), color=GREEN)
        self.play(GrowArrow(arrow_x_to_z), GrowArrow(arrow_y_to_z))
        self.wait(1)

        # Explicación de la relación
        explanation = Text(
            "z depende de x e y mediante una fórmula,\n"
            "por ejemplo: z = ax + by + c",
            font_size=24,
        ).next_to(z_text, DOWN)
        self.play(Write(explanation))
        self.wait(3)

        # Despedida
        conclusion = Text("Esto es una función objetivo.", font_size=28).to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(2)