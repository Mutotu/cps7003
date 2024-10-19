# Application in which an extra layer is added to
# Separate further concerns
# Improve modularity

# 4 layers =>
#     Presentation tier => user interface layer where users interact with the application
#     Application tier (or business logic layer) => it processes the data and implements the core functionality of the application
#     Data Access tier => responsible for interacting with the database or any other data storage mechanism
#     Data Storage tier (or database tier) => responsible for storage of actual data
#     4-tier architecture can be found in complex enterprise applications (e.g., e-commerce platforms, large-scale business systems).

# Presentation (Client) Layer: simple command-line interface (CLI) that allows the users to browse products, add items to their cart, and make purchases
# Business Logic Layer: backend server that processes user requests, handles business logic, and manages sessions
# Data Services Layer: middleware that manages data access, caching, and API calls to external services (e.g., payment gateways, inventory systems)
# Data Layer: databases that store user information, product details, order histories, and other relevant data
# Main program: it manages the different functions created in the four tiers