from typing import List

from curator import CuratorBase, GPT


class GPTZeroShotClassification(CuratorBase):
    def __init__(self, classes: List[str]):
        super().__init__()
        self.gpt = GPT(instructions=f'Classify the text into one of the following classes: {classes}')

    def classify(self, text: str):
        return self.gpt.message(text).text
