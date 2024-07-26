import dspy
import requests
import json

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


def stop_model(
    model: str,
    url: str,
    prompt: str = "STOP! Hammer time",
    keep_alive: int = 0,
    stream: bool = False,
) -> bool:
    if "ollama" in model:
        model = "-".join(model.split("-")[1:])
    url = url + "/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "keep_alive": keep_alive,
        "stream": stream,
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    if response.status_code == 200:
        return True
    else:
        raise Exception(f"Failed to stop model: {response.text}")

class SignatureOld(dspy.Signature):
    """Detect if two code samples are plagiarized. In plagiarized field answer only : Yes if the code samples are plagiarized, No otherwise. In explenation field add the reason why the code samples are/ are not plagiarized."""

    code_sample_1 = dspy.InputField(desc="The first code sample to compare")
    code_sample_2 = dspy.InputField(desc="The second code sample to compare")
    explanation = dspy.OutputField(
        desc="Explanation or reason why the code samples are/ are not plagiarized"
    )
    plagiarized = dspy.OutputField(
        desc="Yes/No indicating if code samples are plagiarized"
    )

class CoT_Old(dspy.Module):
    def __init__(self) -> None:
        super().__init__()
        self.prog = dspy.ChainOfThought(SignatureOld)

    def forward(self, code_sample_1: str, code_sample_2: str) -> SignatureOld:
        return self.prog(code_sample_1=code_sample_1, code_sample_2=code_sample_2)



