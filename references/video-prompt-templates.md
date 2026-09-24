# Image-to-Video Prompt Templates

默认提交方式：

```text
3×3 分镜关键帧图 + 一条完整视频提示词 → 一个 3-15 秒视频
```

不要默认把九宫格拆成三张关键帧、三条提示词、三段视频。

## 参考用途

| 标签 | 输入 | 控制 | 不控制 |
| --- | --- | --- | --- |
| GRID_SHOT_PLAN | 3×3 分镜关键帧图 | 九格顺序、构图方向、景别变化、信息点、节奏、**首帧构图** | 分镜边框、编号、纸纹、主体身份 |
| SUBJECT_IDENTITY | 产品图、角色图、场景图、物件图 | 轮廓、比例、材质、颜色、部件数量、角色识别特征 | 镜头运动、节奏、尚未发生的动作、**首帧构图** |
| STYLE_LIGHT | 风格/灯光参考 | 光比、色温、景深、氛围 | 主体结构、剧情结果 |
| CARRY_IN_ANCHOR | 上一段视频尾帧或终帧图 | 上一段结束状态 | 本段全部镜头设计 |

如果没有原产品图、角色图或场景图，让九宫格同时承担身份锚点，并在提示词中写清静态视觉锚点。

## 首帧锚定（必写）

当提交 `原图（SUBJECT_IDENTITY）+ 九宫格（GRID_SHOT_PLAN）` 两张图给视频模型时，模型默认倾向用 IMAGE 1 的构图和状态作为视频开头。必须在提示词里显式声明：**视频首帧对应九宫格第一格（左上），不是身份参考图**。

英文版锚定块（插入在 IMAGE 声明之后、Dynamic Description 之前）：

```text
First-frame anchor:
The first frame of this video must match Panel 1 (top-left keyframe) of IMAGE 2,
including its composition, subject pose, camera angle and background.
IMAGE 1 is an identity-only reference: it defines face, costume, materials and
proportions, but it never determines the opening composition, subject pose,
camera angle or background.
Do not open the video on IMAGE 1's framing.
```

中文版锚定块：

```text
首帧锚定：
视频第一帧必须对应 IMAGE 2（九宫格分镜图）左上角的第一格，
包括该格的构图、主体姿势、机位和背景。
IMAGE 1 只做身份参考：它决定脸型、服装、材质和比例，
但不决定开头构图、主体姿势、机位或背景。
不要以 IMAGE 1 的构图作为视频开头。
```

只有九宫格单图时不需要此块（首帧天然对应第一格），但仍建议写一句 `The video opens on Panel 1 of IMAGE 1.`。

## 交付结构（默认 H3 + 中文通用版）

`video_prompt.md` 默认输出两个完整可复制代码块，H3 版在前：

1. `## H3 版`：三字段结构（`integrated_multimodal_description` / `overall_soundscape` / `non_diegetic_music`），正文英文，对白用 `<d>[Chinese]</d>` 逐字内联。
2. `## 中文通用版`：纯中文时间线提示词，供不支持三字段结构的图生视频模型使用。
3. 两版共享同一组事实：时间码、对白逐字内容、静态锚点、红线。
4. 对白 / 台词两版都保持中文原文，不翻译。
5. 用户明确只要单版时，可只交付一版，但默认是 H3 + 中文通用。

## H3 三字段格式（默认）

`video_prompt.md` 的第一块默认就是 H3 三字段格式，面向 MiniMax H3 及兼容该结构的模型；同一条时间线一次成稿，中文通用版只是同一事实的另一种包装。

### 字段结构

```text
integrated_multimodal_description: [Shot 1] ... [Shot 2] At 00:03.500, ...

overall_soundscape: ...

non_diegetic_music: ... / N/A
```

1. `integrated_multimodal_description`：画面、动作、镜头、说话人、对白、戏内音，按时间线内联。
2. `overall_soundscape`：环境音、动作音、非人声；1-4 句；不重复对白。
3. `non_diegetic_music`：只给观众听的配乐；没有写 `N/A`。

### 镜头与切换

1. `[Shot 1]` 不写时间码，直接开始。
2. 后续镜头写 `[Shot N] At mm:ss.mmm, the camera cuts to ...`；时间码严格递增且在总时长内。
3. 普通剪辑只用标准短语（the camera cuts to / the shot switches to）；不默认叠化。
4. 运镜写成"类型 + 幅度 + 速度"的自然语句，例如 `The camera pushes in with small amplitude at slow speed`。

