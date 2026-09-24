---
name: nine-grid-storyboard
description: Turn a reference image, script excerpt, or story beat into a production-ready 3x3 storyboard keyframe sheet and complete image-to-video prompt for one 3-12 second clip. For longer or more complex requests, create an approved multi-sequence split with one 3x3 sheet and prompt per sequence. Supports product demos, short drama, comic drama, object animation, and lifestyle clips; does not generate media or call providers.
license: MIT
---

# Nine-Grid Storyboard

把参考图、剧本片段或故事拍点，变成一条可直接提交图生视频的九宫格工作包。

默认规则：

```text
一个片段 = 一张 3×3 分镜关键帧图 + 一条完整视频提示词
片段时长 = 3-12 秒
```

3×3 分镜图里的九个格子，就是这个片段的九个分镜关键帧。它们共同服务同一个 3-12 秒片段，不是九条独立视频，也不是三张独立关键帧。

默认提交方式：

```text
生成的 3×3 分镜图 + 对应完整视频提示词
```

如果用户还提供了产品图、角色图或场景图，可以在模型支持时把它们作为身份参考一起提交；但不要默认把三张关键帧和三条提示词拆成三段视频。

## Quick Start

```text
用 $nine-grid-storyboard 处理这张产品图。我要一条 8 秒 16:9 的产品视频：暗场亮相，展示材质和按键，最后英雄定格。
```

```text
用 $nine-grid-storyboard 处理这段短剧分场：雨夜面馆，女孩推门、停住、看见熟客。目标 10 秒，9:16。输出 3×3 分镜图提示词和完整视频提示词。
```

```text
我想做一条 40 秒的漫剧片段：主角进入旧书店，发现一封没寄出的信，最后决定寄出。请先给拆分方案。
```

## 时长与拆分规则

### 单个九宫格

满足全部条件时只做一个 3×3 分镜图：

1. 目标片段在 `3-12 秒`。
2. 一个主要空间或连续空间。
3. 主体状态变化可以由九格清楚承载。
4. 没有必要的时间跳跃、大范围转场或复杂多线动作。

九格时长不要求平均。可以在 `storyboard_plan.md` 里写每格大致占比，例如 `0-1s`、`1-2.5s`、`2.5-4s`，总和必须等于片段时长。

### 必须先讨论拆分

出现任一情况时，不要直接生成一个九宫格：

1. 用户要求超过 `12 秒`。
2. 动作链过长，九格无法清晰承载。
3. 有多个强转折、多地点、明显时间跳跃。
4. 产品开合/装配/使用流程太复杂。
5. 目标模型单次上限低于用户需求。

先输出 `Master Breakdown Proposal`，和用户确认：

```markdown
# Master Breakdown Proposal

- 总时长：
- 总目标：
- 全局主体：
- 全局风格：
- 分段数：

## SEQ-01
- 时长：3-12s
- 目标：
- Carry-in：
- 九格职责：
- Carry-out：
- 转 SEQ-02 的方式：硬切 / 连续接 / 状态延续

## SEQ-02
...
```

用户确认后，才为每个 `SEQ` 生成一个独立九宫格和一条完整视频提示词。

## 输入

### 必需

至少提供一项：

1. 参考图：产品图、物件图、角色图、场景图、道具图或风格图。
2. 剧本片段、小说段落、分场梗概。
3. 明确的片段意图。

### 常用可选

| 输入 | 用途 |
| --- | --- |
| 时长 | 必须落到 `3-12s`；超过时先拆分。 |
| 画幅 | 默认 `16:9`；抖音竖屏可用 `9:16`。 |
| 模式 | 产品 / 短剧 / 漫剧 / 生活方式。未说明时根据素材推断。 |
| 卖点/情绪 | 决定九格节奏。 |
| 必须出现的画面 | 写入必须满足集合。 |
| 禁止项 | 文字、水印、人物、新增部件、血腥、品牌模仿等。 |
| 目标模型 | 如 Seedance、Kling、Veo、H3；不确定时保持通用提示词。 |

## 模式路由

| 模式 | 判断信号 | 核心问题 |
| --- | --- | --- |
| `product` | 产品图、物件图、卖点、功能演示 | 主体身份、材质、细节、功能动作、英雄定格。 |
| `narrative` | 剧本、人物、冲突、台词、情绪转折 | 空间、人物状态、欲望、压力、转折、后果。 |
| `comic` | 漫剧、漫画页、分格、动态分镜 | 九格阅读顺序、分格边界、角色一致性、动作衔接。 |
| `lifestyle` | 旅行、空间、日常、氛围 | 场景节奏、地方感、注意力转移、记忆画面。 |

读取对应参考：

