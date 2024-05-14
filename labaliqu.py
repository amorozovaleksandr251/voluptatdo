from rich.console import Console

console = Console()

def cprint(text, color):
    console.print(text, style=f"bold {color}")

cprint(f'  {network:<12} added', 'cyan')
