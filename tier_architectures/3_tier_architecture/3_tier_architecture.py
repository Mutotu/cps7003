# Presentation tier => user interface layer where users interact with the application
# Application tier (or business logic layer) => it processes the data and implements the core functionality of the application
# Data tier => responsible for data storage and management
# Each tier runs its own infrastructure
# Main advantages => Managing complexity, improving scalability, and enhancing maintainability

# In a 3-tier architecture, you typically have a presentation (client) layer, a business logic layer (it processes the presentation and data tiers),
#       and a database layer (where the data is stored, retrieved, and managed)
# A basic example is that of a Hotel Online Booking system
# Presentation (Client) Layer: simple command-line interface (CLI) for user interaction
# Business Logic Layer: it handles core functionality and business logic
# Database Layer: it handles data storage and management using SQLite
# Main program: it manages the different functions created in the three tiers