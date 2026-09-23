# Image-to-Video Prompt Templates

默认提交方式：

```text
3×3 分镜关键帧图 + 一条完整视频提示词 → 一个 3-12 秒视频
```

不要默认把九宫格拆成三张关键帧、三条提示词、三段视频。

## 参考用途

| 标签 | 输入 | 控制 | 不控制 |
| --- | --- | --- | --- |
| GRID_SHOT_PLAN | 3×3 分镜关键帧图 | 九格顺序、构图方向、景别变化、信息点、节奏 | 分镜边框、编号、纸纹、主体身份 |
| SUBJECT_IDENTITY | 产品图、角色图、场景图、物件图 | 轮廓、比例、材质、颜色、部件数量、角色识别特征 | 镜头运动、节奏、尚未发生的动作 |
| STYLE_LIGHT | 风格/灯光参考 | 光比、色温、景深、氛围 | 主体结构、剧情结果 |
| CARRY_IN_ANCHOR | 上一段视频尾帧或终帧图 | 上一段结束状态 | 本段全部镜头设计 |

如果没有原产品图、角色图或场景图，让九宫格同时承担身份锚点，并在提示词中写清静态视觉锚点。

## 单九宫格 · 完整视频提示词

### 有原图 / 角色 / 场景参考

```text
Use IMAGE 1 as SUBJECT_IDENTITY.
Use IMAGE 2 as GRID_SHOT_PLAN and storyboard keyframe sheet.

IMAGE 1 defines the exact subject silhouette, proportions, materials, colors,
component count, visible identity cues and, for characters, face shape, hairstyle
and costume continuity.
IMAGE 2 defines a 3-12 second shot plan with nine keyframes. It determines shot
order, framing logic, information beats and rhythm.
IMAGE 2 is not a physical storyboard, comic page or object in the scene.
Do not render its borders, gutters, panel numbers, paper texture or layout.

Target duration: [3-12] seconds.
Aspect ratio: [16:9 / 9:16 / 1:1].
Goal: [product demo / narrative beat / comic drama / lifestyle clip].

Style & Mood: [PALETTE], [LIGHT DIRECTION], [MATERIAL RENDERING], [CAMERA CHARACTER].

Dynamic Description: interpret the nine keyframes as one continuous 3-12 second clip.
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

Target duration: [3-12] seconds.
Aspect ratio: [16:9 / 9:16 / 1:1].
Goal: [product demo / narrative beat / comic drama / lifestyle clip].

Static visual anchors:
[SUBJECT IDENTITY], [COSTUME OR MATERIAL], [LOCATION], [TIME OF DAY],
[LIGHTING], [KEY OBJECTS], [OPENING COMPOSITION], [PALETTE].

Style & Mood: [PALETTE], [LIGHT DIRECTION], [MATERIAL RENDERING], [CAMERA CHARACTER].

Dynamic Description: interpret the nine keyframes as one continuous 3-12 second clip.
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
It defines one continuous [3-12] second segment with nine keyframes.
It is not a physical storyboard, comic page or object.
Do not render its borders, gutters, panel numbers, paper texture or layout.

[Optional: Use IMAGE 0 as SUBJECT_IDENTITY.]
[Optional: Use previous final frame as CARRY_IN_ANCHOR.]

Target duration: [3-12] seconds.
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
