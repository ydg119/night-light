# 🏮 复古夜灯 - 交互式网页灯具

> **一盏会呼吸的数字复古灯** · 纯前端实现 · 零依赖 · 即开即用

<p align="center">
  <img src="vintage-lamp.png" alt="复古灯具" width="150" style="border-radius: 10px;">
</p>

## ✨ 核心功能

### 🎨 **颜色主题切换**
- 🟦 **白色模式** - 清新明亮的工作环境
- 🟨 **黄色模式** - 温暖舒适的阅读氛围  
- 🟥 **红色模式** - 浪漫柔和的夜间照明

### 🔆 **智能亮度调节**
- 🖱️ **鼠标滚轮控制** - 向上滚动调亮，向下滚动调暗
- 📊 **实时显示** - 右上角显示当前亮度百分比 (10%-100%)
- 🎛️ **精细调节** - 每次滚动调节5%亮度

### 💡 **灯具交互**
- ✨ **点击闪烁** - 点击灯具产生瞬间全亮闪烁效果
- 🔍 **悬停放大** - 鼠标悬停时灯具放大5%，增加交互趣味性
- 🌟 **智能光晕** - 灯光颜色随主题变化，亮度影响光晕强度

## 🚀 快速开始

### 方法一：直接打开（最简单）
```bash
# 在项目目录中
open night-light.html
```

### 方法二：本地服务器
```bash
# 使用Python内置服务器
python3 -m http.server 8000
# 然后在浏览器中访问：http://localhost:8000/night-light.html
```

### 方法三：开发模式（推荐）
```bash
# 安装browser-sync（如果未安装）
npm install -g browser-sync

# 启动实时预览服务器
npx browser-sync start --server --files "*.html" --browser "chrome"
```

## 🎮 使用指南

### 基本操作
1. **选择颜色主题** → 点击底部三个圆形按钮
2. **调节亮度** → 使用鼠标滚轮上下滚动
3. **与灯具互动** → 点击灯具体验闪烁效果

### 亮度控制范围
- 🔆 **最大亮度**：100%（完全明亮）
- 🔅 **适中亮度**：50%（舒适阅读）
- 🌙 **最小亮度**：10%（夜间微光）

### 颜色模式效果
| 模式 | 背景色 | 光晕颜色 | 适用场景 |
|------|--------|----------|----------|
| 🟦 白色 | #ffffff | 淡黄色 | 工作、学习 |
| 🟨 黄色 | #fff59d | 亮黄色 | 阅读、休闲 |
| 🟥 红色 | #ef5350 | 红色 | 夜间、放松 |

## 🏗️ 技术架构

### 📦 技术栈
```
📄 HTML5        - 语义化结构，响应式设计
🎨 CSS3         - Flexbox布局，CSS动画，渐变效果
⚡ JavaScript ES6 - 原生DOM操作，事件处理
🖼️ Canvas       - 程序化生成复古灯具图像
```

### 🔧 核心实现
- **单文件架构** - 所有代码集成在 `night-light.html` 中
- **零依赖** - 无外部库，无构建工具
- **纯前端** - 无需后端服务器
- **响应式设计** - 适配不同屏幕尺寸

## 📁 项目结构

```
night-light/
├── 📄 night-light.html          # 主HTML文件（完整实现）
├── 🖼️ vintage-lamp.png          # 复古灯具PNG图像
├── 📝 AGENTS.md                # 开发代理指南
├── 🎨 crafted-radiance-philosophy.md  # 设计哲学（英文）
├── 🏮 古典光韵设计哲学.md      # 设计哲学（中文）
├── 🐍 create_vintage_lamp.py   # 灯具图像生成脚本
├── 🐍 create_lamp_enhanced.py  # 增强版图像生成脚本
├── 📦 lamp-image.js            # 灯具图像base64数据
└── 📄 vintage-lamp-base64.txt  # base64编码文本
```

## 🎨 设计哲学

### "古典光韵"设计理念
本项目基于 **"古典光韵"** 设计哲学，强调：

