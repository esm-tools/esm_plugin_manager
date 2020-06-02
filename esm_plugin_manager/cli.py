from .esm_plugin_manager import find_installed_plugins

def main():
    discovered_plugins = find_installed_plugins()
    for plugin_name in discovered_plugins:
        plugin_code = discovered_plugins[plugin_name]["callable"]
        print(plugin_name)
        doc = getattr(plugin_code, "__doc__")
        if doc:
            print("-"*len(plugin_name))
            print(doc)
        print("\n")

