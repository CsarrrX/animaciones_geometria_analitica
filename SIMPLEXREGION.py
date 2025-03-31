from manim import *
import numpy as np

class OptimizedSimplexAnimation(Scene):
    def construct(self):
        # Configuración visual mejorada
        POLY_COLOR = "#3498db"
        VERTEX_COLOR = "#f1c40f"
        ACTIVE_COLOR = "#e74c3c"
        OPTIMAL_COLOR = "#2ecc71"
        BG_COLOR = "#000000"
        
        self.camera.background_color = BG_COLOR

        # ===== FASE 1: Evolución del área factible =====
        # 1.1 Figura inicial simple (4 vértices)
        simple_verts = [
            np.array([-2.5, -1, 0]),
            np.array([1, -1.5, 0]),
            np.array([2, 1.5, 0]),
            np.array([-1, 2, 0])
        ]
        poly = Polygon(*simple_verts, color=POLY_COLOR, 
                      fill_opacity=0.25, stroke_width=3)
        self.play(DrawBorderThenFill(poly), run_time=2)
        self.wait(1)

        # 1.2 Añadir vértices suavemente
        complex_verts = [
            np.array([-3, -1.5, 0]),
            np.array([-1, -2, 0]),
            np.array([1.5, -1.8, 0]),
            np.array([3, 0, 0]),
            np.array([2.5, 1.8, 0]),
            np.array([0.5, 2.5, 0]),
            np.array([-2, 1.5, 0])
        ]
        
        # Animación mejorada para añadir vértices
        for i in range(len(complex_verts)):
            new_verts = simple_verts + complex_verts[:i+1]
            new_poly = Polygon(*new_verts, color=POLY_COLOR, 
                              fill_opacity=0.25, stroke_width=3)
            
            # Solo animar si hay suficientes puntos para formar un polígono
            if len(new_verts) > 2:
                self.play(Transform(poly, new_poly), run_time=0.5)
        
        # Polígono complejo final
        final_complex = Polygon(*complex_verts, color=POLY_COLOR, 
                              fill_opacity=0.25, stroke_width=3)
        self.play(Transform(poly, final_complex), run_time=1.5)
        
        # Mantener figura compleja por 5 segundos (como pediste)
        self.wait(5)

        # 1.3 Regresar a la figura simple con animación suave
        for i in range(len(complex_verts), 2, -1):
            current_verts = complex_verts[:i] + simple_verts
            new_poly = Polygon(*current_verts, color=POLY_COLOR, 
                              fill_opacity=0.25, stroke_width=3)
            self.play(Transform(poly, new_poly), run_time=0.3)
        
        # Figura simple final
        final_simple = Polygon(*simple_verts, color=POLY_COLOR, 
                             fill_opacity=0.25, stroke_width=3)
        self.play(Transform(poly, final_simple), run_time=1.5)
        self.wait(1)

        # ===== FASE 2: Proceso de pivoteo mejorado =====
        # Añadir puntos en los vértices
        vertex_dots = [Dot(v, color=VERTEX_COLOR, radius=0.1) for v in simple_verts]
        self.play(*[GrowFromCenter(d) for d in vertex_dots], run_time=1.5)
        self.wait(0.5)

        # Función de pivoteo optimizada
        def smooth_pivot(start_idx, end_idx, move_direction=None):
            # Resaltar vértice actual
            self.play(
                vertex_dots[start_idx].animate.set_color(ACTIVE_COLOR).scale(1.3),
                run_time=0.7
            )
            
            # Crear línea de pivoteo
            pivot_line = Line(
                simple_verts[start_idx], simple_verts[end_idx],
                color=ACTIVE_COLOR, stroke_width=8
            )
            self.play(Create(pivot_line), run_time=1.2)
            
            # Movimiento adicional si se especifica dirección
            if move_direction:
                end_point = simple_verts[end_idx] + move_direction
                ghost_line = Line(
                    simple_verts[end_idx], end_point,
                    color=ACTIVE_COLOR, stroke_width=8, stroke_opacity=0.5
                )
                self.play(
                    Transform(pivot_line, ghost_line),
                    run_time=1.5
                )
                self.play(Uncreate(pivot_line))
                return None
            
            self.wait(0.3)
            return pivot_line

        # Secuencia de pivoteo con movimiento a la derecha
        pivot_line = smooth_pivot(0, 1)
        self.play(
            pivot_line.animate.put_start_and_end_on(
                simple_verts[1],
                simple_verts[1] + [2, 0, 0]
            ),
            run_time=1.5
        )
        self.play(Uncreate(pivot_line))
        
        pivot_line = smooth_pivot(1, 2, [0, 1.5, 0])
        pivot_line = smooth_pivot(2, 3)
        self.wait(0.5)

        # ===== FASE 3: Destacar solución óptima =====
        # Efecto de halo pulsante
        optimal_halo = Circle(
            radius=0.6, color=OPTIMAL_COLOR, stroke_width=15,
            stroke_opacity=0.7, fill_opacity=0
        ).move_to(simple_verts[3])
        
        self.play(
            vertex_dots[3].animate.set_color(OPTIMAL_COLOR).scale(1.5),
            GrowFromCenter(optimal_halo),
            run_time=1.5
        )
        
        # Animación de pulsación
        self.play(
            optimal_halo.animate.scale(1.5).set_stroke(opacity=0),
            run_time=2,
            rate_func=there_and_back
        )
        self.wait(3)