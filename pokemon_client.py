import asyncio
import sys

try:
    from fastmcp import Client
except ImportError:
    print("Error: FastMCP module not found.")
    print("Please install it with: pip install fastmcp")
    print("If you've already installed it, make sure you're in the correct virtual environment.")
    sys.exit(1)

async def main():
    # Create client connecting to the poke.py server
    client = Client("poke.py")  # Assumes poke.py exists in the current directory
    
    async with client:
        print("Connected to Pokemon MCP Server")
        
        # List available tools
        tools = await client.list_tools()
        print("\nAvailable tools:")
        for tool in tools:
            print(f"- {tool.name}: {tool.description}")
        
        # Get info about a specific Pokémon
        pokemon_name = "pikachu"
        print(f"\nGetting info for {pokemon_name}...")
        result = await client.call_tool("get_pokemon_info", {"name": pokemon_name})
        print(result[0].text)
        
        # List popular Pokémon
        print("\nListing popular Pokémon...")
        result = await client.call_tool("list_popular_pokemon")
        print(result[0].text)
        
        # Create a tournament squad
        print("\nCreating tournament squad...")
        result = await client.call_tool("create_tournament_squad")
        print(result[0].text)

if __name__ == "__main__":
    print("Starting Pokemon MCP Client...")
    print("Make sure the server (poke.py) is in the same directory")
    print("------------------------------------------------------")
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting tips:")
        print("1. Ensure poke.py is in the current directory")
        print("2. Make sure you've activated your virtual environment")
        print("3. Install required packages: pip install fastmcp httpx") 