1. 产品/物件：[product-intake.md](references/product-intake.md)。
2. 短剧/剧情/漫剧：[narrative-intake.md](references/narrative-intake.md)。
3. 九格节奏：[storyboard-template.md](references/storyboard-template.md)。
4. 短剧/漫剧节奏：[narrative-template.md](references/narrative-template.md)。
5. 参考图边界：[reference-contract.md](references/reference-contract.md)。
6. 覆盖与时间：[coverage-and-timing.md](references/coverage-and-timing.md)。
7. 提示词结构：[prompt-architecture.md](references/prompt-architecture.md)。
8. 视频提示词：[video-prompt-templates.md](references/video-prompt-templates.md)。
9. 多片段连贯：[multi-sequence-continuity.md](references/multi-sequence-continuity.md)。
10. 审查阶段门：[review-gates.md](references/review-gates.md)。
11. 评分表：[review-rubric.md](references/review-rubric.md)。
12. 示例：[examples.md](references/examples.md)。

## 工作流

### 1. 建立 Clip Brief

```markdown
# Clip Brief

- 模式：product / narrative / comic / lifestyle
- 片段意图：
- 时长：3-12s
- 画幅：
- 风格：
- 必须出现：
- 禁止出现：
- 结尾画面：
- 是否需要拆分：否 / 是
```

缺失项可以按合理默认值补齐，但不要发明用户没有授权的品牌、功能、人物关系或剧情。

### 2. 采集事实

根据模式生成 `subject_facts.md` 或 `narrative_facts.md`。

只记录可见、剧本文本支持或用户确认的事实：

1. 产品：轮廓、比例、材质、颜色、按钮/接口数量、识别特征。
2. 角色：脸型、发型、体型、服装、状态、位置、朝向、持物。
3. 场景：地点、时间、光源、入口出口、固定锚点。
4. 动作：起点状态、主要变化、终点状态。

看不清、未确认的内容标为“未确认”，不要编造。

用户提供真实参考图时，按 [reference-contract.md](references/reference-contract.md) 建立槽位：每张图写清顺序、用途、控制范围、不得控制范围和观察状态。没有真实参考图时，不要伪造 `REF`；先输出九宫格图提示词，或把静态视觉锚点完整写进文生视频正文。

### 3. 设计九个分镜关键帧

每格必须写成：

```markdown
### SHOT-01 · <短名>
- 来源/覆盖：
- 职责：
- 目的：
- 时间范围：
- 起点：
- 动作：
- 终点：
- 摄影机：
- 情绪/信息变化：
- 风险：
- 参考用途：
- 声音/台词：
```

先按 [coverage-and-timing.md](references/coverage-and-timing.md) 建立覆盖表和动作账本，再写九格。每个用户必须出现的信息都要有承担格子；每个关键动作只有一个主要落实格子。

九格共同覆盖完整片段：

1. `SHOT-01` 通常建立主体、空间或失衡。
2. 中间格展开材质、动作、反应、功能或冲突。
3. `SHOT-09` 通常收束、定格或留钩子。
4. 相邻两格要有可见变化，不要只是换个角度重复。
5. 前一格终点应能接到后一格起点。

### 4. 输出 3×3 分镜图提示词

读取 [storyboard-template.md](references/storyboard-template.md) 和 [prompt-architecture.md](references/prompt-architecture.md)，按四段式生成可直接复制的提示词：

```text
Sheet Contract → Subject / Story Bible → Nine-Panel Sequence → Style Bible & Red Lines
```

提示词必须明确：

1. 这是一张 3×3 storyboard keyframe sheet。
2. 九格按左到右、上到下阅读。
3. 九格共同覆盖同一个 3-12 秒片段。
4. 每格之间有清晰边框和留白。
5. 九格共享同一主体身份、材质、色彩、光线和空间逻辑。
6. 短剧/漫剧角色不能换脸、换装、换体型。
7. 产品不能新增按钮、接口、屏幕或功能。

如果当前环境有可用图像生成工具，先展示提示词，用户确认后生成 `storyboard_3x3.png`；否则只交付提示词。

### 5. 输出完整视频提示词

读取 [video-prompt-templates.md](references/video-prompt-templates.md) 和 [prompt-architecture.md](references/prompt-architecture.md)。

默认交付一条完整提示词，用于：

```text
3×3 分镜图 + 完整视频提示词 → 一个 3-12s 视频
```

提示词必须写清：

1. 九宫格是分镜关键帧表，不是实体漫画书。
2. 不要让镜头扫过九宫格。
3. 视频中不得出现分镜边框、编号、纸纹或 comic page。
4. 按九格顺序展开时间、动作和镜头。
5. 每个主要变化都要有起点和终点。
6. 最后必须落到用户确认的结尾画面。

视频正文按四段写：

```text
Reference Roles → Style & Mood → Dynamic Description → Static Description & Red Lines
```

`Dynamic Description` 必须带时间码，例如 `0.0-1.2s`。参考图已经表达的外观不要重复堆砌；运动正文重点写起点、主要变化、终点、接触、方向、顺序、摄影机和声音。

如果模型支持额外身份参考，可同时提交产品图、角色图或场景图；但不要把九格拆成三张关键帧、三条提示词、三段视频。

## 多片段连续性

只有用户确认拆分后，才创建多个九宫格。

