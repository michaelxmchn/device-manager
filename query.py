#!/usr/bin/env python3
"""
设备管理系统 - 查询工具
"""

import json
import sys
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "devices.json")

def load_db():
    """加载设备数据库"""
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def list_computers():
    """列出所有电脑"""
    db = load_db()
    print("\n🖥️  电脑列表")
    print("=" * 50)
    
    for key, pc in db["computers"].items():
        status = "🟢 在线" if pc["status"] == "online" else "🔴 离线"
        print(f"\n{pc['name']} ({key})")
        print(f"   IP: {pc['ip']}")
        print(f"   OS: {pc['os']}")
        print(f"   状态: {status}")
        print(f"   Ollama: ✅" if pc["capabilities"]["ollama"] else "   Ollama: ❌")

def list_models():
    """列出所有 AI 模型"""
    db = load_db()
    print("\n🤖 AI 模型列表")
    print("=" * 50)
    
    for key, pc in db["computers"].items():
        print(f"\n{pc['name']}:")
        for model in pc["ollama"]["models"]:
            print(f"   • {model['name']} ({model['size']})")
            print(f"     用途: {model['use_case']}")

def list_printers():
    """列出打印机"""
    db = load_db()
    print("\n🖨️  打印机列表")
    print("=" * 50)
    
    for printer in db["peripherals"]["printers"]:
        print(f"\n{printer['name']}")
        print(f"   IP: {printer['ip']}")
        print(f"   连接: {printer['connected_to']}")
        print(f"   状态: {printer['status']}")

def assign_task(task_type):
    """分配任务"""
    db = load_db()
    assignment = db["task_assignment"].get(task_type, {})
    
    if assignment:
        print(f"\n📋 {task_type} 任务分配")
        print("=" * 50)
        print(f"推荐电脑: {assignment.get('computer', '任意')}")
        print(f"推荐模型: {assignment.get('preferred', '任意')}")
        print(f"备选模型: {assignment.get('alternative', '无')}")
    else:
        print(f"\n❌ 未知任务类型: {task_type}")
        print("可用类型: code_generation, quick_task, reasoning_task, printing")

def status():
    """完整状态"""
    db = load_db()
    print("\n📊 设备管理状态")
    print("=" * 50)
    print(f"更新时间: {db['updated_at']}")
    print(f"电脑数量: {len(db['computers'])}")
    print(f"打印机数量: {len(db['peripherals']['printers'])}")
    
    online = sum(1 for pc in db["computers"].values() if pc["status"] == "online")
    print(f"在线电脑: {online}/{len(db['computers'])}")

if __name__ == "__main__":
    args = sys.argv[1:]
    
    if not args or args[0] == "status":
        status()
    elif args[0] == "computers":
        list_computers()
    elif args[0] == "models":
        list_models()
    elif args[0] == "printers":
        list_printers()
    elif args[0] == "assign" and len(args) > 1:
        assign_task(args[1])
    else:
        print("用法:")
        print("  python query.py status      # 状态")
        print("  python query.py computers   # 电脑列表")
        print("  python query.py models      # 模型列表")
        print("  python query.py printers    # 打印机列表")
        print("  python query.py assign <任务类型>")
