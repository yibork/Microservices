# Microservices Architecture with Eureka and Spring Boot Gateway

## Overview

This project demonstrates a microservices architecture leveraging the Eureka Service Registry and a Spring Boot Gateway for efficient service discovery and routing. The architecture includes two separate microservices applications built with Django, which communicate with each other through defined APIs.

## Components

### Eureka Service Registry

- **Function**: Centralized service registry for our microservices ecosystem.
- **Purpose**: Allows microservices to register their instances and to discover other services for communication.
- **Usage**: Each microservice registers itself with the Eureka server upon startup and queries Eureka to discover the network locations of other services.

### Spring Boot Gateway

- **Function**: An API gateway that provides a single entry point for all client requests.
- **Purpose**: Routes incoming requests to the appropriate microservice based on the request path, method, and other headers.
- **Features**:
  - Request Routing
  - Circuit Breaker patterns
  - Security enforcement, such as authentication and authorization.

### Microservices in Django

- **XtrainUser**: Handles user-related operations (e.g., user authentication, profile management).
- **Xtrain_Diet_Meal**: Manages diet and meal planning functionalities.

## Communication Logic

- **Client Requests**: All client requests are first sent to the Spring Boot Gateway.
- **Service Discovery**: The Gateway queries the Eureka Service Registry to determine the location of the appropriate microservice.
- **Request Routing**: Once the location is known, the Gateway routes the request to the correct microservice.
- **Inter-service Communication**: Microservices communicate with each other using RESTful APIs. They may also use the Eureka Service Registry to discover and communicate with other microservices.
- **Response Aggregation**: The Gateway may also aggregate responses from various microservices and return a consolidated response to the client.

## Setup and Running

(Include instructions on how to set up and run the applications, including starting the Eureka server, running the Spring Boot Gateway, and starting each Django microservice.)

## Conclusion

This setup showcases a resilient and scalable microservices architecture that leverages Eureka and Spring Boot Gateway to manage and route requests to appropriate Django microservices, allowing for a decoupled, maintainable, and scalable system.