### 说话人与对白标记

1. 每个发声角色一个稳定 ID（`S1`、`S2`…），跨镜头不变；不发声的角色不发 ID。
2. 说话人首次出现时写声音画像：年龄感、性别、音高、音色、语速；画像、动作和语气写在 `<d>` 外面。
3. 对白用 `<d>[语言] 台词</d>`：标签里只写语言（中文用 `[Chinese]`），标签后只放逐字原文；不翻译、不改标点。
4. 台词横跨切点：两段连接处都加 `<scenetrans>`，并声明 `continues seamlessly across the cut`。
5. 台词被视频结尾截断：加 `<cutoff>`。
6. 画外音：用 `says in an off-screen voiceover`，`<d>` 之后立刻声明画面人物嘴唇保持闭合。

### 与首帧锚定的关系

若把九宫格首格图像单独导出并作为 H3 的 I2VA 首帧输入，第一行必须是：

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.
```

若只交付文字版三字段（T2VA），不需要该行；首格状态写进 `[Shot 1]` 开头。

## 通用中文版 · 完整视频提示词（兼容导出）

以下模板用于 `## 中文通用版` 代码块，或用户明确不要 H3 结构时的唯一交付。事实与 H3 版完全一致。

### 有原图 / 角色 / 场景参考

```text
Use IMAGE 1 as SUBJECT_IDENTITY.
Use IMAGE 2 as GRID_SHOT_PLAN and storyboard keyframe sheet.

IMAGE 1 defines the exact subject silhouette, proportions, materials, colors,
component count, visible identity cues and, for characters, face shape, hairstyle
and costume continuity.
IMAGE 2 defines a 3-15 second shot plan with nine keyframes. It determines shot
order, framing logic, information beats and rhythm.
IMAGE 2 is not a physical storyboard, comic page or object in the scene.
Do not render its borders, gutters, panel numbers, paper texture or layout.

First-frame anchor:
The first frame of this video must match Panel 1 (top-left keyframe) of IMAGE 2,
including its composition, subject pose, camera angle and background.
IMAGE 1 is an identity-only reference: it defines face, costume, materials and
proportions, but it never determines the opening composition, subject pose,
camera angle or background.
Do not open the video on IMAGE 1's framing.

Target duration: [3-15] seconds.
Aspect ratio: [16:9 / 9:16 / 1:1].
Goal: [product demo / narrative beat / comic drama / lifestyle clip].

Style & Mood: [PALETTE], [LIGHT DIRECTION], [MATERIAL RENDERING], [CAMERA CHARACTER].

Dynamic Description: interpret the nine keyframes as one continuous 3-15 second clip.
0.0-1.2s: [SHOT 01 start, one main change, end, camera].
1.2-2.4s: [SHOT 02 start, one main change, end, camera].
[Continue through SHOT 09 with the exact time ranges from storyboard_plan.md.]
Each major change must have a visible start, development and end.

Static Description: [SUBJECT IDENTITY], [COMPONENT COUNT], [COSTUME / MATERIAL],
[LOCATION ANCHORS], [KEY PROPS], [LIGHT DIRECTION], [FINAL STATE].

Ending: [FINAL STATE].
The subject must always match IMAGE 1, not a stylized copy from IMAGE 2.
Do not add new features, characters, text, watermarks or accessories unless requested.
No storyboard borders, panel numbers, comic page or paper texture in the video.
```

### 只有九宫格

