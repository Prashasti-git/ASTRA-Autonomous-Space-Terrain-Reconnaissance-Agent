"""
Python Environment Import Smoke Tests
Verifies core scientific, machine learning, and computer vision libraries are installed and importable.
"""
import pytest


def test_numpy_import():
    import numpy as np
    arr = np.array([1, 2, 3])
    assert arr.sum() == 6


def test_scipy_import():
    import scipy
    assert scipy.__version__ is not None


def test_pandas_import():
    import pandas as pd
    df = pd.DataFrame({"a": [1, 2]})
    assert len(df) == 2


def test_matplotlib_import():
    import matplotlib
    assert matplotlib.__version__ is not None


def test_opencv_import():
    import cv2
    assert cv2.__version__ is not None


def test_torch_import():
    import torch
    import torchvision
    tensor = torch.tensor([1.0, 2.0])
    assert tensor.shape == torch.Size([2])
    assert torchvision.__version__ is not None
