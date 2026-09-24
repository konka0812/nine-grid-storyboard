# Nine-Grid Storyboard

把一张参考图、一段剧本、一个故事拍点或一个产品卖点，变成可直接用于图生视频的 **3×3 分镜关键帧工作包**。

默认规则：

```text
一个 3-15 秒片段
= 一张 3×3 分镜关键帧图
+ 一条完整图生视频提示词
```

它不是把九宫格当漫画书让镜头扫过去，而是把九格当作视频模型的 **视觉 DNA、镜头顺序和节奏参考**。生成的视频应呈现真实场景或产品动画，而不是出现分镜边框、编号或纸纹。

两个关键交付特性：

- **首帧锚定**：双图提交（身份图 + 九宫格）时，视频提示词强制声明**视频第一帧对应九宫格第一格**，而不是身份参考图的构图——避免视频模型默认用原图开场。
- **双语提示词**：视频提示词默认同时输出中文版和 English Version（对白文本两版都保持中文），可直接复制到不同偏好的模型。

## 支持场景

| 模式 | 适合 |
| --- | --- |
| `product` | 产品图、物件动画、功能演示、电商短视频。 |
| `narrative` | 短剧、剧情片段、小说可视化、预告片。 |
| `comic` | 漫剧、漫画页、动态分镜。 |
| `lifestyle` | 旅行、空间、日常记录、氛围短片。 |

## 安装

### Codex Skill

```powershell
git clone --depth 1 https://github.com/konka0812/nine-grid-storyboard.git "$env:USERPROFILE\.codex\skills\nine-grid-storyboard"
```

安装后开启新的 Codex 对话，即可使用。

### 手动安装

```powershell
git clone --depth 1 https://github.com/konka0812/nine-grid-storyboard.git
Copy-Item -Recurse -Force nine-grid-storyboard "$env:USERPROFILE\.codex\skills\nine-grid-storyboard"
```

Linux / macOS：

```bash
git clone --depth 1 https://github.com/konka0812/nine-grid-storyboard.git
mkdir -p ~/.codex/skills
cp -R nine-grid-storyboard ~/.codex/skills/
```

## 使用

### 产品片段

```text
用 $nine-grid-storyboard 处理这张产品图。
我要一条 8 秒 16:9 的产品视频：
暗场亮相，展示材质和按键，最后英雄定格。
```

### 短剧片段

```text
用 $nine-grid-storyboard 处理这段短剧分场：
雨夜面馆，女孩推门、停住、看见熟客。
目标 10 秒，9:16。
输出 3×3 分镜图提示词和完整视频提示词。
```

### 超过 15 秒

```text
我想做一条 40 秒的漫剧片段：
主角进入旧书店，发现一封没寄出的信，最后决定寄出。
请先给拆分方案。
```

Skill 会先输出 `Master Breakdown Proposal`，和你确认后再拆成多个 `SEQ`。每个 `SEQ` 仍控制在 `3-15 秒`，并各自生成一张九宫格和一条完整视频提示词。

## 默认输出

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

如果拆分为多片段：

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

## 工作流

1. **Clip Brief**：确认模式、时长、画幅、目标、必须出现和禁止出现的内容。
2. **事实采集**：记录产品结构、角色身份、场景、动作和参考图边界。
3. **覆盖与时间**：建立覆盖表、动作账本和连续的 `3-15s` 时间链。
4. **九格分镜**：每格写清来源、职责、起点、动作、终点、摄影机、风险和参考用途。
5. **3×3 图提示词**：按“版式契约、主体/故事事实、九格序列、风格与红线”四段式输出。
6. **完整视频提示词**：把九格翻译成真实场景中的时间、动作、镜头和状态变化。
7. **审查阶段门**：先审事实和分镜，再审九宫格，最后才进入视频生成。

## 多片段连贯

多个九宫格之间通过连续性账本衔接：

```text
SEQ-01 Carry-out = SEQ-02 Carry-in
```

每段记录：

```text
主体位置
朝向
视线
双手 / 持物
服装或材质
关键道具状态
光线方向
转场方式
```

转场类型支持：

| 类型 | 说明 |
| --- | --- |
| 连续接 | 下一格第一画面重复上一段结束状态。 |
| 硬切 | 世界状态不变，允许景别和机位变化。 |
| 省略 | 时间跳过，必须有可见状态差异和可理解因果。 |
| 换场 | 地点或时间改变，但身份、道具和风格来自全局事实。 |

## 参考图原则

每张参考图都会声明：

```text
顺序
用途
能控制什么
不能控制什么
观察状态
```

例如：

```markdown
REF-01 · 顺序 1 · `input/product.png`《产品正面图》
- 用途：主体身份
- 控制：轮廓、长宽比、主体材质、主色、可见按钮/接口数量
- 不得控制：背景、镜头运动、尚未发生的功能动作
- 观察状态：已确认
```

没有真实参考图时，不伪造参考；先输出九宫格图提示词，或在文生视频正文中写完整静态视觉锚点。

### 首帧锚定

当 `原图（SUBJECT_IDENTITY）+ 九宫格（GRID_SHOT_PLAN）` 一起提交给视频模型时，模型会把 IMAGE 1 的构图当成视频开头。所以双图提交的视频提示词必须包含首帧锚定块：

```text
First-frame anchor:
The first frame of this video must match Panel 1 (top-left keyframe) of IMAGE 2,
including its composition, subject pose, camera angle and background.
IMAGE 1 is an identity-only reference: it defines face, costume, materials and
proportions, but it never determines the opening composition, subject pose,
camera angle or background.
Do not open the video on IMAGE 1's framing.
```

九宫格第一格就是片段的开场镜头；身份图里的姿势、机位和背景只是身份快照，不是开场状态。

## 校验

校验九格分镜 Markdown：

```bash
python scripts/validate_storyboard.py path/to/storyboard_plan.md
```

检查项：

1. 是否正好 9 个 `SHOT`。
2. ID 是否连续。
3. 必填字段是否齐全。
4. 时间范围是否连续。
5. 总时长是否在 `3-15` 秒。
6. 是否出现“镜头扫过九宫格”这类错误指令。

## 文件结构

```text
nine-grid-storyboard/
├── SKILL.md
├── README.md
├── LICENSE
├── agents/
│   └── openai.yaml
├── references/
│   ├── product-intake.md
│   ├── narrative-intake.md
│   ├── narrative-template.md
│   ├── storyboard-template.md
│   ├── reference-contract.md
│   ├── coverage-and-timing.md
│   ├── prompt-architecture.md
│   ├── video-prompt-templates.md
│   ├── multi-sequence-continuity.md
│   ├── review-gates.md
│   ├── review-rubric.md
│   └── examples.md
└── scripts/
    └── validate_storyboard.py
```

## 边界

- 本 Skill 不绑定某一家生图或生视频服务商。
- 不直接调用外部 API，不保存 API Key。
- 不替代高精度商业三维；适合前期提案、方向测试和轻量短视频。
- 不处理真实人物肖像、品牌模仿或侵权资产。
- 完整短剧剧本、整集分镜和成片生产建议配合 `short-drama-*` 系列 Skill 使用。

## License

MIT
