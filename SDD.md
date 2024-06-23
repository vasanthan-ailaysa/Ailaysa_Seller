# Ailaysa Book Sellers Page

## Software Requirements Specification
### Data Requirements 
- The site allows publishers to publish their book. Each publisher has unique id, name, address
- A publisher has many books. Each book is written by an author and has a unique id, title, isbn, language, language, etc.,
- A publisher has many staff members. Each has a unique id, name, email

### Functional Requirements
- User Authentication
  - Staff user must be able to register and create account
  - user should be able to log in into and logout from their account in the site
- Book data management
  - logged in staff user must be able to perform crud operations on the book data owned by their publication

### Non Functional Requirements

## Database Schema Design
### Entities and Attributes
  - User (staff member)
    - name
    - email
    - password
    - staff_id
  - Book
    - title
    - author
    - publisher
    - isbn
    - language
    - genre
  - Author
    - name
    - about
  - Publisher
    - name
    - address
    - country

### Relationships
- Publisher - Staff User (one to many)
- Publisher - Book (one to many)
- Author - Book (one to many)

## Development
- User authentication and authorisation API
- Book seller API
- Test cases
- Frontend
- Deployment
- Documentation

## Testing


## Deployment
