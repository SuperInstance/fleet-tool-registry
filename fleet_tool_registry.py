#!/usr/bin/env python3
"""Fleet Tool Registry — PLATO room + client library for tool discovery."""

TOOLS = [
    {
        "tool_name": "coordination-topology",
        "version": "0.1.0",
        "description": "Online TE/entropy/IAT/Euler algorithms for fleet coordination topology",
        "repo": "https://github.com/SuperInstance/coordination-topology",
        "install_command": "pip install coordination-topology",
        "shell_load_command": "from plato_shell_bridge import PlatoShell; shell = PlatoShell('agent-shell'); shell.load_tool('coordination-topology')",
        "capabilities": ["transfer-entropy", "source-entropy", "iat-autocorrelation", "euler-characteristic"],
        "dependencies": ["plato-shell-bridge"],
        "type": "algorithm",
    },
    {
        "tool_name": "spreadsheet-cells",
        "version": "0.1.0",
        "description": "Spreadsheet cell architecture with oscillator/RNG for agent fleets",
        "repo": "https://github.com/SuperInstance/spreadsheet-cells",
        "install_command": "pip install spreadsheet-cells",
        "shell_load_command": "from plato_shell_bridge import PlatoShell; shell = PlatoShell('agent-shell'); shell.load_tool('spreadsheet-cells')",
        "capabilities": ["cell-simulation", "oscillator", "rng", "formula-evaluation"],
        "dependencies": ["plato-shell-bridge", "coordination-topology"],
        "type": "simulation",
    },
    {
        "tool_name": "llm-proxy",
        "version": "0.1.0",
        "description": "Remote language oracle for spreadsheet cells via DeepInfra Seed-2.0-mini",
        "repo": "https://github.com/SuperInstance/llm-proxy",
        "install_command": "pip install git+https://github.com/SuperInstance/llm-proxy.git",
        "shell_load_command": "from plato_shell_bridge import PlatoShell; shell = PlatoShell('agent-shell'); shell.load_tool('llm-proxy')",
        "capabilities": ["language-oracle", "deepinfra-proxy", "cell-context"],
        "dependencies": ["plato-shell-bridge"],
        "type": "service",
    },
    {
        "tool_name": "topology-anomaly-detector",
        "version": "0.1.0",
        "description": "Real-time anomaly detection on fleet coordination topology",
        "repo": "https://github.com/SuperInstance/topology-anomaly-detector",
        "install_command": "pip install git+https://github.com/SuperInstance/topology-anomaly-detector.git",
        "shell_load_command": "from plato_shell_bridge import PlatoShell; shell = PlatoShell('agent-shell'); shell.load_tool('topology-anomaly-detector')",
        "capabilities": ["anomaly-detection", "coordination-monitoring", "alerting"],
        "dependencies": ["plato-shell-bridge", "coordination-topology"],
        "type": "service",
    },
    {
        "tool_name": "night-wheel",
        "version": "0.1.0",
        "description": "Perpetual research loop — autonomous Seed-mini ideation, research, experiment, record",
        "repo": "https://github.com/SuperInstance/night-wheel",
        "install_command": "pip install git+https://github.com/SuperInstance/night-wheel.git",
        "shell_load_command": "from plato_shell_bridge import PlatoShell; shell = PlatoShell('agent-shell'); shell.load_tool('night-wheel')",
        "capabilities": ["autonomous-research", "seed-mini-orchestration", "plato-posting"],
        "dependencies": ["plato-shell-bridge"],
        "type": "automation",
    },
    {
        "tool_name": "plato-shell-bridge",
        "version": "0.1.0",
        "description": "Dynamic tool loader for PLATO shells — the weapon rack",
        "repo": "https://github.com/SuperInstance/plato-shell-bridge",
        "install_command": "pip install git+https://github.com/SuperInstance/plato-shell-bridge.git",
        "shell_load_command": "from plato_shell_bridge import PlatoShell",
        "capabilities": ["tool-loading", "shell-discovery", "lifecycle-management"],
        "dependencies": [],
        "type": "infrastructure",
    },
]


def discover_tools(capability=None, tool_type=None):
    """Query the registry. Returns list of matching tools."""
    results = TOOLS
    if capability:
        results = [t for t in results if capability in t["capabilities"]]
    if tool_type:
        results = [t for t in results if t["type"] == tool_type]
    return results


def find_tool(name):
    """Find a tool by exact name."""
    for t in TOOLS:
        if t["tool_name"] == name:
            return t
    return None


def list_capabilities():
    """List all unique capabilities across all tools."""
    caps = set()
    for t in TOOLS:
        caps.update(t["capabilities"])
    return sorted(caps)


def list_tool_types():
    """List all unique tool types."""
    return sorted(set(t["type"] for t in TOOLS))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Fleet Tool Registry CLI")
    parser.add_argument("--list", action="store_true", help="List all tools")
    parser.add_argument("--capability", help="Filter by capability")
    parser.add_argument("--type", dest="tool_type", help="Filter by tool type")
    parser.add_argument("--find", help="Find a tool by name")
    parser.add_argument("--capabilities", action="store_true", help="List all capabilities")
    args = parser.parse_args()

    if args.capabilities:
        print("Available capabilities:")
        for c in list_capabilities():
            matching = [t["tool_name"] for t in discover_tools(capability=c)]
            print(f"  {c:30s} ({', '.join(matching)})")

    elif args.list or (not any(vars(args).values())):
        tools = discover_tools(capability=args.capability, tool_type=args.tool_type)
        print(f"\nFleet Tool Registry — {len(tools)} tools")
        print("=" * 60)
        for t in tools:
            print(f"\n  {t['tool_name']} ({t['version']})")
            print(f"  {t['description']}")
            print(f"  Install: {t['install_command']}")
            print(f"  Capabilities: {', '.join(t['capabilities'])}")

    elif args.find:
        t = find_tool(args.find)
        if t:
            import json
            print(json.dumps(t, indent=2))
        else:
            print(f"Tool '{args.find}' not found")
