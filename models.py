import dspy

class Signature(dspy.Signature):
    """Detect if two code samples are plagiarized. In plagiarized field answer only : Yes if the code samples are plagiarized, No otherwise. In explenation field add the reason why the code samples are/ are not plagiarized."""

    code_sample_1 = dspy.InputField(desc="The first code sample to compare")
    code_sample_2 = dspy.InputField(desc="The second code sample to compare")
    explanation = dspy.OutputField(
        desc="Explanation or reason why the code samples are/ are not plagiarized"
    )
    plagiarized = dspy.OutputField(
        desc="Yes/No indicating if code samples are plagiarized"
    )

class CoT(dspy.Module):
    def __init__(self) -> None:
        super().__init__()
        self.prog = dspy.ChainOfThought(Signature)

    def forward(self, code_sample_1: str, code_sample_2: str) -> Signature:
        return self.prog(code_sample_1=code_sample_1, code_sample_2=code_sample_2)