```text
Use IMAGE 1 as GRID_SHOT_PLAN and storyboard keyframe sheet.
It also defines the subject identity, wardrobe/material, environment, lighting,
color palette and visible components for the whole clip.
It is a shot-planning sheet, not a physical storyboard, comic page or object.
Do not render its borders, gutters, panel numbers, paper texture or layout.
The video opens on Panel 1 (top-left keyframe) of this sheet.

Target duration: [3-15] seconds.
Aspect ratio: [16:9 / 9:16 / 1:1].
Goal: [product demo / narrative beat / comic drama / lifestyle clip].

Static visual anchors:
[SUBJECT IDENTITY], [COSTUME OR MATERIAL], [LOCATION], [TIME OF DAY],
[LIGHTING], [KEY OBJECTS], [OPENING COMPOSITION], [PALETTE].

Style & Mood: [PALETTE], [LIGHT DIRECTION], [MATERIAL RENDERING], [CAMERA CHARACTER].

Dynamic Description: interpret the nine keyframes as one continuous 3-15 second clip.
0.0-1.2s: [SHOT 01 start, one main change, end, camera].
[Continue through SHOT 09 with the exact time ranges from storyboard_plan.md.]

Static Description: [SUBJECT IDENTITY], [COMPONENT COUNT], [COSTUME / MATERIAL],
[LOCATION ANCHORS], [KEY PROPS], [LIGHT DIRECTION], [FINAL STATE].
Preserve subject identity, component count, material response and spatial logic.
No storyboard borders, panel numbers, comic page, text or watermark.
```

## 多片段 · 每段一条完整提示词

只有用户确认拆分后才使用。每个 `SEQ` 仍然是一条完整提示词，不是一个九格一条碎提示。

每个 `SEQ` 同样默认输出 H3 三字段版；`[Shot 1]` 的 Carry-in 状态写进 `integrated_multimodal_description` 开头，`Carry-out` 写进最后一个镜头的终点描述。

### SEQ 提示词骨架

```text
Use IMAGE 1 as GRID_SHOT_PLAN and storyboard keyframe sheet for SEQ-[NN].
It defines one continuous [3-15] second segment with nine keyframes.
It is not a physical storyboard, comic page or object.
Do not render its borders, gutters, panel numbers, paper texture or layout.

[Optional: Use IMAGE 0 as SUBJECT_IDENTITY.]
[Optional: Use previous final frame as CARRY_IN_ANCHOR.]

[If SUBJECT_IDENTITY present, insert the full First-frame anchor block here.
If only the grid, write: The video opens on Panel 1 of this sheet.]

Target duration: [3-15] seconds.
Aspect ratio: [16:9 / 9:16 / 1:1].
Sequence: SEQ-[NN].
Goal: [segment goal].

Carry-in state: [exact subject pose, wardrobe/material, location, props, light, camera implication].
Style & Mood: [GLOBAL PALETTE], [LIGHT DIRECTION], [MATERIAL RENDERING], [CAMERA CHARACTER].

Dynamic Description: follow the nine keyframes as one continuous segment.
0.0-1.2s: [SHOT 01 start, one main change, end, camera].
[Continue through SHOT 09 with the exact time ranges from storyboard_plan.md.]

Static Description: [SUBJECT IDENTITY], [COMPONENT COUNT], [COSTUME / MATERIAL],
[LOCATION ANCHORS], [KEY PROPS], [LIGHT DIRECTION], [FINAL STATE].
End state / Carry-out: [exact final state handed to the next sequence].

Global continuity:
- Keep [CHARACTER / PRODUCT IDENTITY] exactly consistent.
- Keep [COSTUME / MATERIAL], [KEY PROPS], [LIGHT DIRECTION] and [PALETTE] consistent.
- Do not invent new characters, props, locations, features, text or watermarks.
- No storyboard borders, panel numbers, comic page or paper texture.
```

## 连续性账本

每个 `SEQ` 的视频提示词前，先核对：

```markdown
## SEQ-[NN] Continuity
- Carry-in from previous:
  - 主体位置：
  - 朝向：
  - 手部/持物：
  - 服装/材质：
  - 场景：
  - 光线：
- 本段目标：
- 本段 Carry-out：
- 下一段 Carry-in：
- 转场方式：硬切 / 连续接 / 状态延续
```

规则：

1. 上一段 `Carry-out` 必须等于下一段 `Carry-in`。
2. 主体身份、服装/材质、关键道具、光线方向和调色板来自 Global Facts。
3. 每个九宫格第一格表现本段 `Carry-in`。
4. 每个九宫格最后一格表现本段 `Carry-out`。
5. 硬切允许改变景别和机位，不能改变未说明的世界状态。
6. 连续动作可让下一段第一格重复上一段终态，避免观众感到跳变。

## 反例

不要写：

```text
Camera slowly pans across the nine-grid storyboard.
```

不要写：

```text
The comic book page comes alive.
```

不要堆：

```text
Cinematic, stunning, masterpiece, best quality, highly detailed.
```

这些会让模型把分镜页当实物，或用无信息量的质量词稀释执行指令。
