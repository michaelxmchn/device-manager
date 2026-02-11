#!/usr/bin/env python3
"""
设备管理 - 更新工具
"""

import json
import sys
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "devices.json")

def load_db():
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_db(db):
    with open(DB_PATH, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

def add_computer(key, name, ip, os_name, ssh_user):
    """添加新电脑"""
    db = load_db()
    
    db["computers"][key] = {
        "name": name,
        "ip": ip,
        "os": os_name,
        "hostname": "",
        "ssh_user": ssh_user,
        "sudo_password": "",
        "status": "offline",
        "capabilities": {
            "ollama": False,
            "openclaw": False,
            "print": False,
            "tailscale": False
        },
        "ollama": {
            "version": "",
            "models": [],
            "default_model": ""
        },
        "openclaw": {
            "version": "",
            "discord_token": "",
            "channels": [],
            "skills": []
        }
    }
    
    save_db(db)
    print(f"✅ 已添加电脑: {name} ({key})")

def update_status(key, status):
    """更新状态"""
    db = load_db()
    
    if key in db["computers"]:
        db["computers"][key]["status"] = status
        save_db(db)
        print(f"✅ {key} 状态: {status}")
    else:
        print(f"❌ 未知电脑: {key}")

def add_model(key, name, size, model_type, use_case):
    """添加模型"""
    db = load_db()
    
    if key in db["computers"]:
        db["computers"][key]["ollama"]["models"].append({
            "name": name,
            "size": size,
            "type": model_type,
            "use_case": use_case
        })
        save_db(db)
        print(f"✅ 已添加模型: {name} 到 {key}")
    else:
        print(f"❌ 未知电脑: {key}")

def set_default_model(key, name):
    """设置默认模型"""
    db = load_db()
    
    if key in db["computers"]:
        db["computers"][key]["ollama"]["default_model"] = name
        save_db(db)
        print(f"✅ 默认模型: {name}")
    else:
        print(f"❌ 未知电脑: {key}")

def add_printer(name, ip, connected_to):
    """添加打印机"""
    db = load_db()
    
    db["peripherals"]["printers"].append({
        "name": name,
        "ip": ip,
        "connected_to": connected_to,
        "status": "configured",
        "driver": "raw",
        "notes": ""
    })
    
    save_db(db)
    print(f"✅ 已添加打印机: {name}")

if __name__ == "__main__":
    args = sys.argv[1:]
    
    if not args:
        print("用法:")
        print("  python update.py add-computer <key> <name> <ip> <os> <ssh_user>")
        print("  python update.py status <key> <online|offline>")
        print("  python update.py add-model <key> <name> <size> <type> <use_case>")
        print("  python update.py default-model <key> <name>")
        print("  python update.py add-printer <name> <ip> <connected_to>")
    else:
        cmd = args[0]
        
        if cmd == "add-computer" and len(args) == 6:
            add_computer(args[1], args[2], args[3], args[4], args[5])
        elif cmd == "status" and len(args) == 3:
            update_status(args[1], args[2])
        elif cmd == "add-model" and len(args) == 6:
            add_model(args[1], args[2], args[3], args[4], args[5])
        elif cmd == "default-model" and len(args) == 3:
            set_default_model(args[1], args[2])
        elif cmd == "add-printer" and len(args) == 4:
            add_printer(args[1], args[2], args[3])
        else:
            print("❌ 参数错误")
