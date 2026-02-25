"""
?렞 Playform AI - 3燁믣맱?쎽빽烏ⓩ씮
若욄뿶??쭍??+ 轢귚벽?①뵽 = 塋뗥뜵?계괌曆긷댗
"""

import os
import sys
import time
import subprocess
from pathlib import Path
from datetime import datetime

# 弱앲캊野쇔뀯 rich (?ⓧ틢轢귚벽渦볟눣)
try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.align import Align
    from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
    from rich.layout import Layout
    from rich import box
    HAS_RICH = True
except ImportError:
    HAS_RICH = False
    print("rich is not installed; using basic output mode. Install with: pip install rich")


class FallbackConsole:
    """Simple console shim used when rich is unavailable."""

    @staticmethod
    def print(*args, **kwargs):
        print(*args)


class Dashboard3Sec:
    """3燁믣맱?쎽빽烏ⓩ씮"""
    
    def __init__(self):
        self.console = Console() if HAS_RICH else FallbackConsole()
        self.start_time = datetime.now()
    
    def print_stunning_header(self):
        """?볟뜲?뉑뮳?㎩ㅄ??""
        if not HAS_RICH:
            print("\n" + "="*60)
            print("?? PLAYFORM AI - 3燁믣맱?쏁내瀯?)
            print("="*60 + "\n")
            return
        
        header = """
 ?댿뻽?댿뻽?댿뻽???댿뻽??     ?댿뻽?댿뻽?댿븮 ?댿뻽??  ?댿뻽?쀢뻽?댿뻽?댿뻽?댿뻽???댿뻽?댿뻽?댿뻽???댿뻽?댿뻽?댿뻽???댿뻽?댿븮   ?댿뻽?댿븮
 ?댿뻽?붴븧?먥뻽?댿븮?댿뻽??    ?댿뻽?붴븧?먥뻽?댿븮?싢뻽?댿븮 ?댿뻽?붴븴?댿뻽?붴븧?먥븧?먥븴?댿뻽?붴븧?먥븧?먥븴?댿뻽?붴븧?먥븧?댿뻽?쀢뻽?댿뻽?댿븮 ?댿뻽?댿뻽??
 ?댿뻽?댿뻽?댿뻽?붴븴?댿뻽??    ?댿뻽?댿뻽?댿뻽?댿븨 ?싢뻽?댿뻽?댿븫???댿뻽?댿뻽?댿븮  ?댿뻽??    ?댿뻽??  ?댿뻽?묅뻽?댿븫?댿뻽?댿뻽?붴뻽?댿븨
 ?댿뻽?붴븧?먥븧???댿뻽??    ?댿뻽?붴븧?먥뻽?댿븨  ?싢뻽?댿븫?? ?댿뻽?붴븧?먥븴  ?댿뻽??    ?댿뻽??  ?댿뻽?묅뻽?댿븨?싢뻽?댿븫?앪뻽?댿븨
 ?댿뻽??    ?댿뻽?댿뻽?댿뻽?댿븮?댿뻽?? ?댿뻽??  ?댿뻽??  ?댿뻽?댿뻽?댿뻽?댿븮?싢뻽?댿뻽?댿뻽?댿븮?싢뻽?댿뻽?댿뻽?댿븫?앪뻽?댿븨 ?싢븧???댿뻽??
 ?싢븧??    ?싢븧?먥븧?먥븧?먥븴?싢븧?? ?싢븧??  ?싢븧??  ?싢븧?먥븧?먥븧?먥븴 ?싢븧?먥븧?먥븧???싢븧?먥븧?먥븧???싢븧??    ?싢븧??
        """
        
        self.console.print(Panel(
            header,
            title="?렞 3燁믣맱?쎽빽烏ⓩ씮",
            subtitle="GitHub + Antigravity AI System",
            border_style="bold cyan"
        ))
    
    def show_agent_status(self):
        """?양ㅊ3訝찥gent?뜻곻펷?ら뿪?묈뀎竊?""
        if not HAS_RICH:
            print("\n?렗 YouTube Agent    ????弱긺빽")
            print("?숋툘  SaaS Agent       ????弱긺빽")
            print("?뱼 Marketing Agent  ????弱긺빽\n")
            return
        
        # ?쎾뻠烏ⓩ졏
        table = Table(title="?쨼 AI Agent 若욄뿶?뜻?, box=box.ROUNDED)
        table.add_column("Agent", style="cyan bold")
        table.add_column("?뜻?, style="green")
        table.add_column("?잒꺗", style="magenta")
        table.add_column("雅㎩눣", style="yellow")
        
        agents = [
            ("?렗 YouTube", "???①봇", "?끻??잍닇", "3鰲녽쥜?싨쑍"),
            ("?숋툘  SaaS", "???①봇", "?ゅ뒯凉??, "1?잒꺗?①쉿"),
            ("?뱼 Marketing", "???①봇", "?ι??ゅ뒯??, "20?끻?"),
        ]
        
        for agent, status, func, output in agents:
            table.add_row(agent, status, func, output)
        
        self.console.print(table)
    
    def show_statistics(self):
        """?양ㅊ若욄뿶?경뜮竊덃빊耶쀨럼?ⓩ븞?쒙펹"""
        if not HAS_RICH:
            print("?뱤 若욄뿶?경뜮:")
            print("  ??YouTube ?ε쓦役뤺쭏: 5,432")
            print("  ??驪뤸쐢?①쉿?잒꺗: 12+")
            print("  ???ι?鰲?씨: 50K+")
            print("  ??楹사퍨閭ｅ만瓦먫죱: 99.9%\n")
            return
        
        stats_data = [
            ("?벟 YouTube 役뤺쭏", "5,432/day", "??23%"),
            ("?숋툘  ?잒꺗?①쉿", "12+/month", "??8%"),
            ("?뱼 鰲?씨雅뷸빊", "50K+", "??45%"),
            ("??楹사퍨??뵪??, "99.9%", "??葉녑츣"),
        ]
        
        table = Table(title="?뱤 若욄뿶?경뜮", box=box.ROUNDED)
        table.add_column("?뉑젃", style="cyan")
        table.add_column("?겼?, style="green bold")
        table.add_column("擁뗥듌", style="magenta")
        
        for metric, value, trend in stats_data:
            table.add_row(metric, value, trend)
        
        self.console.print(table)
    
    def show_next_run(self):
        """?양ㅊ訝뗦А瓦먫죱?믦???""
        if not HAS_RICH:
            print("??訝뗦А?ゅ뒯瓦먫죱: ??6:00 弱뤸뿶")
            print("?뵒 GitHub Actions ?ゅ뒯鰲?룕\n")
            return
        
        panel_content = """
??訝뗦А?ゅ뒯瓦먫죱?띌뿴
?곣봺?곣봺?곣봺?곣봺?곣봺?곣봺?곣봺?곣봺??
?뙇 UTC: 18:00 (?? 2026-02-28)
?뙊 雅싨눠: 02:00+8 (訝, 2026-03-01)
?곣봺?곣봺?곣봺?곣봺?곣봺?곣봺?곣봺?곣봺??
??GitHub Actions 藥꿴뀓營?
??驪?6 弱뤸뿶?ゅ뒯?㎬죱訝轝?
??Firebase ?ゅ뒯?①쉿
"""
        self.console.print(Panel(
            panel_content,
            title="??溫▼닋餓삣뒦",
            border_style="yellow",
            expand=False
        ))
    
    def show_quick_commands(self):
        """?양ㅊ恙ラ잌뫝餓?""
        if not HAS_RICH:
            print("?렞 恙ラ잌뫝餓?")
            print("  1. python master.py ??[2] ?경뜮轢붺ㅊ")
            print("  2. python master.py ??[3] ?잌츩瓦먫죱")
            print("  3. python dashboard.py ?룡뼭餓よ〃??n")
            return
        
        commands = """
[1] 轢붺ㅊ與▼폀   ??python master.py ??[2]
[2] 若욄뿶瓦먫죱   ??python master.py ??[3]
[3] ?룡뼭餓よ〃????python dashboard.py
[4] GitHub?③???git push origin main
"""
        self.console.print(Panel(
            commands,
            title="?렞 恙ラ잌뫝餓?,
            border_style="green",
            expand=False
        ))
    
    def show_animated_progress(self):
        """?양ㅊ轢귚벽?꾥퓵佯?씉?①뵽"""
        if not HAS_RICH:
            print("??楹사퍨弱긺빽...\n")
            return
        
        tasks = [
            "?렗 YouTube 凉뺞뱨",
            "?숋툘  SaaS 凉뺞뱨",
            "?뱼 Marketing 凉뺞뱨",
            "?뵕 GitHub Actions",
            "?뵦 Firebase ?①쉿"
        ]
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(bar_width=20),
            TextColumn("[progress.percentage]{task.percentage:.0f}%"),
        ) as progress:
            for i, task in enumerate(tasks):
                task_id = progress.add_task(task, total=100)
                for _ in range(100):
                    progress.update(task_id, advance=1)
                    time.sleep(0.01)
    
    def show_final_message(self):
        """??롧쉪?닺각岳→겘"""
        if not HAS_RICH:
            print("??Playform AI 藥꿨뇛鸚뉐?竊?)
            print("?? 3燁믣냵弱김덩孃쀤틙?①쉪力ⓩ꼷?쎾릹竊?)
            print("?뮕 塋뗥뜵凉冶? python master.py\n")
            return
        
        final = """
??楹사퍨藥?100% ?녶쨭弱긺빽竊?

?렞 ?ⓨ럴??3 燁믣냵?뗥댆竊?
   ??3 訝ゅ성鸚㎫쉪 AI 凉뺞뱨
   ??若욄뿶?ゅ뒯?뽪빊??
   ??6 弱뤸뿶?ゅ뒯瓦먫죱
   ??若뚧빐?꾡틧?①쉿
   ??鴉곦툣瀛㎩츎?ⓩ?

?? 塋뗥뜵凉冶? python master.py
?뮕 ?뽬끾탲鰲? https://github.com/your/playform-ai
"""
        self.console.print(Panel(
            final,
            title="?럦 3燁믣맱?쎿폇鹽뷴츑??,
            border_style="bold magenta"
        ))
    
    def run_3sec_demo(self):
        """瓦먫죱3燁믣맱?쎾츑?닸폇鹽?""
        self.print_stunning_header()
        time.sleep(0.5)
        
        self.show_agent_status()
        time.sleep(0.5)
        
        self.show_statistics()
        time.sleep(0.5)
        
        self.show_animated_progress()
        time.sleep(0.3)
        
        self.show_next_run()
        time.sleep(0.3)
        
        self.show_quick_commands()
        time.sleep(0.3)
        
        self.show_final_message()
        time.sleep(0.5)


def install_rich():
    """?ゅ뒯若됭즳 rich"""
    print("?벀 閭ｅ쑉若됭즳 rich 佯볞빳?룟풓?鵝녘쭍鰲됪븞??..")
    subprocess.run([sys.executable, "-m", "pip", "install", "rich"])


def main():
    # 倻귝옖亦→쐣 rich竊뚦컼瑥뺝츎獒?
    if not HAS_RICH:
        print("?렞 閭ｅ쑉?녶쨭?鵝녘쭍鰲됦퐪謠?..\n")
        try:
            install_rich()
        except Exception as e:
            print(f"?좑툘  若됭즳鸚김뇰竊뚥슴?ⓨ읃簾與▼폀: {e}\n")
    
    # 瓦먫죱轢붺ㅊ
    dashboard = Dashboard3Sec()
    dashboard.run_3sec_demo()
    
    # 雅ㅴ틨?됮」
    print("\n" + "="*60)
    print("?ⓩ꺍誤곦?阿덌폕")
    print("[1] 轢붺ㅊ與▼폀 (python master.py ??[2])")
    print("[2] 若욄뿶瓦먫죱 (python master.py ??[3])")
    print("[3] ?띸쐦訝?띹퓳訝ゆ폇鹽?)
    print("[Q] ???)
    print("="*60)
    
    choice = input("\n?됪떓 (1-3/Q): ").strip().upper()
    
    if choice == "1":
        os.system("python master.py")
    elif choice == "2":
        os.system("python master.py")
    elif choice == "3":
        main()
    elif choice == "Q":
        print("?몝 ?띹쭅!")


if __name__ == "__main__":
    main()


