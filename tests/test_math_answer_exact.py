from tools.math_answer_exact import grade_answer_verl


if __name__=="__main__":
    """
    1. solution_str must include '\\boxed{}' around the answer.
    """
    # example one, result: True
    print(grade_answer_verl("\\boxed{\\dfrac{1}{2}}", "0.5"))

    # example two, result: True
    print(grade_answer_verl("\\boxed{2x}", "x+x"))

    # example three, result: True
    print(grade_answer_verl("\\boxed{12}", "\\boxed{12\\text{ cm}}"))