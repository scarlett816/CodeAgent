"""
CodeAgent

程序入口
"""

from rich.console import Console
from rich.panel import Panel

from agent.loop import AgentLoop

console = Console()


def print_banner():
    console.print(
        Panel.fit(
            "[bold cyan]CodeAgent[/bold cyan]\n"
            "Local Coding Assistant",
            border_style="cyan"
        )
    )


def main():

    print_banner()

    agent = AgentLoop()

    while True:

        try:

            user_input = console.input(
                "\n[bold green]User > [/bold green]"
            ).strip()

            if not user_input:
                continue

            if user_input.lower() in [
                "exit",
                "quit",
                "q"
            ]:
                console.print(
                    "\n[yellow]Bye![/yellow]"
                )
                break

            result = agent.run(user_input)

            console.print()

            console.print(
                Panel(
                    result,
                    title="Agent",
                    border_style="blue"
                )
            )

        except KeyboardInterrupt:

            console.print("\n[yellow]Interrupted[/yellow]")

            break

        except Exception as e:

            console.print(
                f"[red]Error:[/red] {e}"
            )


if __name__ == "__main__":

    main()