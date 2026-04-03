---
title: Auto-Discovering Console Commands in Power Modules - DEV Community
url: https://dev.to/homeless-coder/auto-discovering-console-commands-in-power-modules-4j8a
date: 2025-10-16
site: devto
model: llama3.2:1b
summarized_at: 2025-10-22T11:29:57.548441
screenshot: devto-auto-discovering-console-commands-in-power-modules.png
---

# Auto-Discovering Console Commands in Power Modules - DEV Community

**Power Modules Console Command Registration Framework**
=====================================================

### Overview

This framework allows for the automatic discovery and registration of console commands across multiple projects that use the Power Modules framework. It extends Symfony's console capabilities to encapsulate modules and their dependencies, leveraging the Modular Architecture for a decoupled setup.

### Implementation

The solution employs the PowerModuleSetup concept to bridge Symfony Console with the Power Modules framework's modular architecture. This approach ensures that modules export console commands while maintaining strict boundaries, and auto-discover and register these commands into a central Console\Application instance.

**ConsoleCommandsSetup class**
---------------------------

```php
final class ConsoleCommandsSetup implements PowerModuleSetup {

    private \Symfony\Component\Console\Application $console;

    public function __construct() {
        $this->console = new Symfony\Component\Console\Application();
    }

    public function setup(PowerModuleSetupDto $dto) {
        if (PowerModuleSetupDto::instance($dto)) {
            return;
        }

        // Direct registration iteration 1
        if ($dto instanceof Command) {
            foreach ($this->getModules() as $module) {
                try {
                    if (!$module instanceof Command) {
                        continue;
                    }
                    $this->registerCommandFromModule($module, $dto);
                } catch (Exception $e) {
                    // Handle errors
                }
            }
        }

        // Direct registration iteration 2 (setup phase)
        if ($dto->getSetupPhase() !== SetupPhase::LAST && $dto->getSetupPhase() === SetupPhase::FIRST) {
            return;
        }

        try {
            foreach ($this->getModules() as $module) {
                try {
                    if (!$module instanceof Command || !$module instanceof SetupCommand) {
                        continue;
                    }
                    $this->registerCommandFromModule($module, $dto);
                } catch (Exception $e) {
                    // Handle errors
                }
            }
        } catch (Exception $e) {
            // Handle errors
        })
    }

    private function getModules() {
        return [
            new OrdersModule(),
            new UsersModule(),
            // Add other modules as needed
        ];
    }

    private function registerCommandFromModule(Command $module, PowerModuleSetupDto $dto) {
        // Register command from module using DI container
        if ($module->instance instanceof Command) {
            // No-op (already handled by Command::class)
        } else {
            // Resolve dependencies and add to Console\Application instance
            $container = new Container();
            try {
                // Resolve dependencies of the current module
                $dependencies = $module->getInstanceDependencies($container);

                // Register command in console application instance
                $this->console->addCommand($module, new $module->className(), null, $dependencies);
            } catch (Exception $e) {
                // Handle errors
            }
        }
    }
}
```

### Usage

```php
$setup = new ConsoleCommandsSetup();
$setup->setup(new PowerModuleSetupDto());
```

This example demonstrates how the `ConsoleCommandsSetup` class can be used to register console commands from different modules in a decoupled setup. The framework ensures that modules export console commands while maintaining strict boundaries, and auto-discover and register these commands into a central Console\Application instance.

Note: This implementation is based on the provided code snippet and might require modifications to fit your specific use case.
