# ChinaOps - Emoji使用规范说明

**日期:** 2026-01-22  
**版本:** v1.0  
**作者:** TechDadShanghai

---

## 📋 当前状态

### ✅ 已完成

1. **首页更新通知优化**
   - 原文案：`New in v1.0: Added Shanghai-specific guides...`
   - 新文案：`v1.0 首次上线！这是ChinaOps的第一个正式版本。如果您觉得有用，欢迎提出宝贵意见和建议，您的支持是我持续更新的动力！`
   
2. **首页emoji保留**
   - 首页的emoji图标保留，用于视觉吸引力和快速识别
   - 包括：Quick Links的emoji、统计数字、分类图标等

---

## 🎯 Emoji使用策略

### ✅ 保留Emoji的位置

**1. 首页 (index.html)**
- Quick Links (Choose Your Path)
  - 👤 First-Time Visitor
  - 👨‍👩‍👧 Traveling with Kids
  - 🆘 Emergency
  - 🚀 Daily Navigation
  - 🏮 Chinese Holiday
  - 🥗 Vegetarian / Vegan

- Full Guide Library 表格
  - 每个指南标题前的emoji图标
  - 用于快速视觉识别

- 统计数字
  - "27 Technical SOPs"
  - "24/7 Availability"
  - "Zero BS Content"

**2. 分类Index页面**
- 保留分类标题的emoji（如 ✈️ System Setup, 🚗 Daily Runtime等）
- 用于导航和视觉层次

### ❌ 移除Emoji的位置

**指南内容页面 (所有.md文件)**
- 移除所有section header中的emoji
- 保持专业、简洁的阅读体验
- 避免视觉干扰

**示例：**
```markdown
# 移除前
## 🥗 1. The Vegan "Environment Variable"
## 🛡️ 2. Critical Phrases & Logic
## 🍽️ 3. Top Restaurant Nodes

# 移除后
## 1. The Vegan "Environment Variable"
## 2. Critical Phrases & Logic
## 3. Top Restaurant Nodes
```

---

## 📝 需要处理的文件列表

### 高优先级（新增的Shanghai指南）

1. **shanghai-vegan-guide.md** ⏳ 部分完成
   - ✅ 已移除：🥗
   - ⏳ 待移除：🛡️, 🍽️, 📱, 🔗

2. **shanghai-food-guide.md**
   - 待移除：🥟, 🍚, 🛡️, 🔗

3. **shanghai-weather-guide.md**
   - 待移除：🌫️, 🌡️, 🌀, 💡

4. **shanghai-attractions-guide.md**
   - 待移除：🏛️, 🏙️, 👨‍👩‍👧, 💡

5. **emergency-contacts-card.md**
   - 待移除：🆘, 📞, 🏛️, 🏥, 💬, 📱, 🖨️, 🔗

6. **shanghai-safety-guide.md**
   - 待移除：🛡️, 🚨, 🏥

### 中优先级（其他指南）

7. **baby-survival-master-runbook.md**
   - 待移除：🍼, 🏥

8. **holiday-survival-guide.md**
   - 待移除：🛡️, 🏥

9. **safety-and-common-scams.md**
   - 待移除：🚨, 🏥

### 低优先级（Index页面）

10. **各分类index.md**
    - 保留分类标题emoji
    - 移除子标题emoji（如果有）

---

## 🔧 处理方法

### 方法1：手动逐个替换（推荐）
使用 `replace_file_content` 工具逐个文件处理，确保准确性。

### 方法2：PowerShell批量处理
```powershell
# 示例脚本
$files = Get-ChildItem -Path "docs" -Filter "*.md" -Recurse
foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw
    $content = $content -replace '## 🥗', '##'
    $content = $content -replace '## 🛡️', '##'
    # ... 更多替换
    Set-Content $file.FullName $content
}
```

---

## 📊 进度跟踪

| 文件 | 状态 | Emoji数量 | 完成度 |
|:---|:---:|:---:|:---:|
| shanghai-vegan-guide.md | ⏳ 进行中 | 5 | 20% |
| shanghai-food-guide.md | ⏳ 待处理 | 4 | 0% |
| shanghai-weather-guide.md | ⏳ 待处理 | 4 | 0% |
| shanghai-attractions-guide.md | ⏳ 待处理 | 4 | 0% |
| emergency-contacts-card.md | ⏳ 待处理 | 8 | 0% |
| shanghai-safety-guide.md | ⏳ 待处理 | 3 | 0% |
| baby-survival-master-runbook.md | ⏳ 待处理 | 2 | 0% |
| holiday-survival-guide.md | ⏳ 待处理 | 2 | 0% |
| safety-and-common-scams.md | ⏳ 待处理 | 2 | 0% |

**总计:** 约34个emoji需要移除

---

## ✅ 设计原则

1. **首页 = 视觉吸引力**
   - 保留所有emoji
   - 帮助用户快速识别和导航

2. **指南内容 = 专业简洁**
   - 移除所有emoji
   - 专注于内容本身
   - 提升阅读体验

3. **分类页 = 导航清晰**
   - 保留主标题emoji
   - 移除次级标题emoji

---

## 🎯 下一步行动

1. **立即处理**（高优先级）
   - 完成 shanghai-vegan-guide.md 的剩余emoji移除
   - 处理其他5个新增Shanghai指南
   - 处理 emergency-contacts-card.md

2. **后续处理**（中优先级）
   - 处理其他现有指南的emoji

3. **验证**
   - 检查所有指南的可读性
   - 确保没有遗漏的emoji
   - 测试页面渲染效果

---

## 📝 备注

- 此策略平衡了**视觉吸引力**（首页）和**专业性**（内容页）
- 符合商业化产品的专业形象要求
- 提升用户阅读体验，减少视觉干扰

---

**创建时间:** 2026-01-22  
**状态:** ⏳ 进行中  
**预计完成时间:** 需要约1-2小时手动处理