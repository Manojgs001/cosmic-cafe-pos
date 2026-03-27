import random
import time
from rich.console import Console
from rich.panel import Panel

console = Console()

# --- 1. Variables & Datatypes ---
team_name = "Nebula Drifters"
credits = 1500
in_garage = True

# --- 2. Data Structures ---
# Dictionary holding our ship's current stats
ship = {
    "model": "Zephyr Mk II",
    "top_speed": 350,   # km/h
    "hover_height": 12, # meters
    "handling": 80      # out of 100
}

# Dictionary holding available upgrades
shop = {
    "Plasma Thruster": {"cost": 500, "stat": "top_speed", "boost": 50},
    "Repulsor Lift": {"cost": 400, "stat": "hover_height", "boost": 5},
    "Magnetic Stabilizer": {"cost": 300, "stat": "handling", "boost": 15}
}

# List of opponents for the race
opponents = [
    {"name": "Void Runner", "speed": 340},
    {"name": "Star Chaser", "speed": 380},
    {"name": "Meteor Strike", "speed": 420}
]

console.print(Panel.fit(f"[bold cyan]--- Welcome to the {team_name} Anti-Gravity Garage ---[/bold cyan]", border_style="blue"))

# --- 3. Flow Controls ---
while in_garage:
    console.print(f"\n[bold yellow]💰 Credits: ₡{credits}[/bold yellow]")
    console.print(f"[bold green]🚀 Ship: {ship['model']} | Speed: {ship['top_speed']} km/h | Hover: {ship['hover_height']}m | Handling: {ship['handling']}[/bold green]")
    console.print("\n[bold white][1][/bold white] View Upgrade Shop\n[bold white][2][/bold white] Simulate Race\n[bold white][3][/bold white] Exit Garage")
    
    choice = input("Terminal Awaiting Input: ")

    # Conditionals for menu navigation
    if choice == '1':
        console.print("\n[bold magenta]--- UPGRADE SHOP ---[/bold magenta]")
        # For loop to display dictionary items
        for item, details in shop.items():
            console.print(f"[cyan]- {item}[/cyan]: ₡{details['cost']} (+{details['boost']} to {details['stat']})")
        
        buy = input("Enter part name to buy (or type 'back'): ")
        
        # Logic to check if part exists and if player has money
        if buy in shop:
            if credits >= shop[buy]['cost']:
                credits -= shop[buy]['cost']
                stat_to_upgrade = shop[buy]['stat']
                ship[stat_to_upgrade] += shop[buy]['boost']
                console.print(f"[bold green]✅ Successfully installed {buy}![/bold green]")
            else:
                console.print("[bold red]❌ Insufficient credits! Win more races.[/bold red]")
        elif buy.lower() != 'back':
            console.print("[bold red]❌ Part not found in database.[/bold red]")

    elif choice == '2':
        console.print("\n[bold red]🏎️ Initiating Anti-Gravity Sequence...[/bold red]")
        # For loop for race countdown
        for countdown in range(3, 0, -1):
            console.print(f"[bold yellow]Engaging repulsors in {countdown}...[/bold yellow]")
            time.sleep(1)
        console.print("[bold green]GO!!![/bold green]")
        
        # --- Complex Race Logic ---
        opponent = random.choice(opponents)
        console.print(f"\n[white]You are racing against [bold red]{opponent['name']}[/bold red] (Base Speed: {opponent['speed']} km/h)[/white]")
        
        # "Roll a dice" to add random variance to speed
        player_roll = random.randint(10, 60)
        opponent_roll = random.randint(10, 60)
        
        player_total_speed = ship['top_speed'] + player_roll
        opponent_total_speed = opponent['speed'] + opponent_roll
        
        console.print(f"Your speed during the race: [cyan]{player_total_speed} km/h[/cyan] (Base: {ship['top_speed']} + Boost: {player_roll})")
        console.print(f"Opponent's speed during the race: [red]{opponent_total_speed} km/h[/red] (Base: {opponent['speed']} + Boost: {opponent_roll})")
        
        time.sleep(1)
        
        if player_total_speed > opponent_total_speed:
            reward = random.randint(150, 300)
            console.print(f"\n[bold green]🏆 YOU WON THE RACE! 🏆[/bold green]")
            console.print(f"[bold yellow]You earned ₡{reward} credits![/bold yellow]")
            credits += reward
            
            # Tiny chance for a handling or hover deduction/bonus if they won
            if random.random() < 0.2:
                console.print("[bold magenta]🌟 Wow! Your ship's repulsors aligned perfectly, increasing handling permanently by 2![/bold magenta]")
                ship['handling'] += 2
        elif player_total_speed < opponent_total_speed:
            console.print(f"\n[bold red]💀 YOU LOST THE RACE! 💀[/bold red]")
            console.print("Better upgrade your ship and try again.")
        else:
            console.print(f"\n[bold blue]🤝 IT'S A TIE! 🤝[/bold blue]")
            console.print("No credits awarded. It was a photo finish!")
        
    elif choice == '3':
        console.print("[bold blue]Powering down repulsor lifts. See you next time![/bold blue]")
        in_garage = False # Breaks the while loop
        
    else:
        console.print("[bold red]Invalid input. Please select 1, 2, or 3.[/bold red]")
