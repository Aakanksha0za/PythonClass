# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 15:09:35 2026
5. Enforcing Keyword-Only Arguments
Write a function export_data(*items, format="csv", destination="local") that accepts any number of items to export, but strictly requires format and destination to be passed as keyword arguments. Demonstrate that passing them positionally raises a TypeError.

6. Deep Dictionary Merger
Write a function merge_configs(*configs, **overrides) that takes any number of dictionaries as positional arguments and merges them in order from left to right. Finally, apply any key-value pairs inside overrides as the highest-priority settings. Return the combined dictionary.
@author: Admin
"""
5.
def export_data(*items, format="csv", destination="local"):
    """
    Exports items to a destination using the specified format.
    
    *items collects positional arguments.
    'format' and 'destination' must be explicitly provided using key=value syntax.
    """
    print(f"Exporting {len(items)} items as '{format}' to '{destination}'.")
    return {"items": items, "format": format, "destination": destination}


# Demonstration: Valid Usage (Using keyword arguments)
print("--- Valid Usage ---")
export_data("item1", "item2", format="json", destination="cloud")

# Demonstration: Invalid Usage (Passing format positionally)
print("\n--- Invalid Usage ---")
try:
    # Attempting to pass "json" and "cloud" as positional arguments
    export_data("item1", "item2", "json", "cloud")
except TypeError as e:
    print(f"TypeError caught successfully:\n{e}")
    
    
    6.
def merge_configs(*configs, **overrides):
    """
    Merges any number of dictionary configurations from left to right.
    Keyword arguments in `overrides` take top priority.
    """
    result = {}

    # Iterate through all positional dictionary arguments in order
    for config in configs:
        if isinstance(config, dict):
            # Update result: existing keys are overwritten by keys from current config
            result.update(config)

    # Apply highest-priority keyword overrides
    result.update(overrides)

    return result


# Example Usage
default_config = {"host": "localhost", "port": 8080, "debug": False}
environment_config = {"port": 5000, "debug": True}
user_config = {"theme": "dark"}

# Merging dictionaries with an explicit keyword override
final_config = merge_configs(
    default_config, 
    environment_config, 
    user_config, 
    debug=False,  # Overrides 'debug' from environment_config
    verbose=True  # Adds a new highest-priority key
)

print(final_config)