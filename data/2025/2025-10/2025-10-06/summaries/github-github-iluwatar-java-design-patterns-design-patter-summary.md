---
title: GitHub - iluwatar/java-design-patterns: Design patterns implemented in Java
url: https://github.com/iluwatar/java-design-patterns
date:
site: github
model: llama3.2:1b
summarized_at: 2025-10-06T11:17:31.609608
screenshot: github-github-iluwatar-java-design-patterns-design-patter.png
---

# GitHub - iluwatar/java-design-patterns: Design patterns implemented in Java

## Java Design Patterns Implemented in GitHub Repository
==========================

### Overview
------------

This repository showcases a collection of design patterns implemented in Java, demonstrating various creational, structural, and behavioral patterns.

### Main Sections
----------------

#### **Design Patterns Applied**
---------------------------

*   **Creational**:
    *   Singleton pattern: Ensures only one instance of the class is created.
        ```java
class Singleton {
    private static Singleton instance;
    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
}
```

#### **Structural**:
    *   Factory Method pattern: Provides a way to create objects without specifying the exact class of object that will be created.
        ```java
class ShapeFactory {
    public static Object createShape() {
        if (shapeType == null) {
            shapeType = new Rectangle();
        }
        return shapeType;
    }

    private static String shapeType = "Rectangle";
}
```

### Source Code Examples
-------------------------

#### **Singleton Pattern**
```java
class Singleton {
    private static Singleton instance;
    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
}
```
#### **Factory Method pattern**
```java
abstract class Shape {
    abstract void draw();
}

class Circle extends Shape {
    @Override
    public void draw() {
        System.out.println("Drawing a circle");
    }
}

class Rectangle extends Shape {
    @Override
    public void draw() {
        System.out.println("Drawing a rectangle");
    }
}
```

#### **Decorator pattern**
```java
abstract class Component {
    abstract void doSomething();

    void doSomething() {
        System.out.println("Do something");
    }

    Component withAdditionalAction(Component component) {
        System.out.println("Adding additional action");
        return new Composite(component);
    }
}

class ConcreteComponent1 implements Component {
    @Override
    public void doSomething() {
        super.doSomething();
    }
}
```

#### **Adapter pattern**
```java
interface Source {
    void sendNotification();
}

interface Target {
    void receiveNotification();
}

public class Mailender implements Source {
    public interface NotificationReceivable {
        void receiveNotification();
    }

    @Override
    public void sendNotification() {
        // Simulate sending email notification
        Target target = new ConcreteTarget();
                target.receiveNotification();
    }
}
```
#### **Composite pattern**
```java
class Composite {
    private String name;

    public Composite(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void displayInfo() {
        System.out.println("Name: " + name);
    }
}

// Create some concrete elements of composite tree
Composite root = new Composite("Root");
root.appendChild(new Composite("Child A"));
root.appendChild(new Compose("Child B"));

root.displayInfo();  // Output: Name: Root, Child A, Child B
```
