import manim
from typing import Optional

class PhigrosScoreCalculator(manim.Scene):
    def __init__(self) -> None:
        super().__init__()

        self.font = "JetBrains Mono NL"
        self.title_font_size = 64
        self.subtitle_font_size = 36
        self.title_color = manim.WHITE
        self.title_fade_in_time = 1.0
        self.title_lasting_time = 3.0
        self.title_fade_out_time = 1.0

        self.sep_time = 0.5

        self.section_scale_factor = 0.5
        self.section_fade_in_time = 1.0
        self.section_lasting_time = 2.0
        self.section_move_time = 1.0
        self.section_title_color = manim.BLUE
        self.section_clean_time = 1.0

        self.formula_font_size = 32

    def construct(self) -> None:
        self.display_title()
        self.display_chat_history()
        self.display_section_1()
        self.display_section_2()
        self.display_section_3()

    def display_title(self) -> None:
        title = manim.Text(
            "Phigros 分数逆计算器", 
            font=self.font, font_size=self.title_font_size, color=self.title_color
        )
        subtitle = manim.Text(
            "基于数论的分数逆向计算", 
            font=self.font, font_size=self.subtitle_font_size, color=self.title_color
        )
        subtitle.next_to(title, manim.DOWN)

        title_group = manim.VGroup(title, subtitle)
        title_group.move_to(manim.ORIGIN)

        self.play(manim.Write(title_group, shift=manim.UP, run_time=self.title_fade_in_time))
        self.wait(self.title_lasting_time)
        self.play(manim.Unwrite(title_group, shift=manim.UP, run_time=self.title_fade_out_time))
        self.remove(title_group)

        self.wait(self.sep_time)

    def display_chat_history(self) -> None:
        chat_history_image_1 = manim.ImageMobject("chat_his_1.jpg")
        chat_history_image_2 = manim.ImageMobject("chat_his_2.jpg")
        chat_history_image_3 = manim.ImageMobject("chat_his_3.jpg")

        chat_history_image_1.to_edge(manim.UP, buff=0.5)
        chat_history_image_2.next_to(chat_history_image_1, manim.DOWN * 0.4, buff=0.5)
        chat_history_image_3.next_to(chat_history_image_2, manim.DOWN * 0.4, buff=0.5)
        chat_history_image_3.align_to(chat_history_image_2, manim.RIGHT)

        self.play(manim.FadeIn(chat_history_image_1, shift=manim.UP, run_time=1.0))
        self.wait(6.0)

        self.play(manim.FadeIn(chat_history_image_2, shift=manim.UP, run_time=1.0))
        self.wait(1.0)

        self.play(manim.FadeIn(chat_history_image_3, shift=manim.UP, run_time=1.0))
        self.wait(5.0)

        self.play(
            manim.FadeOut(chat_history_image_1, shift=manim.UP, run_time=1.0),
            manim.FadeOut(chat_history_image_2, shift=manim.UP, run_time=1.0),
            manim.FadeOut(chat_history_image_3, shift=manim.UP, run_time=1.0)
        )
        self.wait(self.sep_time)

    def display_section_title(self, section_title: str, section_subtitle: Optional[str] = None) -> None:
        title = manim.Text(
            section_title, 
            font=self.font, font_size=self.title_font_size, color=self.section_title_color
        )

        if section_subtitle:
            subtitle = manim.Text(
                section_subtitle, 
                font=self.font, font_size=self.subtitle_font_size, color=self.section_title_color
            )
            subtitle.next_to(title, manim.DOWN)
            section_group = manim.VGroup(title, subtitle)
        else:
            section_group = title

        self.section_title = section_group

        self.play(manim.Write(section_group, shift=manim.UP, run_time=self.section_fade_in_time))
        self.wait(self.section_lasting_time)
        self.play(
            section_group.animate.scale(self.section_scale_factor).to_corner(manim.UL),
            run_time=self.section_move_time
        )
        self.wait(self.sep_time)
        
    def display_section_1(self) -> None:
        self.display_section_title("第一节：分数正向计算公式")
        self.display_score_formula()
        self.display_notation()
        self.clean_section_1()
        self.wait(self.sep_time)

    def display_score_formula(self) -> None:
        formula_origin = manim.MathTex(
            r"\text{总分}", r" = \mathrm{round}\left(", r"\text{判定分}", " + ", r"\text{连击分}", r"\right)",
            tex_template=manim.TexTemplateLibrary.ctex,
            font_size=self.formula_font_size
        )
        formula_origin[0].set_color(manim.WHITE)
        formula_origin[1].set_color(manim.WHITE)
        formula_origin[2].set_color(manim.GREEN)
        formula_origin[3].set_color(manim.WHITE)
        formula_origin[4].set_color(manim.RED)
        formula_origin[5].set_color(manim.WHITE)

        formula_origin.move_to(manim.ORIGIN + manim.UP * 2.0)

        self.play(manim.Write(formula_origin, run_time=1.0))
        self.wait(12.0)
        
        formula_expanded = manim.MathTex(
            r"\text{总分}", r" = \mathrm{round}\left(", 
            r"\frac{\text{Perfect} + \text{Good} \times 65\%}{\text{总物量}} \times 900000", " + ", 
            r"\frac{\text{Max Combo}}{\text{总物量}} \times 100000", r"\right)",
            tex_template=manim.TexTemplateLibrary.ctex,
            font_size=self.formula_font_size
        )
        formula_expanded[0].set_color(manim.WHITE)
        formula_expanded[1].set_color(manim.WHITE)
        formula_expanded[2].set_color(manim.GREEN)
        formula_expanded[3].set_color(manim.WHITE)
        formula_expanded[4].set_color(manim.RED)
        formula_expanded[5].set_color(manim.WHITE)

        formula_expanded.move_to(formula_origin.get_center())

        self.play(manim.Transform(formula_origin, formula_expanded, run_time=1.0))
        self.formula = formula_origin

    def display_notation(self) -> None:
        notation_title = manim.Text(
            "符号说明",
            font=self.font, font_size=self.subtitle_font_size, color=self.title_color
        )
        notation_title.next_to(self.formula, manim.DOWN)

        notation_lines = [
            manim.MathTex(
                r"\text{总分} \quad \text{Score}",
                tex_template=manim.TexTemplateLibrary.ctex, font_size=self.formula_font_size, color=manim.WHITE
            ),
            manim.MathTex(
                r"\text{Perfect 判定个数} \quad \text{Perfect}",
                tex_template=manim.TexTemplateLibrary.ctex, font_size=self.formula_font_size, color=manim.GREEN
            ),
            manim.MathTex(
                r"\text{Good 判定个数} \quad \text{Good}",
                tex_template=manim.TexTemplateLibrary.ctex, font_size=self.formula_font_size, color=manim.GREEN
            ),
            manim.MathTex(
                r"\text{连击数} \quad \text{Max Combo}",
                tex_template=manim.TexTemplateLibrary.ctex, font_size=self.formula_font_size, color=manim.RED
            ),
            manim.MathTex(
                r"\text{总物量} \quad \text{Total Amount}",
                tex_template=manim.TexTemplateLibrary.ctex, font_size=self.formula_font_size, color=manim.WHITE
            ),
            manim.MathTex(
                r"\text{有效打击} \quad \text{Effective Hits} = \text{Perfect} + \text{Good}",
                tex_template=manim.TexTemplateLibrary.ctex, font_size=self.formula_font_size, color=manim.WHITE
            )
        ]

        notation_content = manim.VGroup(*notation_lines).arrange(
            direction=manim.DOWN * 0.5, aligned_edge=manim.LEFT, buff=0.5
        )
        notation_content.next_to(notation_title, manim.DOWN)

        self.play(manim.Write(notation_title, run_time=1.0))
        self.play(manim.Write(notation_content, run_time=1.0))
        self.wait(15)

        notation_lines_transformed = [
            manim.MathTex(
                r"\text{总分} \quad \text{S}",
                tex_template=manim.TexTemplateLibrary.ctex, font_size=self.formula_font_size, color=manim.WHITE
            ),
            manim.MathTex(
                r"\text{Perfect 判定个数} \quad \text{P}",
                tex_template=manim.TexTemplateLibrary.ctex, font_size=self.formula_font_size, color=manim.GREEN
            ),
            manim.MathTex(
                r"\text{Good 判定个数} \quad \text{G}",
                tex_template=manim.TexTemplateLibrary.ctex, font_size=self.formula_font_size, color=manim.GREEN
            ),
            manim.MathTex(
                r"\text{连击数} \quad \text{C}",
                tex_template=manim.TexTemplateLibrary.ctex, font_size=self.formula_font_size, color=manim.RED
            ),
            manim.MathTex(
                r"\text{总物量} \quad \text{A}",
                tex_template=manim.TexTemplateLibrary.ctex, font_size=self.formula_font_size, color=manim.WHITE
            ),
            manim.MathTex(
                r"\text{有效打击} \quad \text{E} = \text{P} + \text{G}",
                tex_template=manim.TexTemplateLibrary.ctex, font_size=self.formula_font_size, color=manim.WHITE
            )
        ]

        notation_content_transformed = manim.VGroup(*notation_lines_transformed).arrange(
            direction=manim.DOWN * 0.5, aligned_edge=manim.LEFT, buff=0.5
        )
        notation_content_transformed.next_to(notation_title, manim.DOWN)

        self.formula_transformed = manim.MathTex(
            r"\text{S}", r" = \mathrm{round}\left(", 
            r"\frac{\text{P} + \text{G} \times 65\%}{\text{A}} \times 900000", " + ",
            r"\frac{\text{C}}{\text{A}} \times 100000", r"\right)",
            tex_template=manim.TexTemplateLibrary.ctex, font_size=self.formula_font_size
        )
        self.formula_transformed[0].set_color(manim.WHITE)
        self.formula_transformed[1].set_color(manim.WHITE)
        self.formula_transformed[2].set_color(manim.GREEN)
        self.formula_transformed[3].set_color(manim.WHITE)
        self.formula_transformed[4].set_color(manim.RED)
        self.formula_transformed[5].set_color(manim.WHITE)

        self.formula_transformed.move_to(self.formula.get_center())

        self.play(
            manim.Transform(self.formula, self.formula_transformed, run_time=1.0),
            manim.Transform(notation_content, notation_content_transformed, run_time=1.0)
        )
        self.wait(5)

        self.notation_title = notation_title
        self.notation_content = notation_content

    def clean_section_1(self) -> None:
        self.play(
            manim.Unwrite(self.formula, run_time=self.section_clean_time),
            manim.Unwrite(self.section_title, run_time=self.section_clean_time),
            manim.Unwrite(self.notation_title, run_time=self.section_clean_time),
            manim.Unwrite(self.notation_content, run_time=self.section_clean_time)
        )
        self.remove(self.notation_title, self.notation_content)

    def display_section_2(self) -> None:
        self.formula_font_size = 48
        self.display_section_title("第二节：建模约束与问题转化", "分数计算的约束条件")
        self.display_constraints()
        self.clean_section_2()
        self.wait(self.sep_time)

    def display_constraints(self) -> None:
        self.display_constraints_C()
        self.display_all_constraints()

    def display_constraints_C(self) -> None:
        goal = manim.Text(
            "目标：计算 C 的上下界",
            font=self.font, font_size=self.subtitle_font_size, color=self.title_color
        )
        goal.move_to(manim.ORIGIN + manim.UP * 2.0)

        self.play(manim.Write(goal, run_time=1.0))
        self.wait(1.0)

        notice = manim.MathTex(
            r"\text{Perfect}", r"\quad" ,r"\text{Good}", r"\quad \text{无区别，都算一次连击}",
            tex_template=manim.TexTemplateLibrary.ctex, font_size=self.formula_font_size, color=manim.WHITE
        )
        notice[0].set_color("#E8D547")
        notice[2].set_color(manim.BLUE)
        notice.next_to(goal, manim.DOWN)

        self.play(manim.Write(notice, run_time=1.0))
        self.wait(10.0)

        hit_sequence = manim.MathTex(
            "1", "1", r"\dots", "1", "0", "0", r"\dots", "0",
            tex_template=manim.TexTemplateLibrary.ctex, font_size=self.formula_font_size, color=manim.WHITE
        )
        hit_sequence.next_to(notice, manim.DOWN * 2)

        ones_group = manim.VGroup(*hit_sequence[:4])
        ones_brace = manim.Brace(ones_group, direction=manim.DOWN, buff=0.1)
        ones_label = ones_brace.get_text("E * 1")

        hit_sequence_group = manim.VGroup(hit_sequence, ones_brace, ones_label)

        self.play(manim.Write(hit_sequence, run_time=1.0))
        self.wait(1.0)

        self.play(manim.Create(ones_brace), manim.Create(ones_label))
        self.wait(5.0)

        supremum = manim.MathTex(
            r"\text{上确界} \quad C \leq E",
            tex_template=manim.TexTemplateLibrary.ctex, font_size=self.formula_font_size, color=manim.WHITE
        )
        supremum.move_to(hit_sequence.get_center())

        self.play(manim.Transform(hit_sequence_group, supremum, run_time=1.0))
        supremum = hit_sequence_group
        self.wait(10.0)

        hit_sequence = manim.MathTex(
            "1", "1", r"\dots", "1", "0", "1", "1", r"\dots", "1", "0", "1", "1", r"\dots", "1",
            tex_template=manim.TexTemplateLibrary.ctex, font_size=self.formula_font_size, color=manim.WHITE
        )
        hit_sequence.next_to(supremum, manim.DOWN * 2)

        zeros_brace = manim.Brace(hit_sequence, direction=manim.DOWN, buff=0.1)
        zeros_label = zeros_brace.get_text("(A - E) * 0")

        hit_sequence_group = manim.VGroup(hit_sequence, zeros_brace, zeros_label)

        self.play(manim.Write(hit_sequence, run_time=1.0))
        self.wait(1.0)

        self.play(manim.Create(zeros_brace), manim.Create(zeros_label))
        self.wait(7.0)

        infimum = manim.MathTex(
            r"\text{下界} \quad C \geq \lceil \frac{E}{A - E + 1} \rceil \\",
            r"\text{下界} \quad C \geq \lceil \frac{S - 900000}{100000} \times A \rceil",
            tex_template=manim.TexTemplateLibrary.ctex, font_size=self.formula_font_size, color=manim.WHITE
        )
        infimum.next_to(supremum, manim.DOWN)

        self.play(manim.Transform(hit_sequence_group, infimum, run_time=1.0))
        infimum = hit_sequence_group
        self.wait(10.0)

        self.play(
            manim.Unwrite(goal, run_time=1.0),
            manim.Unwrite(notice, run_time=1.0),
            manim.Unwrite(hit_sequence, run_time=1.0),
            manim.Unwrite(supremum, run_time=1.0),
            manim.Unwrite(infimum, run_time=1.0)
        )
        self.remove(
            goal, notice, 
            supremum, infimum, 
            zeros_brace, zeros_label, ones_brace, ones_label, hit_sequence_group
        )

    def display_all_constraints(self) -> None:
        self.formula_font_size = 32

        self.formula = manim.MathTex(
            r"\text{S}", r" = \mathrm{round}\left(", 
            r"\frac{\text{P} + \text{G} \times 65\%}{\text{A}} \times 900000", " + ",
            r"\frac{\text{C}}{\text{A}} \times 100000", r"\right)",
            tex_template=manim.TexTemplateLibrary.ctex, font_size=self.formula_font_size
        )
        self.formula[0].set_color(manim.WHITE)
        self.formula[1].set_color(manim.WHITE)
        self.formula[2].set_color(manim.GREEN)
        self.formula[3].set_color(manim.WHITE)
        self.formula[4].set_color(manim.RED)
        self.formula[5].set_color(manim.WHITE)
        self.formula.move_to(manim.ORIGIN + manim.UP * 2.0)

        constraints_content = manim.MathTex(
            r"\text{s.t.}~\begin{cases}"
            r"A, S \quad \text{给定} \\"
            r"S, P, G, C, A \in \mathbb{N} \\"
            r"A \geq E \geq C \geq \max(\lceil \frac{E}{A - E + 1} \rceil, \lceil \frac{S - 900000}{100000} \times A \rceil) \\"
            r"\end{cases}",
            tex_template=manim.TexTemplateLibrary.ctex,
            font_size=self.formula_font_size
        )
        constraints_content.next_to(self.formula, manim.DOWN * 2.0)

        self.play(
            manim.Write(self.formula, run_time=1.0),
            manim.Write(constraints_content, run_time=1.0)
        )
        self.wait(5.0)

        constraints_content_transformed = manim.MathTex(
            r"\text{s.t.}~\begin{cases}"
            r"A, S \quad \text{给定} \\"
            r"S, P, G, C, A \in \mathbb{N} \\"
            r"A \geq E \geq C \geq \max(\lceil \frac{E}{A - E + 1} \rceil, \lceil \frac{S - 900000}{100000} \times A \rceil) \\"
            r"S - 0.5 \leq \frac{\text{P} + \text{G} \times 65\%}{\text{A}} \times 900000 + \frac{\text{C}}{\text{A}} \times 100000 < S + 0.5 \\"
            r"\end{cases}",
            tex_template=manim.TexTemplateLibrary.ctex,
            font_size=self.formula_font_size
        )
        constraints_content_transformed.next_to(self.formula, manim.DOWN * 2.0)

        self.play(
            manim.Transform(constraints_content, constraints_content_transformed, run_time=1.0)
        )
        self.wait(5.0)

        constraints_content_transformed = manim.MathTex(
            r"\text{s.t.}~\begin{cases}"
            r"A, S \quad \text{给定} \\"
            r"S, P, G, C, A \in \mathbb{N} \\"
            r"A \geq E \geq C \geq \max(\lceil \frac{E}{A - E + 1} \rceil, \lceil \frac{S - 900000}{100000} \times A \rceil) \\"
            r"(S - 0.5)A \leq (P + 0.65 G) \times 900000 + C \times 100000 < (S + 0.5)A \\"
            r"\end{cases}",
            tex_template=manim.TexTemplateLibrary.ctex,
            font_size=self.formula_font_size
        )
        constraints_content_transformed.next_to(self.formula, manim.DOWN * 2.0)

        self.play(manim.Transform(constraints_content, constraints_content_transformed, run_time=1.0))
        self.wait(5.0)

        constraints_content_transformed = manim.MathTex(
            r"\text{s.t.}~\begin{cases}"
            r"A, S \quad \text{给定} \\"
            r"S, P, G, C, A \in \mathbb{N} \\"
            r"A \geq E \geq C \geq \max(\lceil \frac{E}{A - E + 1} \rceil, \lceil \frac{S - 900000}{100000} \times A \rceil) \\"
            r"(S - 0.5)A \leq 900000 P + 585000 G + 100000 C < (S + 0.5)A \\"
            r"\end{cases}",
            tex_template=manim.TexTemplateLibrary.ctex,
            font_size=self.formula_font_size
        )
        constraints_content_transformed.next_to(self.formula, manim.DOWN * 2.0)

        self.play(manim.Transform(constraints_content, constraints_content_transformed, run_time=1.0))
        self.wait(5.0)

        constraints_content_transformed = manim.MathTex(
            r"\text{s.t.}~\begin{cases}"
            r"A, S \quad \text{给定} \\"
            r"S, P, G, C, A \in \mathbb{N} \\"
            r"A \geq E \geq C \max(\lceil \frac{E}{A - E + 1} \rceil, \lceil \frac{S - 900000}{100000} \times A \rceil) \\"
            r"a_1 P + a_2 G + a_3 C = k \\"
            r"a_1 = 900000, a_2 = 585000, a_3 = 100000 \\"
            r"k \in \mathbb{N}, k \in \left[ (S - 0.5)A, (S + 0.5)A \right) \\"
            r"\end{cases}",
            tex_template=manim.TexTemplateLibrary.ctex,
            font_size=self.formula_font_size
        )
        constraints_content_transformed.next_to(self.formula, manim.DOWN * 2.0)

        self.play(manim.Transform(constraints_content, constraints_content_transformed, run_time=1.0))
        self.constraints = constraints_content
        self.wait(5.0)

    def clean_section_2(self):
        self.play(
            manim.Unwrite(self.formula, run_time=1.0),
            manim.Unwrite(self.constraints, run_time=1.0),
            manim.Unwrite(self.section_title, run_time=1.0)
        )
        self.wait(1.0)

    def display_section_3(self) -> None:
        self.formula_font_size = 48
        self.display_section_title("第三节：线性丢番图方程")
        self.display_diophantine_equation()
        self.wait(self.sep_time)

    def display_diophantine_equation(self) -> None:
        self.formula = manim.MathTex(
            r"\text{丢番图方程}~a_1 P + a_2 G + a_3 C = k",
            tex_template=manim.TexTemplateLibrary.ctex,
            font_size=self.formula_font_size
        )
        self.formula.move_to(manim.ORIGIN + manim.UP * 2.0)

        self.play(manim.Write(self.formula, run_time=1.0))
        self.wait(5.0)

        gcd_content = manim.MathTex(
            r"\mathrm{gcd}(a_1, a_2, a_3) \mid a_1, a_2, a_3",
            tex_template=manim.TexTemplateLibrary.ctex,
            font_size=self.formula_font_size
        )
        gcd_content.next_to(self.formula, manim.DOWN)

        self.play(manim.Write(gcd_content, run_time=1.0))
        self.wait(5.0)

        gcd_content_transformed = manim.MathTex(
            r"\mathrm{gcd}(a_1, a_2, a_3) \mid a_1 P, a_2 G, a_3 C",
            tex_template=manim.TexTemplateLibrary.ctex,
            font_size=self.formula_font_size
        )
        gcd_content_transformed.next_to(self.formula, manim.DOWN)

        self.play(manim.Transform(gcd_content, gcd_content_transformed, run_time=1.0))
        self.wait(5.0)

        gcd_content_transformed = manim.MathTex(
            r"\mathrm{gcd}(a_1, a_2, a_3) \mid a_1 P + a_2 G + a_3 C",
            tex_template=manim.TexTemplateLibrary.ctex,
            font_size=self.formula_font_size
        )
        gcd_content_transformed.next_to(self.formula, manim.DOWN)

        self.play(manim.Transform(gcd_content, gcd_content_transformed, run_time=1.0))
        self.wait(5.0)

        gcd_content_transformed = manim.MathTex(
            r"\mathrm{gcd}(a_1, a_2, a_3) \mid k",
            tex_template=manim.TexTemplateLibrary.ctex,
            font_size=self.formula_font_size
        )
        gcd_content_transformed.next_to(self.formula, manim.DOWN)

        self.play(manim.Transform(gcd_content, gcd_content_transformed, run_time=1.0))
        self.wait(5.0)
        
        new_coefficients = manim.MathTex(
            r"\text{新系数}~\begin{cases}"
            r"a_1' = \frac{a_1}{\mathrm{gcd}(a_1, a_2, a_3)} \\"
            r"a_2' = \frac{a_2}{\mathrm{gcd}(a_1, a_2, a_3)} \\"
            r"a_3' = \frac{a_3}{\mathrm{gcd}(a_1, a_2, a_3)} \\"
            r"k' = \frac{k}{\mathrm{gcd}(a_1, a_2, a_3)} \\"
            r"k' \in \mathbb{N}, k' \in \left[ \frac{(S - 0.5)A}{\mathrm{gcd}(a_1, a_2, a_3)}, \frac{(S + 0.5)A}{\mathrm{gcd}(a_1, a_2, a_3)} \right) \\"
            r"\end{cases}",
            tex_template=manim.TexTemplateLibrary.ctex,
            font_size=self.formula_font_size
        )
        new_coefficients.next_to(self.formula, manim.DOWN * 2.0)

        C_constraints = manim.MathTex(
            r"\text{丢番图方程}~a_1' P + a_2' G + a_3' C = k'",
            tex_template=manim.TexTemplateLibrary.ctex,
            font_size=self.formula_font_size
        )
        C_constraints.move_to(manim.ORIGIN + manim.UP * 2.0)

        self.play(
            manim.Transform(gcd_content, new_coefficients, run_time=1.0),
            manim.Transform(self.formula, C_constraints, run_time=1.0)
        )
        self.wait(5.0)

        C_constraints = manim.MathTex(
            r"\text{丢番图方程}~a_1' P + a_2' G = k' - a_3' C",
            tex_template=manim.TexTemplateLibrary.ctex,
            font_size=self.formula_font_size
        )
        C_constraints.move_to(manim.ORIGIN + manim.UP * 2.0)

        self.play(manim.Transform(self.formula, C_constraints, run_time=1.0))
        self.wait(5.0)

        gcd_content_transformed = manim.MathTex(
            r"\mathrm{gcd}(a_1', a_2') \mid k' - a_3' C",
            tex_template=manim.TexTemplateLibrary.ctex,
            font_size=self.formula_font_size
        )
        gcd_content_transformed.next_to(self.formula, manim.DOWN)

        self.play(manim.Transform(gcd_content, gcd_content_transformed, run_time=1.0))
        self.wait(5.0)

        gcd_content_transformed = manim.MathTex(
            r"a_3' C \equiv k' \pmod{\mathrm{gcd}(a_1', a_2')}",
            tex_template=manim.TexTemplateLibrary.ctex,
            font_size=self.formula_font_size
        )
        gcd_content_transformed.next_to(self.formula, manim.DOWN)

        self.play(manim.Transform(gcd_content, gcd_content_transformed, run_time=1.0))
        self.wait(5.0)       

        gcd_content_transformed = manim.MathTex(
            r"C \equiv k' (a_3')^{-1} \pmod{\mathrm{gcd}(a_1', a_2')} \quad (a_3')^{-1} \text{为模逆元}",
            tex_template=manim.TexTemplateLibrary.ctex,
            font_size=self.formula_font_size
        )
        gcd_content_transformed.next_to(self.formula, manim.DOWN)

        self.play(manim.Transform(gcd_content, gcd_content_transformed, run_time=1.0))
        self.wait(5.0)              
        
        gcd_content_transformed = manim.MathTex(
            r"C = k' (a_3')^{-1} + \alpha \cdot \mathrm{gcd}(a_1', a_2')} \quad \alpha \in \mathbb{Z}",
            tex_template=manim.TexTemplateLibrary.ctex,
            font_size=self.formula_font_size
        )
        gcd_content_transformed.next_to(self.formula, manim.DOWN)

        self.play(manim.Transform(gcd_content, gcd_content_transformed, run_time=1.0))
        self.wait(5.0)

        new_coefficients = manim.MathTex(
            r"\text{新系数}~\begin{cases}"
            r"a_1'' = \frac{a_1'}{\mathrm{gcd}(a_1', a_2')} \\"
            r"a_2'' = \frac{a_2'}{\mathrm{gcd}(a_1', a_2')} \\"
            r"k'' = \frac{k' - a_3' C}{\mathrm{gcd}(a_1', a_2')} \\"
            r"\end{cases}",
            tex_template=manim.TexTemplateLibrary.ctex,
            font_size=self.formula_font_size
        )
        new_coefficients.next_to(self.formula, manim.DOWN * 2.0)

        C_constraints = manim.MathTex(
            r"\text{丢番图方程}~a_1'' P + a_2'' G = k''",
            tex_template=manim.TexTemplateLibrary.ctex,
            font_size=self.formula_font_size
        )
        C_constraints.move_to(manim.ORIGIN + manim.UP * 2.0)
        
        self.play(
            manim.Transform(gcd_content, new_coefficients, run_time=1.0),
            manim.Transform(self.formula, C_constraints, run_time=1.0)
        )
        self.wait(5.0)

        C_constraints = manim.MathTex(
            r"\text{C的约束}~E \geq C \geq \lceil \frac{E}{A - E + 1} \rceil",
            tex_template=manim.TexTemplateLibrary.ctex,
            font_size=self.formula_font_size
        )
        C_constraints.next_to(gcd_content, manim.DOWN)

        self.play(manim.Write(C_constraints, run_time=1.0))
        self.wait(5.0)

        E_constraint = manim.MathTex(
            r"\text{E的约束}~C \leq E \leq \lfloor \frac{(A + 1)C}{C + 1} \rfloor",
            tex_template=manim.TexTemplateLibrary.ctex,
            font_size=self.formula_font_size
        )
        E_constraint.move_to(C_constraints.get_center())

        self.play(manim.Transform(C_constraints, E_constraint, run_time=1.0))
        self.wait(5.0)
        self.play(manim.Unwrite(C_constraints, run_time=1.0))
        self.wait(5.0)

        constraints = manim.MathTex(
            r"\text{约束}~\begin{cases}"
            r"\min (a_1'', a_2'') \cdot C \leq \frac{k' - a_3' C}{\mathrm{gcd}(a_1', a_2')} \leq \max (a_1'', a_2'') \cdot \lfloor \frac{(A + 1)C}{C + 1} \rfloor \\"
            r"C = C_0 + \alpha \cdot \mathrm{gcd}(a_1', a_2') \quad C_0 = k' (a_3')^{-1} \\"
            r"a_1'' P + a_2'' G = k'' \\"
            r"C \leq E = P + G \leq \lfloor \frac{(A + 1)C}{C + 1} \rfloor \\"
            r"\end{cases}",
            tex_template=manim.TexTemplateLibrary.ctex,
            font_size=32
        )
        constraints.next_to(self.formula, manim.DOWN)

        self.play(manim.Transform(gcd_content, constraints, run_time=1.0))
        self.wait(5.0)

        constraints = manim.MathTex(
            r"\text{约束}~\begin{cases}"
            r"\min (a_1'', a_2'') \cdot C \leq \frac{k' - a_3' C}{\mathrm{gcd}(a_1', a_2')} \leq \max (a_1'', a_2'') \cdot \lfloor \frac{(A + 1)C}{C + 1} \rfloor \\"
            r"C = C_0 + \alpha \cdot \mathrm{gcd}(a_1', a_2') \quad C_0 = k' (a_3')^{-1} \\"
            r"\lceil \frac{a_1'' C - k''}{a_1'' - a_2''} \rceil \leq G \leq \lfloor \frac{a_1'' \lfloor \frac{(A + 1)C}{C + 1} \rfloor - k''}{a_1'' - a_2''} \rfloor \\"
            r"C \leq E = P + G \leq \lfloor \frac{(A + 1)C}{C + 1} \rfloor \\"
            r"\end{cases}",
            tex_template=manim.TexTemplateLibrary.ctex,
            font_size=32
        )
        constraints.next_to(self.formula, manim.DOWN)

        self.play(manim.Transform(gcd_content, constraints, run_time=1.0))
        self.wait(5.0)

        formula_transformed = manim.MathTex(
            r"\text{丢番图方程}~a_1'' P = k'' - a_2'' G",
            tex_template=manim.TexTemplateLibrary.ctex,
            font_size=self.formula_font_size
        )
        formula_transformed.move_to(self.formula.get_center())

        self.play(manim.Transform(self.formula, formula_transformed, run_time=1.0))
        self.wait(5.0)

        result = manim.MathTex(
            r"\text{解}~\begin{cases}"
            r"\min (a_1'', a_2'') \cdot C \leq \frac{k' - a_3' C}{\mathrm{gcd}(a_1', a_2')} \leq \max (a_1'', a_2'') \cdot \lfloor \frac{(A + 1)C}{C + 1} \rfloor \\"
            r"0 \leq G \leq \lfloor \frac{k''}{a_2''} \rfloor \\"
            r"\lceil \frac{a_1'' C - k''}{a_1'' - a_2''} \rceil \leq G \leq \lfloor \frac{a_1'' \lfloor \frac{(A + 1)C}{C + 1} \rfloor - k''}{a_1'' - a_2''} \rfloor \\"
            r"C = C_0 + \alpha \cdot \mathrm{gcd}(a_1', a_2') \quad C_0 = k' (a_3')^{-1} \\"
            r"P = P_0 + \beta \cdot a_2'' \quad P_0 = k'' (a_2'')^{-1} \\"
            r"G = \frac{k'' - a_2'' G}{a_1''} \\"
            r"\end{cases}",
            tex_template=manim.TexTemplateLibrary.ctex,
            font_size=32
        )
        result.next_to(self.formula, manim.DOWN)

        self.play(manim.Transform(gcd_content, result, run_time=1.0))
        self.wait(5.0)
