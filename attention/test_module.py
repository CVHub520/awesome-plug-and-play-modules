import torch

from se_layer import SELayer


def test_se_layer():
    # 定义测试数据
    x = torch.randn(2, 16, 32, 32)
    # 创建注意力模块
    selayer = SELayer(16)
    # 执行前向传播
    y = selayer(x)
    # 验证输出的形状是否正确
    assert y.shape == x.shape

