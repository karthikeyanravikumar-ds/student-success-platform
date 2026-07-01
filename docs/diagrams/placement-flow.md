```mermaid
flowchart TD

A([Start]) --> B[Login]

B --> C{Authentication Successful?}

C -- No --> B

C -- Yes --> D[Placement Dashboard]

D --> E[Manage Companies]

D --> F[Create Placement Drive]

D --> G[View Eligible Students]

D --> H[Applications]

D --> I[Placement Reports]

E --> J([Logout])

F --> J

G --> J

H --> J

I --> J
```