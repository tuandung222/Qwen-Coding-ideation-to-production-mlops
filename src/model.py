# model.py - Hàm trả lời MCQ (giả lập)
def answer_mcq(question, choices):
    # TODO: Thay thế bằng inference thực tế với Qwen2.5-Coder-1.5B-Instruct
    # Ở đây chỉ chọn ngẫu nhiên một đáp án để demo
    import random
    if not choices:
        return None
    return random.choice(choices)