拆分方案、Carry 状态、转场类型和生成顺序按 [multi-sequence-continuity.md](references/multi-sequence-continuity.md) 执行。

每个 `SEQ` 仍遵守 `3-12s` 规则：

```text
SEQ-01：3-12s + SEQ-01 3×3 分镜图 + SEQ-01 完整视频提示词
SEQ-02：3-12s + SEQ-02 3×3 分镜图 + SEQ-02 完整视频提示词
...
```

### 连续性账本

在 `master_breakdown.md` 中维护：

```markdown
# Master Breakdown

## Global Facts
- 主体身份：
- 服装/材质：
- 场景：
- 光线：
- 风格：
- 关键道具：
- 禁止项：

## SEQ-01
- 时长：3-12s
- Carry-in：角色站在门口，伞收在右手，地面湿。
- 目标：看见熟悉的名字。
- Carry-out：角色停在桌前，视线锁定信件。
- 转 SEQ-02：状态延续。

## SEQ-02
- Carry-in：角色停在桌前，视线锁定信件。
- ...
- Carry-out：...
```

规则：

1. 上一段 `Carry-out` 必须等于下一段 `Carry-in`。
2. 主体身份、服装、材质、光线方向和关键道具来自 `Global Facts`。
3. 每个九宫格的第一格要表现本段 `Carry-in`。
4. 每个九宫格的最后一格要表现本段 `Carry-out`。
5. 硬切允许改变景别和机位，但不能改变未说明的世界状态。
6. 连续动作允许把上一段尾状态作为下一段首格参考。
7. 如果工具支持上一段视频尾帧，可将其作为可选身份/状态锚点；但主流程仍然是“本段九宫格 + 本段完整提示词”。

## 生成与交付

如果运行环境有可用图像生成工具：

1. 展示九格计划。
2. 用户确认后生成 `storyboard_3x3.png`。
3. 按 [review-gates.md](references/review-gates.md) 审查九宫格；未通过时先修图，不进入视频。
4. 输出完整视频提示词（中文版 + English version，对白文本保持中文；双图提交时必须包含首帧锚定块）。
5. 用户确认后再交给可用视频工具。

如果没有图像生成工具，交付九格计划和提示词，并把 `storyboard_3x3.png` 标记为“待生成”。

## 输出结构

### 单片段

```text
nine_grid/
├── clip_brief.md
├── subject_facts.md
├── storyboard_plan.md
├── storyboard_image_prompt.md
├── storyboard_3x3.png
├── video_prompt.md
└── qa_checklist.md
```

短剧/漫剧可把 `subject_facts.md` 命名为 `narrative_facts.md`。

### 多片段

```text
nine_grid/
├── clip_brief.md
├── subject_facts.md
├── master_breakdown.md
├── sequence_01/
│   ├── storyboard_plan.md
│   ├── storyboard_image_prompt.md
│   ├── storyboard_3x3.png
│   └── video_prompt.md
├── sequence_02/
│   └── ...
└── qa_checklist.md
```

## 质量检查

按 [review-gates.md](references/review-gates.md) 分阶段审查。除此之外，交付前检查：

交付前检查：

1. 单个片段时长在 `3-12s`。
2. 九格 ID 连续，无重复、无缺失。
3. 九格共同覆盖完整片段，不缺开始、中间或结尾。
4. 每格有独立职责，不只是“换个角度再看一遍”。
5. 每格有起点、动作、终点。
6. 3×3 图提示词可直接复制。
7. 视频提示词可直接复制。
8. 没有把“镜头扫过九宫格”写进视频提示词。
9. 多片段时，所有 `Carry-out → Carry-in` 状态一致。
10. 没有发明未授权的品牌、功能、角色关系或剧情。
11. 双图提交（身份图 + 九宫格）时，视频提示词包含首帧锚定：视频第一帧对应九宫格第一格，不是身份参考图的构图。
12. 视频提示词同时提供中文版和英文版；对白文本两版都保持中文。

## 边界

- 本 Skill 不直接调用外部生图或生视频 API；生成动作交由当前环境可用工具或用户自己的工具完成。
- 不替代高精度商业三维；适合前期提案、方向测试、轻量视频。
- 不处理真实人物肖像、品牌模仿、侵权资产。
- 如果用户需要完整短剧剧本、整集分镜或成片生产，优先使用可用的 `short-drama-storyboard`、`short-drama-video-prompts`、`short-drama-produce`。
- 本 Skill 不默认输出 A/B/C 实验表；方法对比只属于项目研究，不属于创作交付。

## 完成标准

1. 用户拿到明确的片段 Brief。
2. 单片段时，拿到九格分镜计划、3×3 图提示词和完整视频提示词。
3. 多片段时，拿到已确认的 Master Breakdown，以及每个 `SEQ` 的九宫格工作包。
4. 每个可提交片段都有对应 3×3 分镜图或“待生成”标记。
5. 每个可提交片段都有中文版和英文版各一条完整视频提示词（对白保持中文）。
6. 没有把三张关键帧和三条视频提示词作为默认交付。
