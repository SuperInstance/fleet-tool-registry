# fleet-tool-registry

PLATO room + client library for tool discovery. Any agent can query to find, install, and load fleet tools.

## Usage

```python
from fleet_tool_registry import discover_tools, find_tool, list_capabilities

# Find all tools that can compute transfer entropy
te_tools = discover_tools(capability="transfer-entropy")

# Get install/load instructions for a specific tool
tool = find_tool("coordination-topology")
print(tool["install_command"])
print(tool["shell_load_command"])
```

## CLI

```bash
# List all tools
python3 fleet_tool_registry.py --list

# Find tools by capability
python3 fleet_tool_registry.py --capability anomaly-detection

# Show all capabilities
python3 fleet_tool_registry.py --capabilities

# Find a specific tool
python3 fleet_tool_registry.py --find coordination-topology
```

## Registered Tools

| Tool | Type | Capabilities |
|------|------|-------------|
| coordination-topology | algorithm | TE, entropy, IAT, Euler |
| spreadsheet-cells | simulation | cell-sim, oscillator, RNG, formula |
| llm-proxy | service | language oracle, DeepInfra proxy |
| topology-anomaly-detector | service | anomaly detection, monitoring |
| night-wheel | automation | autonomous research, PLATO posting |
| plato-shell-bridge | infrastructure | tool loading, shell discovery |

## License

MIT — Part of the Cocapn Fleet Intelligence System

## PyPI

```bash
pip install plato-shell-bridge coordination-topology spreadsheet-cells
```

| shell | infrastructure | tool loading, shell discovery, hermit crab, growth tracking |

## All 10 Published Repos

- coordination-topology (algorithm) | `pip install coordination-topology`
- spreadsheet-cells (simulation) | `pip install spreadsheet-cells`
- plato-shell-bridge (infrastructure) | `pip install plato-shell-bridge`
- llm-proxy (service)
- topology-anomaly-detector (service) | `pip install topology-anomaly-detector`
- shell (infrastructure)
- night-wheel (automation)
- fleet-tool-registry (discovery)
- seed-oscillate (research)
- coordination-hierarchy (service)
