# AGENTS.md - 夜灯网页项目指南

## 项目概述
这是一个简单的复古夜灯网页项目，包含一个独立的HTML文件，使用纯HTML、CSS和JavaScript实现交互式夜灯效果。

## 项目结构
```
night-light/
├── night-light.html    # 主HTML文件（包含所有代码）
└── AGENTS.md          # 本项目指南
```

## 构建与运行

### 本地运行
```bash
# 直接在浏览器中打开
open night-light.html

# 或使用Python简单HTTP服务器
python3 -m http.server 8000
# 然后访问 http://localhost:8000/night-light.html
```

### 开发服务器
```bash
# 使用浏览器同步（推荐用于开发）
npx browser-sync start --server --files "*.html" --browser "chrome"
```

## 代码风格指南

### HTML
- 使用HTML5标准：`<!DOCTYPE html>`
- 语言设置为中文：`<html lang="zh-CN">`
- 包含必要的meta标签：
  - `<meta charset="UTF-8">`
  - `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
- 使用语义化class命名（kebab-case）：
  - 容器：`.lamp-container`, `.controls`
  - 组件：`.lamp`, `.color-btn`
  - 状态：`.active`, `.white-bg`
- 内联样式表：本项目使用内联CSS（单个文件）

### CSS
- **重置样式**：
  ```css
  * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
  }
  ```
- **布局**：使用Flexbox进行垂直居中布局
- **单位**：优先使用`vh`、`%`、`px`单位
- **颜色**：使用十六进制颜色值（#ffffff）或rgba透明度
- **过渡效果**：所有交互都应有平滑过渡（0.3s-0.5s）
- **命名约定**：BEM风格命名（block__element--modifier）
- **动画**：使用CSS关键帧动画增强用户体验

### JavaScript
- **变量声明**：使用`let`和`const`，避免`var`
- **函数命名**：使用camelCase，动词开头（如`updateBrightness`、`changeColor`）
- **事件处理**：使用事件委托或直接事件监听
- **DOM操作**：优先使用`document.querySelector()`和`classList` API
- **注释**：使用中文注释，函数应有简要说明
- **代码组织**：
  - 全局变量声明在顶部
  - 函数定义按逻辑分组
  - 事件监听器在初始化时绑定

### 交互模式
1. **颜色切换**：点击底部按钮切换页面背景色
2. **亮度控制**：鼠标滚轮控制页面亮度（10%-100%）
3. **灯具交互**：点击灯具有闪烁效果

## 开发工作流

### 1. 代码修改
```bash
# 1. 编辑HTML文件
# 2. 保存更改
# 3. 刷新浏览器查看效果
```

### 2. 功能测试清单
- [ ] 颜色按钮点击正常切换背景色
- [ ] 鼠标滚轮正常控制亮度
- [ ] 灯具点击有闪烁效果
- [ ] 页面在不同屏幕尺寸下显示正常
- [ ] 所有过渡动画平滑
- [ ] 按钮悬停效果正常

### 3. 浏览器兼容性
- Chrome 60+
- Firefox 55+
- Safari 11+
- Edge 79+

## 代理工作指导

### 新增功能
1. **评估复杂度**：如果功能需要多个组件交互，应先规划架构
2. **保持简单**：避免添加不必要的依赖
3. **向后兼容**：新功能不应破坏现有交互

### 代码审查要点
1. **性能**：避免强制同步布局，使用CSS transform进行动画
2. **可访问性**：确保按钮有足够点击区域，颜色对比度足够
3. **响应式**：在移动设备上测试布局
4. **代码清晰**：函数职责单一，注释清晰

### 错误处理
1. **图片加载失败**：应有备用图片或优雅降级
2. **JavaScript错误**：使用try-catch处理可能失败的操作
3. **用户输入验证**：验证亮度值在有效范围内

## 项目约定

### 文件管理
- 所有代码位于单个HTML文件中
- 外部资源（图片）使用CDN链接
- 不添加构建工具或包管理器，除非必要

### 版本控制
- 提交信息使用中文描述
- 功能更改应包含测试步骤
- 重大变更应更新本AGENTS.md文件

### 部署
- 可直接上传HTML文件到任何静态文件托管服务
- 无需服务器端处理
- 建议启用GZIP压缩

## 故障排除

### 常见问题
1. **图片不显示**：检查CDN链接，添加备用图片源
2. **滚轮不工作**：检查事件监听器是否正确绑定
3. **动画卡顿**：检查是否使用GPU加速属性（transform, opacity）

### 调试技巧
```javascript
// 在控制台调试亮度
updateBrightness(50);  // 设置亮度为50%

// 检查当前状态
console.log('当前亮度:', currentBrightness);
console.log('当前颜色:', currentColor);
```

## 扩展建议

### 可能的功能扩展
1. **颜色选择器**：自定义背景颜色
2. **亮度记忆**：保存用户偏好设置到localStorage
3. **动画模式**：添加呼吸灯效果
4. **声音效果**：点击按钮添加音效
5. **移动端优化**：触摸手势控制

### 技术栈扩展（如果需要）
1. **构建工具**：使用Vite或Parcel进行模块化
2. **框架**：可迁移到Vue.js或React
3. **测试**：添加Jest + Testing Library
4. **样式**：引入Tailwind CSS

---

**最后更新**: 2026-02-03  
**维护者**: Sisyphus Agent  
**项目状态**: 稳定生产版本