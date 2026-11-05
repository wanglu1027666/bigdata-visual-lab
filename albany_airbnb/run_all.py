import subprocess
import sys
import os

def run_script(script_path):
    print(f"\n正在执行: {script_path} ...")
    # 切换工作目录到 scripts，保证相对路径正确
    result = subprocess.run([sys.executable, os.path.basename(script_path)], cwd=os.path.dirname(script_path))
    if result.returncode != 0:
        print(f"执行失败: {script_path}")
        sys.exit(1)

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    scripts = [
        os.path.join(base_dir, "scripts", "01_clean.py"),
        os.path.join(base_dir, "scripts", "02_visuals_templates.py"),
        os.path.join(base_dir, "scripts", "03_models_business.py"),
    ]
    for s in scripts:
        run_script(s)
        
    print("\n=======================================")
    print("全部数据处理与 16 张图表生成完毕！请查看 outputs/figures 目录。")
    print("如需启动大屏，请在终端运行: streamlit run scripts/04_dashboard.py")