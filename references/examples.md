# Worked Examples

这些例子只示范结构，不替代用户事实。使用时必须替换为主体、场景、动作和禁止项。

## Example 1 · 8 秒产品片段

### Clip Brief

```markdown
- 模式：product
- 时长：8s
- 画幅：16:9
- 目标：暗场亮相，确认主体与部件，展示开合，英雄定格。
- 必须出现：正面轮廓、3 个按键、1 个充电口、盖子打开。
- 禁止：新增按键、文字、水印、人物、logo。
```

### Nine-Beat Plan

| 格 | 时间 | 职责 |
| --- | --- | --- |
| 01 | 0.0-0.8s | 暗场轮廓亮相。 |
| 02 | 0.8-1.6s | 侧光建立材质。 |
| 03 | 1.6-2.4s | 全貌与比例。 |
| 04 | 2.4-3.2s | 主材质特写。 |
| 05 | 3.2-4.0s | 3 个按键与充电口可见。 |
| 06 | 4.0-5.2s | 盖子从关闭到开启。 |
| 07 | 5.2-6.0s | 使用尺度。 |
| 08 | 6.0-6.8s | 回到主体。 |
| 09 | 6.8-8.0s | 英雄定格。 |

### Storyboard Image Prompt Shape

```text
A clean 3x3 storyboard keyframe sheet for one continuous 8 second product video.
Read order: left-to-right, top-to-bottom. Nine separate panels with clear borders and clean gutters.

Subject identity: [product silhouette, proportions, primary material, secondary material,
primary color, three buttons, one charging port].
Scene: dark display podium, soft left key light, cool rim light, no background clutter.

Panel 1 (top-left): 0.0-0.8s, product silhouette emerges from darkness, slow dolly-in.
Panel 2 (top-center): 0.8-1.6s, side light reveals surface response, fixed wide shot.
[Continue through Panel 9.]

Style: professional product previsualization, controlled lighting, muted palette,
thin ink borders, clean gutters.
Red lines: same product identity, proportions, materials, three buttons and one charging port
in every panel; no new features, text, logos, watermarks or people.
```

### Video Prompt Shape

```text
Use IMAGE 1 as SUBJECT_IDENTITY.
Use IMAGE 2 as GRID_SHOT_PLAN.

Style & Mood: dark product stage, soft left key light, cool rim light, controlled material rendering.

Dynamic Description:
0.0-0.8s: silhouette emerges, camera slowly dollies in.
0.8-1.6s: side light moves across the surface, camera holds wide.
[Continue through 8.0s with the exact nine-shot time ranges.]

Static Description: [product identity], three buttons, one charging port, [materials],
dark podium, consistent light direction, final hero state with lid open.

The grid is not a physical storyboard. Do not render borders, gutters, numbers or paper texture.
```

## Example 2 · 10 秒短剧片段

### Clip Brief

```markdown
- 模式：narrative
- 时长：10s
- 画幅：9:16
- 场景：雨夜面馆门口到店内。
- 主体：角色 A，深色外套，收起的伞。
- 目标：推门、停住、看见熟客。
- 禁止：新增人物、台词、字幕、水印。
```

### Nine-Beat Plan

| 格 | 时间 | 职责 |
| --- | --- | --- |
| 01 | 0.0-1.0s | 雨夜门口与角色背影。 |
| 02 | 1.0-2.0s | 手推向门把。 |
| 03 | 2.0-3.0s | 门缝透出店内暖光。 |
| 04 | 3.0-4.0s | 角色进入，视线扫过店内。 |
| 05 | 4.0-5.0s | 看见熟客的背影。 |
| 06 | 5.0-6.0s | 角色停步，伞仍在右手。 |
| 07 | 6.0-7.2s | 熟客未回头，只轻推一碗面。 |
| 08 | 7.2-8.6s | 角色视线从熟客落到那碗面。 |
| 09 | 8.6-10.0s | 门口冷光与店内暖光同框，留钩子。 |

连续性红线：角色脸型、发型、外套、伞的位置、门内桌椅位置和光源方向九格一致。

## Example 3 · 24 秒拆分

不要生成一个 24 秒九宫格。先提出：

| SEQ | 时长 | 目标 | Carry-out |
| --- | ---: | --- | --- |
| SEQ-01 | 8s | 进入书店并发现信 | 角色站在桌前，信封未打开，右手压信封。 |
| SEQ-02 | 8s | 打开信并读到关键信息 | 信纸摊开，角色视线锁定一行字。 |
| SEQ-03 | 8s | 决定寄出，抬头看窗外 | 角色持信走向门口，窗外光照亮侧脸。 |

每个 `SEQ` 各自生成一张 3×3 分镜图和一条完整视频提示词。下一段第一格必须重复上一段 `Carry-out` 的可见状态。
