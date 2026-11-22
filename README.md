# pairwise-cloud-phase-multiscatter

## 领域

游戏、图形与多媒体

## 主题

云层多重散射

## 说明

双瓣 HG 相位、多次散射补偿与分段光学厚度。

初始状态下 `render/cloud_phase_multiscatter.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
