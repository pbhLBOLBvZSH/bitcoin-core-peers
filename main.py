import asyncio
import aiohttp
from bitcoinrpc import BitcoinRPC

async def scrapeNodes(rpc):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://bitnodes.io/api/v1/snapshots/latest/') as resp: # cheers
            data = await resp.json()

            for node, details in data['nodes'].items():
                if ".onion" not in node and "[" not in node:
                    try:
                        print(f"Adding node {node}")
                        print(await rpc.acall("addnode", [node, "add"]))
                    except Exception as e:
                        print(f"Failed to add to node {node}")
                    try:
                        print(f"Trying to connect to node {node}")
                        print(await rpc.acall("addnode", [node, "onetry"]))
                    except Exception as e:
                        print(f"Failed to connect to node {node}")

async def main():
    async with BitcoinRPC.from_config("http://127.0.0.1:8332", ("username", "pass")) as rpc:
        await scrapeNodes(rpc)

if __name__ == "__main__":
    asyncio.run(main())
