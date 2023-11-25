from typing import List

from transformers import pipeline

from curator import CuratorBase
from curator.types import TextClassification


class BARTZeroShotClassifier(CuratorBase):
    """Meta's BART model set up for zero shot classification.

    Refer to the `paper <https://arxiv.org/abs/1909.00161>`_ for model details.
    """
    name = 'BARTZeroShotClassifier'

    def __init__(self, device='cuda'):
        super().__init__()

        self.model = pipeline(
            'zero-shot-classification',
            model='facebook/bart-large-mnli',
            device=device)

    def classify(self, text: str, labels: List[str]) -> TextClassification:
        response = self.model(text, labels, multi_label=False)
        return TextClassification(
            classification=response['labels'][0],
            labels=response['labels'],
            scores=response['scores']
        )

    def __call__(self, text: str, labels: List[str]) -> TextClassification:
        return self.classify(text=text, labels=labels)
