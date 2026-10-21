# PaperTouch

**英文论文轻修，新增计算机与网络安全专家润色模式。**

PaperTouch 是用于已有英文论文的 AI 助手技能。默认采用六条明确的编辑白名单，只改命中片段，其余原样保留；v1.1.0 新增可选专家润色，面向计算机与网络安全论文改善表达、语法和局部衔接，同时保留科学含义、原有主张和用户指定的结构。

English academic editing with an unchanged six-rule whitelist by default, plus opt-in CS/security expert editing informed by published papers.

| 模式 | 如何启用 | 适用任务 |
|---|---|---|
| 白名单轻修 | 默认，或指定“原有白名单模式” | 只处理E1–E6，未命中文字逐字保留 |
| 专家润色 | 明确指定“专家润色模式” | 在授权范围内改善表达、语法和局部衔接，保留攻击者能力、实验条件及结论强度 |

两种模式都支持仅审核。专家模式不会自动重排章节或补写缺失研究内容；原有六条规则和补丁工具保持不变。

## 可选专家润色

```text
使用 $paper-touch-en 的专家润色模式修改下面网络安全论文段落。
改善表达和局部衔接，保留攻击者能力、实验条件、数字、引用、研究状态和结论强度。
只输出修改后的段落。
```

学习记录覆盖100篇开放获取论文：60篇USENIX Security、20篇NDSS、10篇OSDI和10篇NSDI。26篇开发集论文的76处章节窗口经过研读，20篇论文留出用于冻结后的适用性检查。全文采集、自动分析与章节研读分别记录，不宣称逐页精读全部100篇，也不证明作者身份或检测效果。参见 [专家指南](paper-touch-en/references/expert-editing.md)、[证据与边界](paper-touch-en/references/style-evidence.md)和[语料清单](paper-touch-en/references/style-sources.json)。论文PDF与完整正文不随技能再分发。

专家指南重点覆盖问题与机制、威胁模型与信任边界、评估比较，以及假设、观察、推断和证明的区分。风格蒸馏不涉及模型参数训练。

[下载 v1.1.0 技能包](https://github.com/ZXON-ZTX/PaperTouch/releases/download/v1.1.0/paper-touch-en.zip) · [下载学习与验证材料](https://github.com/ZXON-ZTX/PaperTouch/releases/download/v1.1.0/PaperTouch-style-study.zip)

## 能做什么

| 规则 | 允许处理的问题 |
|---|---|
| E1 | 不承担必要强调或警示作用的空泛提示语 |
| E2 | 两组明确列出的冗长功能短语 |
| E3 | 三组研究动作中可等价简化的轻动词结构 |
| E4 | 同一位置紧邻叠加的添加连接词 |
| E5 | 同一数值前重复的近似词 |
| E6 | 功能已完整说明、且不承载独立信息的装饰性职业拟人 |

每次修改必须满足对应规则的触发条件和例外要求。不确定时保留原文；不为增加修改量而改写。完整规则见 [English whitelist](paper-touch-en/references/english-rules.md)。

例如，以下只是编辑示例，不是研究结果：

```text
Before: We conducted an evaluation of the encoder on the test split.
After:  We evaluated the encoder on the test split.
```

数字、单位、公式、术语、引用、限定条件、阴性结果和研究完成状态属于保护内容。正常被动语态、必要长句、真实对比及专业术语重复都不作为改写理由。

## 安装

适用于支持本地 `SKILL.md` 技能的 AI 助手。以 Codex 为例：

1. 下载 [paper-touch-en.zip](https://github.com/ZXON-ZTX/PaperTouch/releases/latest/download/paper-touch-en.zip)。
2. 解压后，将整个 `paper-touch-en` 文件夹放入技能目录，例如 Windows 的 `%USERPROFILE%\.agents\skills\`。
3. 确认路径为 `%USERPROFILE%\.agents\skills\paper-touch-en\SKILL.md`。如果尚未出现在技能列表中，重启 Codex 后再试。

也可以克隆本仓库，将其中的 `paper-touch-en` 文件夹复制到技能目录。调用标识为 `$paper-touch-en`，展示名称为 PaperTouch。

## 使用

清理已有英文原稿：

```text
使用 $paper-touch-en 清理下面英文论文段落。
只按白名单修改，保留未命中文字、数字、公式、引用和原有结构。
只输出修改后的全文。

[粘贴英文原稿]
```

仅审核，不修改：

```text
使用 $paper-touch-en，仅审核、不改写。
列出命中的 E1–E6、原文位置及最小修改建议。

[粘贴英文原稿]
```

作者样本或风格指南可以随任务提供。默认只输出完整修改稿；没有明确命中时原样返回。

## 补丁工具与测试

技能附带 Python 3.10+ 补丁工具，用于将已审阅的编辑计划应用到 UTF-8 文本、Markdown 和 LaTeX。无第三方 Python 依赖，工具本身不调用 API、检测器或网络服务。

```text
cd paper-touch-en
python scripts/apply_edits.py draft.md --plan edits.json -o draft.cleaned.md
python -B -m unittest discover -s tests -v
```

输出必须是新文件。工具检查字面锚点、重叠、未改区域、部分受保护结构、数值及常见单位、否定/模态标记和常见引文；它不能判定规则是否真正适用或科学语义是否等价。列表和表格等已识别结构继续整行保护。识别不到的专业单位、引文和其他结构需要显式保护范围及人工复核。

当前随包包含 **19 项自动测试**，覆盖原有补丁行为、六条规则示例和保护修复。专家模式另记录了六组独立代理行为检查，包含研究状态、样本范围、保护片段、清楚段落不改以及白名单模式回归；这些有限案例不等于真人专家盲评。参见 [模式对照记录](paper-touch-en/references/expert-mode-validation.json)、[补丁格式与限制](paper-touch-en/references/patch-format.md)和[验证记录](paper-touch-en/验证记录.md)。

## 适用边界

PaperTouch 用于已有英文成稿，不负责从零起草、中文改写、翻译或未经授权的结构重组。默认白名单模式不执行全面语法校对；专家模式允许授权范围内的语法和表达调整。Word/PDF 需要相应文档工具及独立排版验证，不能直接输入上述补丁脚本。

六条规则是编辑白名单，不是作者身份或 AI 检测模型。没有英文大规模实证或检测器降分保证；中文来源中的语料频率不作为英文效果证据。AI 助手实际运行所需的账号和服务由使用者所在环境提供。

## 来源与许可

本英文版本改编自用户提供的 `lieflat-less-ai-tone` 中文技能，保留白名单、最小改动和信息守恒方法；英文规则独立列明。原始 Copyright (c) 2026 shiujan 和 [MIT 许可证](LICENSE) 保留。

完整来源说明、中文原始快照及文件哈希随仓库提供：[source-notes.md](paper-touch-en/references/source-notes.md)、[source-zh.md](paper-touch-en/references/source-zh.md)、[source-provenance.json](paper-touch-en/references/source-provenance.json)。
