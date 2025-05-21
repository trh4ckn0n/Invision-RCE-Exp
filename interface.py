from rich.console import Console
from rich.panel import Panel
from questionary import text

console = Console()

def show_banner():
    console.print(Panel("[bold green]TRHACKNON Mod'Z Invision RCE Exploit[/bold green]\n[violet]Interactive shell - CVE PoC[/violet]", title="trhacknon", subtitle="v1.0"))

def get_target_url():
    return text("Entrer l'URL de la cible (ex: https://site.com:7777)").ask()
