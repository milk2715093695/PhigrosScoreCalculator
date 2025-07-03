# Phigros 分数逆向计算器

本项目实现了一个 **Phigros 分数逆向计算器**，用于计算在给定谱面物量和目标分数的情况下，所有可能达到该分数的击打组合。

- **纯 Python 实现**，不依赖任何外部包。
- 包含与本项目相关的 Manim 视频源码，视频演示了计算思路和过程。
- 运行视频部分需要安装 [Manim](https://docs.manim.community/)。

---

## 功能介绍

Phigros 的分数计算机制基于判定分和连击分，最终结果通过四舍五入计算得到。  
本项目不仅计算单一解，还能列出所有满足条件的击打组合，方便对控分机制的研究与分析。

---

## 目录结构

- `calculator.py`：核心计算脚本，实现分数逆向计算功能，仅 100 行，思路很简单，运行一次求解 1ms 左右，无需外部库可直接运行。
- `media/`：视频相关的素材文件夹。
- `video.py`：Manim 视频的源码。
- `LICENSE`、`README.md`：项目许可及说明文件。

---

## 使用方法

1. 克隆仓库：

```bash
git clone https://github.com/milk2715093695/PhigrosScoreCalculator.git
cd PhigrosScoreCalculator
````

2. 运行计算器：

```bash
python calculator.py
```

3. （可选）运行视频演示：

请确保安装了 Manim，详情见官方文档。
执行：

```bash
manim -pql video/你的视频脚本.py
```

---

## 许可证

本项目采用 MIT 许可证，详情见 `LICENSE` 文件。
