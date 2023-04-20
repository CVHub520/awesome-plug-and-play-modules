import torch

from se_layer import SELayer
from eca_layer import ECALayer


#---------- Channel Attention ---------- #

def test_se_layer():

    x = torch.randn(2, 16, 64, 64)
    selayer = SELayer(16)
    y = selayer(x)

    assert y.shape == x.shape

def test_eca_layer():

    x = torch.randn(2, 16, 64, 64)
    selayer = ECALayer(3)
    y = selayer(x)

    assert y.shape == x.shape

