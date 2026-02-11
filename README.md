# 设备管理系统

## 目标

记录所有可控电脑的资源，按任务分配工作。

## 架构

```
设备管理器
│
├── 电脑列表
│   ├── 旧电脑 (192.168.1.17)
│   │   ├── IP: 192.168.1.17
│   │   ├── OS: Ubuntu 24.04
│   │   ├── Ollama: deepseek-r1:7b, llama3.2:3b
│   │   ├── 打印机: 无
│   │   └── OpenClaw: ✅
│   │
│   └── 新电脑 (192.168.1.67)
│       ├── IP: 192.168.1.67
│       ├── OS: Ubuntu 24.04
│       ├── Ollama: qwen2.5-coder:7b, qwen2.5-coder:14b
│       ├── 打印机: Lenovo LJ2250 (192.168.1.102)
│       └── OpenClaw: ✅
│
└── 任务分配
    ├── 代码任务 → qwen2.5-coder:14b
    ├── 快速响应 → llama3.2:3b
    └── 推理任务 → deepseek-r1:7b
```

## 设备数据库

见 `devices.json`
