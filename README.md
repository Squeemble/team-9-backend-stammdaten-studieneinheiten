# UserService

UserService is a Spring Boot-based application designed to manage user-related operations. It leverages modern Java (Java 21) and integrates with various Spring Boot modules for web, data, and testing functionalities.

## Features

- RESTful API for user management
- Integration with H2 in-memory database
- Dependency injection and configuration using Spring Boot
- Unit and integration testing with JUnit 5
- Maven-based build and dependency management

## Prerequisites

- Java 21 or higher
- Maven 3.8 or higher

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/your-repo/userservice.git
cd userservice
```
### Build the Project
```bash
mvn clean install
```
### Run the Application
```bash
mvn spring-boot:run
```
The application will start on http://localhost:8080

## Testing
### Unit Tests
Run unit tests using Maven:
```bash
mvn test
```
### System Tests
Here information will follow, but system tests will be run on a central server and reports will be made.

## Dependencies
The project uses the following key dependencies:
- `spring-boot-starter-web`: For building web applications, including RESTful services.
- `spring-boot-starter-data-jpa`: For integrating with JPA and databases.
- `spring-boot-starter-test`: For testing support, including JUnit 5.
- `h2`: An in-memory database for development and testing purposes.
- `lombok`: For reducing boilerplate code in Java classes.
- `spring-boot-starter-validation`: For validating user input.
- `spring-boot-starter-security`: For securing the application with basic authentication.
- `springdoc-openapi-ui`: For generating OpenAPI documentation and Swagger UI.
- `spring-boot-starter-actuator`: For monitoring and managing the application.
