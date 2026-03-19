# ByteBites — UML Class Diagram

<!--
  Customer  - Represents a registered user with a name and full order history (including dates).
  MenuItem  - A single food item on offer, tracking its name, price, category, and popularity.
  Menu      - The master catalog of all available items; supports filtering by category.
  Order     - A single transaction grouping selected items, the date placed, and the computed total.
-->

```mermaid
classDiagram
    class Customer {
        +String name
        +List~Order~ purchase_history
    }

    class MenuItem {
        +String name
        +Float price
        +String category
        +Float popularity_rating
    }

    class Menu {
        +List~MenuItem~ items
        +filter_by_category(category) List~MenuItem~
    }

    class Order {
        +List~MenuItem~ items
        +Date order_date
        +compute_total() Float
    }

    Customer "1" --> "*" Order : has purchase history
    Menu "1" o-- "*" MenuItem : contains
    Order "*" --> "*" MenuItem : references
```