- **材质真实性** - 黄铜金属、玻璃灯罩、灯泡发光的物理精确性
- **结构清晰度** - 每个组件连接点和结构关系的明确可见
- **光线交互** - 光线与每个表面的反射、折射和阴影效果
- **工艺可见性** - 制造痕迹（焊接点、螺纹、抛光纹路）的微妙存在
- **功能表达** - 清晰传达灯具工作原理和各部件功能目的

## 🔄 交互逻辑

### 颜色切换系统
```javascript
function changeColor(color, bgClass) {
    // 1. 更新背景颜色类
    // 2. 激活对应按钮状态
    // 3. 调整光晕颜色匹配主题
    // 4. 保存当前颜色状态
}
```

### 亮度控制系统
```javascript
function updateBrightness(brightness) {
    // 1. 限制范围 (10%-100%)
    // 2. 应用CSS filter到背景层
    // 3. 调整光晕透明度
    // 4. 更新显示百分比
}
```

### 灯具交互系统
```javascript
lamp.addEventListener('click', () => {
    // 1. 保存当前亮度
    // 2. 瞬间设为100%亮度
    // 3. 200ms后恢复原亮度
    // 4. 产生闪烁视觉效果
});
```

## 🛠️ 开发指南

### 代码规范
- **HTML**：语义化标签，中文注释，BEM命名规范
- **CSS**：Flexbox布局，CSS变量，平滑过渡动画
- **JavaScript**：ES6语法，事件委托，模块化函数

### 扩展建议
1. **🎨 颜色自定义** - 添加颜色选择器或调色板
2. **💾 本地存储** - 使用localStorage保存用户偏好
3. **📱 触摸支持** - 添加移动端手势控制
4. **🎵 音效增强** - 点击按钮和灯具时添加音效
5. **🌙 自动模式** - 基于时间自动调整亮度和颜色

### 浏览器兼容性
- ✅ Chrome 60+
- ✅ Firefox 55+ 
- ✅ Safari 11+
- ✅ Edge 79+

## 🐛 故障排除

### 常见问题
| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 滚轮不工作 | 事件监听器冲突 | 确保页面焦点正确 |
| 图片不显示 | base64编码错误 | 检查HTML第194行base64数据 |
| 按钮无响应 | JavaScript错误 | 检查浏览器控制台错误信息 |
| 动画卡顿 | 硬件加速不足 | 使用CSS transform代替其他属性 |

### 调试技巧
```javascript
// 在浏览器控制台中调试
updateBrightness(50);  // 设置亮度为50%
console.log('当前亮度:', currentBrightness);  // 查看当前状态
console.log('当前颜色:', currentColor);       // 查看当前颜色
```

## 📄 许可证

本项目采用 **MIT 许可证** - 详情请查看 [LICENSE](LICENSE) 文件。

## 👥 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 🌟 项目亮点

### 🏆 技术成就
- 🚀 **单文件实现** - 完整功能集成在单个HTML文件中
- 🎯 **零依赖架构** - 无外部库，启动速度快
- 🔧 **程序化图像** - 使用Python生成定制灯具图像
- 🎨 **设计系统** - 完整的"古典光韵"设计哲学

### 🎭 用户体验
- ✨ **直观交互** - 三色按钮+滚轮控制，学习成本为零
- 🔄 **即时反馈** - 所有操作都有视觉或动画反馈
- 🎛️ **精细控制** - 亮度可精确到5%一档调节
- 🖼️ **视觉美感** - 复古风格与现代扁平化设计的完美结合

---

<p align="center">
  <em>✨ 让这盏数字复古灯，为你的数字空间增添一丝温暖与怀旧 ✨</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/技术栈-HTML5/CSS3/JavaScript-blue" alt="技术栈">
  <img src="https://img.shields.io/badge/许可证-MIT-green" alt="许可证">
  <img src="https://img.shields.io/badge/状态-生产就绪-brightgreen" alt="状态">
</p>