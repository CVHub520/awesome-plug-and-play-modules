<div>
  <p>
    <a align="center" href="https://zhuanlan.zhihu.com/p/379501097" target="_blank">
      <img width="100%" src="https://github.com/CVHub520/awesome-plug-and-play-modules/releases/download/v1.0/attention.png"></a>
  </p>
</div>
<br>

## 📑 目录

- [🚀 导读](#--导读-)
- [✨ 通道注意力](#-通道注意力-)
- [✨ 空间注意力](#-空间注意力-)
- [✨ 自注意力](#-自注意力-)
- [✨ 其它注意力](#-其它注意力-)


# 导读

视觉注意力机制是人类视觉所特有的一种大脑信号处理机制，而深度学习中的注意力机制正是借鉴了人类视觉的注意力思维方式。一般来说，人类在观察外界环境时会迅速的扫描全景，然后根据大脑信号的处理快速的锁定重点关注的目标区域，最终形成注意力焦点。该机制可以帮助人类在有限的资源下，从大量无关背景区域中筛选出具有重要价值信息的目标区域，帮助人类更加高效的处理视觉信息。

本仓库将重点围绕通道、空间、自注意力等多个维度介绍计算机视觉领域中相关的即插即用型注意力机制方法，力争用最简短的语言解释得更加通俗易懂，同时给出相应的源码供大家使用。

# 通道注意力

**通道注意力**旨在显示的建模出不同通道之间的相关性，通过网络学习的方式来自动获取到每个特征通道的重要程度，最后再为每个通道赋予不同的权重系数，从而来强化重要的特征抑制非重要的特征。

## [SELayer](https://github.com/CVHub520/awesome-plug-and-play-modules/blob/main/attention/se_layer.py) [🔝](#-目录)

> 标题：Squeeze-and-Excitation Networks</br>
> 发表：CVPR 2018</br>
> 论文：https://arxiv.org/abs/1709.01507

![](https://github.com/CVHub520/awesome-plug-and-play-modules/releases/download/v1.0/SE-Block.png)


# 空间注意力 [🔝](#-目录)

**空间注意力**旨在提升关键区域的特征表达，本质上是将原始图片中的空间信息通过空间转换模块，变换到另一个空间中并保留关键信息，为每个位置生成权重掩膜并加权输出，从而增强感兴趣的特定目标区域同时弱化不相关的背景区域。




# 自注意力 [🔝](#-目录)


# 其它注意力 [🔝](#-目录)



