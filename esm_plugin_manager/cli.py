def main():
    import pkg_resources

    discovered_plugins = {
        entry_point.name: entry_point.load()
        for entry_point
        in pkg_resources.iter_entry_points('esm_tools.plugins')
    }

    for plugin_name, plugin_code in discovered_plugins.items():
        print(plugin_name)
        doc = getattr(plugin_code, "__doc__")
        if doc:
            print("-"*len(plugin_name))
            print(doc)
        print("\n")

