# Prompt Architecture

九宫格生图和图生视频提示词都使用四段式结构。这个结构吸收产品动画流程中的“主体锁定、镜头序列、风格圣经、一致性红线”，并扩展到短剧、漫剧和生活方式片段。

## 一、3×3 分镜图提示词

### 1. Sheet Contract

写清版式契约：

```text
A 3x3 storyboard keyframe sheet for one continuous [3-15] second clip.
Read order: left-to-right, top-to-bottom.
Nine panels with clear borders and clean gutters.
```

必须包含：

1. `3x3`
2. `nine panels`
3. 阅读顺序
4. 边框和留白
5. 一个连续片段，不是九张海报

### 2. Subject / Story Bible

只写已确认事实：

```text
Subject identity:
[product silhouette, proportions, materials, component count]
or [character face shape, hairstyle, body type, costume, identifying marks]

Scene:
[location, time, weather, entry/exit, fixed anchors, light direction]

State:
[opening state, key prop, hands / movable part, ending state]
```

### 3. Nine-Panel Sequence

每格一句话，包含状态、主要变化和摄影意图：

```text
Panel 1 (top-left): [visible start state], [one main change], [camera intention].
Panel 2 (top-center): ...
...
Panel 9 (bottom-right): [final visible state], [hero hold / hook / consequence].
```

不要把每格写成独立插画说明。九格必须形成同一条时间链。

### 4. Style Bible & Red Lines

```text
Style:
[visual medium], [lighting], [palette], [camera language], [surface rendering].

Consistency red lines:
Keep the same subject identity, silhouette, proportions, materials, component count,
costume, hairstyle, spatial axis, light direction and palette across all nine panels.
Do not redesign the subject. Do not add unrequested characters, buttons, ports, screens,
accessories, text, logos or watermarks.
```

## 二、视频提示词

视频提示词不是把九宫格再解释一遍，而是把九格翻译成真实场景中的时间、动作和镜头。

### 1. Reference Roles

```text
Use IMAGE 1 as SUBJECT_IDENTITY.
Use IMAGE 2 as GRID_SHOT_PLAN.
```

如果只有九宫格：

```text
Use IMAGE 1 as GRID_SHOT_PLAN and subject identity.
```

### 1.5 First-Frame Anchor（双图提交时必写）

双图提交（身份图 + 九宫格）时，视频模型默认会把 IMAGE 1 的构图当视频开头。必须在 Reference Roles 之后立刻写首帧锚定，把开头权交给九宫格第一格：

```text
First-frame anchor:
The first frame of this video must match Panel 1 (top-left keyframe) of IMAGE 2,
including its composition, subject pose, camera angle and background.
IMAGE 1 is an identity-only reference: it defines face, costume, materials and
proportions, but it never determines the opening composition, subject pose,
camera angle or background.
Do not open the video on IMAGE 1's framing.
```

中文版同步翻译此块。只有九宫格单图时写一句 `The video opens on Panel 1 of this sheet.` 即可。

### 1.6 Delivery Format（默认 H3 + 中文通用版）

最终交付的视频提示词默认输出两个完整代码块，H3 版在前：

1. `## H3 版`：`integrated_multimodal_description` / `overall_soundscape` / `non_diegetic_music` 三字段，正文英文，镜头用 `[Shot N] At mm:ss.mmm`，运镜写“类型 + 幅度 + 速度”。
2. `## 中文通用版`：纯中文时间线提示词，供不支持三字段的模型。
3. 两版时间线、静态锚点、红线语义完全一致；对白两版都保持中文原文。

### 1.7 Speaker & Dialogue Markup

H3 版带对白时必须：

1. 每个发声角色一个稳定 ID（`S1`、`S2`…），跨镜头不变；声音画像（年龄感、性别、音高、音色、语速）写在首次出现处、`<d>` 外面。
2. 对白写 `<d>[Chinese] 台词</d>`：只放逐字原文，不翻译、不改标点。
3. 台词跨切点：两段连接处加 `<scenetrans>` 并声明声音连续；被结尾截断加 `<cutoff>`。
4. 画外音用 `says in an off-screen voiceover`，`<d>` 后立刻声明画面人物嘴唇保持闭合。

### 2. Style & Mood

写调色板、光线、材质、镜头气质。不要堆 `cinematic`、`masterpiece` 这类空词。

### 3. Dynamic Description

按时间写动作：

```text
0.0-1.2s: ...
1.2-2.4s: ...
...
```

每段写：

1. 起点。
2. 一个主要变化。
3. 终点。
4. 摄影机行为。
5. 观众此刻应该看清什么。

### 4. Static Description & Red Lines

写生成器必须知道的静态事实：

1. 主体身份和部件数量。
2. 服装或材质。
3. 场景锚点。
4. 关键道具和双手/可动部件。
5. 光线方向。
6. 禁止出现的内容。

结尾必须写：

```text
The grid is not a physical storyboard, comic page or object in the scene.
Do not render its borders, gutters, numbers, paper texture or layout.
```

## 提示词洁癖

不要进入可复制正文的内容：

1. 文件路径。
2. 内部 ID。
3. 评分表。
4. 流程说明。
5. 供应商参数。
6. “请”“我们”“接下来”这类对话语。
7. 与画面无关的质量承诺。

这些可以写在 Markdown 卡片里，不能让生成器当成画面内容。
