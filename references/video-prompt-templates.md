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

## 双语交付

`video_prompt.md` 默认输出**中文版 + English version** 两个完整可复制代码块：

1. 两版内容语义一致：同一条时间线、同一组静态锚点、同一套红线。
2. 对白 / 台词文本两个版本都保持中文原文，不翻译。
3. 两版都放在独立代码块中，标注 `## 中文版` 和 `## English Version`。
4. 用户明确只要单语时，可只交付一版，但默认是双语。

## 单九宫格 · 完整视频提示词

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
